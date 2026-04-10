import pandas as pd
from config import SCHEMAS


def validate(df: pd.DataFrame, platform: str, file_type: str) -> dict:
    errors = []
    warnings = []

    schema = SCHEMAS[platform][file_type]
    expected = schema["columns"]
    types = schema["types"]
    actual = list(df.columns)

    # ══════════════════════════════════════════
    # CHECK 1 : Column Names (ไม่สนลำดับ)
    # ══════════════════════════════════════════
    missing = [c for c in expected if c not in actual]
    extra = [c for c in actual if c not in expected]

    if missing:
        errors.append({
            "check": "Column Names",
            "detail": (
                f"Column ชื่อไม่ถูกต้อง/ขาดหายไป ({len(missing)} columns): "
                f"{', '.join(missing)}"
            ),
            "fix": "กรุณาแก้ชื่อให้ถูกต้อง/เพิ่ม column ที่ขาดหายไปให้ครบ"
        })

    if extra:
        warnings.append({
            "check": "Extra Columns",
            "detail": (
                f"Column เกินจาก Template ({len(extra)}): "
                f"{', '.join(extra)}"
            ),
            "fix": "ลบ column ที่ไม่อยู่ใน Template ออก"
        })

    # ══════════════════════════════════════════
    # CHECK 2 : Extra Columns & Trailing Blank Rows/Columns
    # ══════════════════════════════════════════

    # ── Extra Columns ─────────────────────────
    extra_cols = [c for c in actual if c not in expected]
    if extra_cols:
        errors.append({
            "check": "Extra Columns",
            "detail": (
                f"พบ column ที่ไม่อยู่ใน Template "
                f"({len(extra_cols)} columns): "
                f"{', '.join(str(c) for c in extra_cols)}"
            ),
            "fix": "ลบ column ที่ไม่อยู่ใน Template ออกจากไฟล์"
        })

    # ── Trailing Blank Rows ────────────────────
    non_blank_df = df.dropna(how="all")

    if len(non_blank_df) < len(df):
        last_data_row_idx = non_blank_df.index.max()
        trailing_rows = df[df.index > last_data_row_idx]

        if len(trailing_rows) > 0:
            errors.append({
                "check": "Trailing Blank Rows",
                "detail": (
                    f"พบแถวว่าง {len(trailing_rows)} แถว "
                    f"หลัง row สุดท้ายที่มีข้อมูล "
                    f"(แถวที่: {list(trailing_rows.index + 2)})"
                ),
                "fix": (
                    f"ลบแถวว่างส่วนเกินออก "
                    f"(ข้อมูลควรจบที่แถว {last_data_row_idx + 2})"
                )
            })

    # ── Trailing Blank Columns ─────────────────
    non_blank_cols = [c for c in df.columns if df[c].notna().any()]

    if non_blank_cols:
        last_data_col_idx = df.columns.get_loc(non_blank_cols[-1])
        trailing_cols = list(df.columns[last_data_col_idx + 1:])

        trailing_extra_cols = [
            c for c in trailing_cols if c not in expected
        ]

        if trailing_extra_cols:
            errors.append({
                "check": "Trailing Blank Columns",
                "detail": (
                    f"พบ column ว่างที่ไม่อยู่ใน Template "
                    f"{len(trailing_extra_cols)} columns "
                    f"({', '.join(str(c) for c in trailing_extra_cols)})"
                ),
                "fix": "ลบ column ว่างส่วนเกินออกจากไฟล์"
            })

    # ══════════════════════════════════════════
    # CHECK 3 : Data Types
    # ══════════════════════════════════════════
    for col, dtype in types.items():
        if col not in df.columns:
            continue

        col_data = df[col].dropna()
        if len(col_data) == 0:
            continue

        if dtype == "int":
            count = pd.to_numeric(col_data, errors="coerce").isnull().sum()
            if count > 0:
                bad_rows = list(
                    df[col][
                        df[col].notna()
                        & pd.to_numeric(df[col], errors="coerce").isnull()
                    ].index[:5] + 2
                )

                errors.append({
                    "check": "Data Type (int)",
                    "detail": (
                        f"'{col}' ต้องเป็นตัวเลขจำนวนเต็ม "
                        f"พบค่าผิด {count} ค่า "
                        f"(ตัวอย่างแถว: {bad_rows})"
                    ),
                    "fix": f"แก้ไขค่าใน '{col}' ให้เป็นตัวเลขจำนวนเต็มเท่านั้น"
                })

        elif dtype == "decimal":
            count = pd.to_numeric(col_data, errors="coerce").isnull().sum()
            if count > 0:
                bad_rows = list(
                    df[col][
                        df[col].notna()
                        & pd.to_numeric(df[col], errors="coerce").isnull()
                    ].index[:5] + 2
                )

                errors.append({
                    "check": "Data Type (decimal)",
                    "detail": (
                        f"'{col}' ต้องเป็นตัวเลขทศนิยม "
                        f"พบค่าผิด {count} ค่า "
                        f"(ตัวอย่างแถว: {bad_rows})"
                    ),
                    "fix": f"แก้ไขค่าใน '{col}' ให้เป็นตัวเลขเท่านั้น"
                })

        elif dtype == "date":
            invalid_count = (
                pd.to_datetime(col_data, dayfirst=True, errors="coerce")
                .isnull()
                .sum()
            )

            if invalid_count > 0:
                errors.append({
                    "check": "Date Format",
                    "detail": (
                        f"'{col}' มีรูปแบบวันที่ไม่ถูกต้อง "
                        f"{invalid_count} ค่า"
                    ),
                    "fix": "รูปแบบที่รองรับ: YYYY-MM-DD หรือ DD/MM/YYYY"
                })

    # ══════════════════════════════════════════
    # สรุปผล
    # ══════════════════════════════════════════
    return {
        "passed": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "total_rows": len(df),
        "total_cols": len(df.columns),
        "platform": platform,
        "file_type": file_type
    }