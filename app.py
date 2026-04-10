# app.py
import streamlit as st
import pandas as pd
import openpyxl
import io
from config import SCHEMAS
from validator import validate

# ── Page Config ───────────────────────────────
st.set_page_config(
    page_title="Media Data Validator",
    page_icon="📊",
    layout="centered"
)

# ── Header ────────────────────────────────────
st.title("📊 Media Data Validator")
st.caption("ตรวจสอบไฟล์ก่อนนำเข้าระบบ — รองรับทุก Media Platform")
st.divider()

# ── Step 1 : เลือก Platform ──────────────────
st.subheader("Step 1 : เลือก Media Platform")
platform = st.selectbox(
    "Platform",
    options=list(SCHEMAS.keys()),
    index=None,
    placeholder="เลือก Platform..."
)

# ── Step 2 : เลือก File Type ─────────────────
file_type = None
if platform:
    file_types = list(SCHEMAS[platform].keys())

    if len(file_types) == 1:
        # Platform ที่มี file type เดียว
        file_type = file_types[0]
        st.info(f"📂 File Type : **{file_type}**")
    else:
        st.subheader("Step 2 : เลือก File Type")
        file_type = st.selectbox(
            "File Type",
            options=file_types,
            index=None,
            placeholder="เลือก File Type..."
        )

# ── Step 3 : Download Template ───────────────
if platform and file_type:
    schema_cols = SCHEMAS[platform][file_type]["columns"]

    with st.expander("📥 ดาวน์โหลด Template Excel"):
        template_df = pd.DataFrame(columns=schema_cols)
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            template_df.to_excel(writer, index=False, sheet_name="Template")

        st.download_button(
            label="⬇️ Download Template",
            data=buffer.getvalue(),
            file_name=f"template_{platform}_{file_type}.xlsx".replace(" ", "_"),
            mime="application/vnd.ms-excel"
        )
        st.caption(f"Template มีทั้งหมด {len(schema_cols)} columns")

st.divider()

# ── Step 4 : Upload ──────────────────────────
st.subheader("Step 3 : Upload ไฟล์")
uploaded = st.file_uploader(
    "อัพโหลดไฟล์ Excel หรือ CSV",
    type=["xlsx", "xls", "csv"]
)

if uploaded:
    try:
        file_bytes = uploaded.read()

        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(io.BytesIO(file_bytes))
        else:
            wb = openpyxl.load_workbook(io.BytesIO(file_bytes))
            ws = wb.active
            data = list(ws.values)
            wb.close()

            if not data or len(data) < 2:
                st.error("❌ ไฟล์ว่างหรือไม่มีข้อมูล")
                st.stop()

            # แถวแรก = header
            headers = [
                str(h) if h is not None else f"Unnamed_{i}"
                for i, h in enumerate(data[0])
            ]
            rows = data[1:]
            df = pd.DataFrame(rows, columns=headers)

             # แปลง empty string และ None → NaN
             # เพื่อให้ dropna() ทำงานได้ถูกต้อง
            df = df.map(
                 lambda x: None if (
                 x is None or
                 (isinstance(x, str) and x.strip() == "")
                 ) else x
            )

    except Exception as e:
        st.error(f"❌ ไม่สามารถเปิดไฟล์ได้: {e}")
        st.stop()

    st.success(
        f"✅ โหลดไฟล์สำเร็จ : "
        f"**{len(df):,} แถว** | **{len(df.columns)} columns**"
    )

    with st.spinner("🔍 กำลังตรวจสอบข้อมูล..."):
        result = validate(df, platform, file_type)

    st.divider()
    st.subheader("📋 ผลการตรวจสอบ")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Platform", result["platform"])
    col2.metric("File Type", result["file_type"])
    col3.metric("❌ Errors", len(result["errors"]))
    col4.metric("⚠️ Warnings", len(result["warnings"]))

    st.divider()

    if result["passed"]:
        st.success("🎉 ไฟล์ผ่านการตรวจสอบทั้งหมด! พร้อม Upload เข้าระบบ")

        if result["warnings"]:
            st.warning("⚠️ มีข้อควรระวัง (ไม่บล็อกการ Upload)")
            for w in result["warnings"]:
                with st.expander(f"⚠️ {w['check']}"):
                    st.write(w["detail"])
                    st.info(f"💡 {w['fix']}")

        st.subheader("👀 Preview Data")
        st.dataframe(df.head(10), use_container_width=True)

    else:
        st.error(
            f"❌ ไม่ผ่านการตรวจสอบ — "
            f"พบข้อผิดพลาด **{len(result['errors'])} รายการ** "
            f"กรุณาแก้ไขก่อน Upload"
        )

        for i, err in enumerate(result["errors"], 1):
            with st.expander(
                f"🔴 ข้อผิดพลาด #{i} : {err['check']}",
                expanded=True
            ):
                st.write(f"**รายละเอียด:** {err['detail']}")
                st.info(f"💡 วิธีแก้ไข: {err['fix']}")

        if result["warnings"]:
            st.subheader("⚠️ ข้อควรระวังเพิ่มเติม")
            for w in result["warnings"]:
                with st.expander(f"⚠️ {w['check']}"):
                    st.write(w["detail"])
                    st.info(f"💡 {w['fix']}")

        st.divider()
        error_df = pd.DataFrame([
            {
                "ประเภท": err["check"],
                "รายละเอียด": err["detail"],
                "วิธีแก้ไข": err["fix"]
            }
            for err in result["errors"]
        ])

        st.download_button(
            label="📥 Download Error Report",
            data=error_df.to_csv(index=False, encoding="utf-8-sig"),
            file_name="error_report.csv",
            mime="text/csv"
        )