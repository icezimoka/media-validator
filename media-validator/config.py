# config.py

SCHEMAS = {

# ─────────────────────────────────────────
# FACEBOOK
# ─────────────────────────────────────────
"Facebook (FB)": {
    "Placement": {
        "columns": [
            "Campaign name","Ad Set Name","Ad name","Objective","Placement",
            "Day","Impressions","Reach","Clicks (all)","Link clicks",
            "Outbound clicks","Post engagements","Post reactions","Post comments",
            "Post shares","3-second video plays","ThruPlays",
            "Video plays at 25%","Video plays at 50%","Video plays at 75%",
            "Video plays at 100%","Website leads","Meta Leads",
            "Website content views","Amount spent (THB)",
            "Reporting starts","Reporting ends"
        ],
        "types": {
            "Campaign name":"nvarchar","Ad Set Name":"nvarchar",
            "Ad name":"nvarchar","Objective":"nvarchar","Placement":"nvarchar",
            "Day":"date","Impressions":"int","Reach":"int",
            "Clicks (all)":"int","Link clicks":"int","Outbound clicks":"int",
            "Post engagements":"int","Post reactions":"int","Post comments":"int",
            "Post shares":"int","3-second video plays":"int","ThruPlays":"int",
            "Video plays at 25%":"int","Video plays at 50%":"int",
            "Video plays at 75%":"int","Video plays at 100%":"int",
            "Website leads":"int","Meta Leads":"int",
            "Website content views":"int","Amount spent (THB)":"decimal",
            "Reporting starts":"date","Reporting ends":"date"
        }
    },
    "Region": {
        "columns": [
            "Campaign name","Ad Set Name","Ad name","Objective","Region",
            "Day","Impressions","Reach","Clicks (all)","Link clicks",
            "Outbound clicks","Post engagements","Post reactions","Post comments",
            "Post shares","3-second video plays","ThruPlays",
            "Video plays at 25%","Video plays at 50%","Video plays at 75%",
            "Video plays at 100%","Website leads","Meta Leads",
            "Website content views","Amount spent (THB)",
            "Reporting starts","Reporting ends"
        ],
        "types": {
            "Campaign name":"nvarchar","Ad Set Name":"nvarchar",
            "Ad name":"nvarchar","Objective":"nvarchar","Region":"nvarchar",
            "Day":"date","Impressions":"int","Reach":"int",
            "Clicks (all)":"int","Link clicks":"int","Outbound clicks":"int",
            "Post engagements":"int","Post reactions":"int","Post comments":"int",
            "Post shares":"int","3-second video plays":"int","ThruPlays":"int",
            "Video plays at 25%":"int","Video plays at 50%":"int",
            "Video plays at 75%":"int","Video plays at 100%":"int",
            "Website leads":"int","Meta Leads":"int",
            "Website content views":"int","Amount spent (THB)":"decimal",
            "Reporting starts":"date","Reporting ends":"date"
        }
    },
    "Demographic": {
        "columns": [
            "Campaign name","Ad Set Name","Ad name","Objective",
            "Gender","Age","Day","Impressions","Reach","Clicks (all)",
            "Link clicks","Outbound clicks","Post engagements","Post reactions",
            "Post comments","Post shares","3-second video plays","ThruPlays",
            "Video plays at 25%","Video plays at 50%","Video plays at 75%",
            "Video plays at 100%","Website leads","Meta Leads",
            "Website content views","Amount spent (THB)",
            "Reporting starts","Reporting ends"
        ],
        "types": {
            "Campaign name":"nvarchar","Ad Set Name":"nvarchar",
            "Ad name":"nvarchar","Objective":"nvarchar",
            "Gender":"nvarchar","Age":"nvarchar","Day":"date",
            "Impressions":"int","Reach":"int","Clicks (all)":"int",
            "Link clicks":"int","Outbound clicks":"int",
            "Post engagements":"int","Post reactions":"int","Post comments":"int",
            "Post shares":"int","3-second video plays":"int","ThruPlays":"int",
            "Video plays at 25%":"int","Video plays at 50%":"int",
            "Video plays at 75%":"int","Video plays at 100%":"int",
            "Website leads":"int","Meta Leads":"int",
            "Website content views":"int","Amount spent (THB)":"decimal",
            "Reporting starts":"date","Reporting ends":"date"
        }
    }
},

# ─────────────────────────────────────────
# YOUTUBE
# ─────────────────────────────────────────
"YouTube (YT)": {
    "Overall": {
        "columns": [
            "Campaign type","Campaign","Ad group","Ad state","Final URL",
            "Long headline 1","Headline 1","Description 1","Video",
            "Call to action text","Call to action text 1","Video ID",
            "Companion banner","Ad name","Display URL","Path 1","Path 2",
            "Ad type","Campaign ID","Day","Campaign start date","Campaign end date",
            "Impr.","Clicks","Interactions","Engagements","Views",
            "Video played to 25%","Video played to 50%","Video played to 75%",
            "Video played to 100%","YouTube Earned Views","YouTube Earned Likes",
            "YouTube Earned Shares","YouTube Earned Subscribers",
            "YouTube Earned Playlist Additions",
            "Conversions","All conv.","Currency code","Cost"
        ],
        "types": {
            "Campaign type":"nvarchar","Campaign":"nvarchar","Ad group":"nvarchar",
            "Ad state":"nvarchar","Final URL":"nvarchar","Long headline 1":"nvarchar",
            "Headline 1":"nvarchar","Description 1":"nvarchar","Video":"nvarchar",
            "Call to action text":"nvarchar","Call to action text 1":"nvarchar",
            "Video ID":"nvarchar","Companion banner":"nvarchar","Ad name":"nvarchar",
            "Display URL":"nvarchar","Path 1":"nvarchar","Path 2":"nvarchar",
            "Ad type":"nvarchar","Campaign ID":"nvarchar","Day":"date",
            "Campaign start date":"date","Campaign end date":"date",
            "Impr.":"int","Clicks":"int","Interactions":"int",
            "Engagements":"int","Views":"int",
            "Video played to 25%":"decimal","Video played to 50%":"decimal",
            "Video played to 75%":"decimal","Video played to 100%":"decimal",
            "YouTube Earned Views":"nvarchar","YouTube Earned Likes":"nvarchar",
            "YouTube Earned Shares":"nvarchar","YouTube Earned Subscribers":"nvarchar",
            "YouTube Earned Playlist Additions":"nvarchar",
            "Conversions":"decimal","All conv.":"decimal",
            "Currency code":"nvarchar","Cost":"decimal"
        }
    },
    "Region": {
        "columns": [
            "Campaign type","Campaign","Campaign ID","Ad group type","Ad group",
            "Most specific location target (Matched)","Region (Matched)",
            "Day","Campaign start date","Campaign end date",
            "Impr.","Clicks","Interactions","Views",
            "Conversions","All conv.","Currency code","Cost"
        ],
        "types": {
            "Campaign type":"nvarchar","Campaign":"nvarchar","Campaign ID":"nvarchar",
            "Ad group type":"nvarchar","Ad group":"nvarchar",
            "Most specific location target (Matched)":"nvarchar",
            "Region (Matched)":"nvarchar","Day":"date",
            "Campaign start date":"date","Campaign end date":"date",
            "Impr.":"int","Clicks":"int","Interactions":"int","Views":"int",
            "Conversions":"decimal","All conv.":"decimal",
            "Currency code":"nvarchar","Cost":"decimal"
        }
    },
    "Demographic": {
        "columns": [
            "Campaign type","Ad group type","Campaign","Campaign ID","Ad group",
            "Day","Age","Gender","Campaign start date","Campaign end date",
            "Impr.","Clicks","Interactions","Engagements","Views",
            "Video played to 25%","Video played to 50%","Video played to 75%",
            "Video played to 100%","Conversions","All conv.","Currency code","Cost"
        ],
        "types": {
            "Campaign type":"nvarchar","Ad group type":"nvarchar",
            "Campaign":"nvarchar","Campaign ID":"nvarchar","Ad group":"nvarchar",
            "Day":"date","Age":"nvarchar","Gender":"nvarchar",
            "Campaign start date":"date","Campaign end date":"date",
            "Impr.":"int","Clicks":"int","Interactions":"int",
            "Engagements":"int","Views":"int",
            "Video played to 25%":"decimal","Video played to 50%":"decimal",
            "Video played to 75%":"decimal","Video played to 100%":"decimal",
            "Conversions":"decimal","All conv.":"decimal",
            "Currency code":"nvarchar","Cost":"decimal"
        }
    }
},

# ─────────────────────────────────────────
# TIKTOK
# ─────────────────────────────────────────
"TikTok": {
    "Placement": {
        "columns": [
            "Campaign name","Advertising objective","Campaign ID","Ad group name",
            "Ad name","Placements Types","By Day","Schedule","Cost","Impressions",
            "Clicks (destination)","CTR (destination)","Video views",
            "2-second video views","6-second video views",
            "Video views at 100%","Video views at 75%",
            "Video views at 50%","Video views at 25%",
            "Average play time per video view","Paid follows","Paid likes",
            "Paid comments","Paid shares","Paid profile visits","Currency"
        ],
        "types": {
            "Campaign name":"nvarchar","Advertising objective":"nvarchar",
            "Campaign ID":"nvarchar","Ad group name":"nvarchar","Ad name":"nvarchar",
            "Placements Types":"nvarchar","By Day":"date","Schedule":"nvarchar",
            "Cost":"decimal","Impressions":"int","Clicks (destination)":"int",
            "CTR (destination)":"decimal","Video views":"int",
            "2-second video views":"int","6-second video views":"int",
            "Video views at 100%":"int","Video views at 75%":"int",
            "Video views at 50%":"int","Video views at 25%":"int",
            "Average play time per video view":"decimal",
            "Paid follows":"int","Paid likes":"int","Paid comments":"int",
            "Paid shares":"int","Paid profile visits":"int","Currency":"nvarchar"
        }
    },
    "Region": {
        "columns": [
            "Campaign name","Advertising objective","Campaign ID","Ad group name",
            "Ad name","By Day","Schedule","Subregion","Cost","Impressions",
            "Clicks (destination)","CTR (destination)","Video views",
            "2-second video views","6-second video views",
            "Video views at 100%","Video views at 75%",
            "Video views at 50%","Video views at 25%",
            "Average play time per video view","Paid follows","Paid likes",
            "Paid comments","Paid shares","Paid profile visits","Currency"
        ],
        "types": {
            "Campaign name":"nvarchar","Advertising objective":"nvarchar",
            "Campaign ID":"nvarchar","Ad group name":"nvarchar","Ad name":"nvarchar",
            "By Day":"date","Schedule":"nvarchar","Subregion":"nvarchar",
            "Cost":"decimal","Impressions":"int","Clicks (destination)":"int",
            "CTR (destination)":"decimal","Video views":"int",
            "2-second video views":"int","6-second video views":"int",
            "Video views at 100%":"int","Video views at 75%":"int",
            "Video views at 50%":"int","Video views at 25%":"int",
            "Average play time per video view":"decimal",
            "Paid follows":"int","Paid likes":"int","Paid comments":"int",
            "Paid shares":"int","Paid profile visits":"int","Currency":"nvarchar"
        }
    },
    "Demographic": {
        "columns": [
            "Campaign name","Advertising objective","Campaign ID","Ad group name",
            "Ad name","By Day","Schedule","Gender","Age","Cost","Impressions",
            "Clicks (destination)","CTR (destination)","Video views",
            "2-second video views","6-second video views",
            "Video views at 100%","Video views at 75%",
            "Video views at 50%","Video views at 25%",
            "Average play time per video view","Paid follows","Paid likes",
            "Paid comments","Paid shares","Paid profile visits","Currency"
        ],
        "types": {
            "Campaign name":"nvarchar","Advertising objective":"nvarchar",
            "Campaign ID":"nvarchar","Ad group name":"nvarchar","Ad name":"nvarchar",
            "By Day":"date","Schedule":"nvarchar","Gender":"nvarchar","Age":"nvarchar",
            "Cost":"decimal","Impressions":"int","Clicks (destination)":"int",
            "CTR (destination)":"decimal","Video views":"int",
            "2-second video views":"int","6-second video views":"int",
            "Video views at 100%":"int","Video views at 75%":"int",
            "Video views at 50%":"int","Video views at 25%":"int",
            "Average play time per video view":"decimal",
            "Paid follows":"int","Paid likes":"int","Paid comments":"int",
            "Paid shares":"int","Paid profile visits":"int","Currency":"nvarchar"
        }
    }
},

# ─────────────────────────────────────────
# LINE ADS
# ─────────────────────────────────────────
"Line Ads": {
    "AD DETAILS": {
        "columns": [
            "Day","Ad account name","Campaign name","Campaign objective",
            "Ad group name","Ad name","Title","Description","Impressions",
            "Viewable impressions","Clicks","CTR (click-through rate)","Cost",
            "Currency","Video (viewed for at least three seconds)",
            "Video (25% watched)","Video (50% watched)",
            "Video (75% watched)","Video (95% watched)",
            "Video (100% watched)","Age","Gender"
        ],
        "types": {
            "Day":"date","Ad account name":"nvarchar","Campaign name":"nvarchar",
            "Campaign objective":"nvarchar","Ad group name":"nvarchar",
            "Ad name":"nvarchar","Title":"nvarchar","Description":"nvarchar",
            "Impressions":"int","Viewable impressions":"int","Clicks":"int",
            "CTR (click-through rate)":"decimal","Cost":"decimal",
            "Currency":"nvarchar",
            "Video (viewed for at least three seconds)":"int",
            "Video (25% watched)":"int","Video (50% watched)":"int",
            "Video (75% watched)":"int","Video (95% watched)":"int",
            "Video (100% watched)":"int","Age":"nvarchar","Gender":"nvarchar"
        }
    }
},

# ─────────────────────────────────────────
# SEM
# ─────────────────────────────────────────
"SEM": {
    "Overall": {
        "columns": [
            "Campaign","Ad group","Region","Day","Impr.","Clicks",
            "Currency code","Avg. CPC","CTR","Conversions","Conv. rate",
            "Cost / conv.","Cost","Reporting Start Date","Reporting End Date"
        ],
        "types": {
            "Campaign":"nvarchar","Ad group":"nvarchar","Region":"nvarchar",
            "Day":"date","Impr.":"int","Clicks":"int","Currency code":"nvarchar",
            "Avg. CPC":"decimal","CTR":"decimal","Conversions":"decimal",
            "Conv. rate":"decimal","Cost / conv.":"decimal","Cost":"decimal",
            "Reporting Start Date":"date","Reporting End Date":"date"
        }
    }
},

# ─────────────────────────────────────────
# GDN
# ─────────────────────────────────────────
"GDN": {
    "Overall": {
        "columns": [
            "Campaign type","Ad type","Campaign","Ad group","Ad name",
            "Day","Campaign start date","Campaign end date",
            "Impr.","Clicks","Interactions","Engagements","Views",
            "Video played to 25%","Video played to 50%",
            "Video played to 75%","Video played to 100%",
            "Conversions","All conv.","Currency code","Cost"
        ],
        "types": {
            "Campaign type":"nvarchar","Ad type":"nvarchar",
            "Campaign":"nvarchar","Ad group":"nvarchar","Ad name":"nvarchar",
            "Day":"date","Campaign start date":"date","Campaign end date":"date",
            "Impr.":"int","Clicks":"int","Interactions":"int",
            "Engagements":"int","Views":"int",
            "Video played to 25%":"decimal","Video played to 50%":"decimal",
            "Video played to 75%":"decimal","Video played to 100%":"decimal",
            "Conversions":"decimal","All conv.":"decimal",
            "Currency code":"nvarchar","Cost":"decimal"
        }
    },
    "Region": {
        "columns": [
            "Campaign type","Campaign","Ad group","Region (Matched)",
            "Day","Campaign start date","Campaign end date",
            "Impr.","Clicks","Interactions","All conv.","Currency code","Cost"
        ],
        "types": {
            "Campaign type":"nvarchar","Campaign":"nvarchar","Ad group":"nvarchar",
            "Region (Matched)":"nvarchar","Day":"date",
            "Campaign start date":"date","Campaign end date":"date",
            "Impr.":"int","Clicks":"int","Interactions":"int",
            "All conv.":"decimal","Currency code":"nvarchar","Cost":"decimal"
        }
    },
    "Demographic": {
        "columns": [
            "Campaign type","Campaign","Day","Campaign start date","Campaign end date",
            "Age","Gender","Impr.","Clicks","Interactions","Engagements","Views",
            "Video played to 25%","Video played to 50%",
            "Video played to 75%","Video played to 100%",
            "Conversions","All conv.","Currency code","Cost"
        ],
        "types": {
            "Campaign type":"nvarchar","Campaign":"nvarchar",
            "Day":"date","Campaign start date":"date","Campaign end date":"date",
            "Age":"nvarchar","Gender":"nvarchar",
            "Impr.":"int","Clicks":"int","Interactions":"int",
            "Engagements":"int","Views":"int",
            "Video played to 25%":"decimal","Video played to 50%":"decimal",
            "Video played to 75%":"decimal","Video played to 100%":"decimal",
            "Conversions":"decimal","All conv.":"decimal",
            "Currency code":"nvarchar","Cost":"decimal"
        }
    }
},

# ─────────────────────────────────────────
# TABOOLA
# ─────────────────────────────────────────
"Taboola": {
    "AD DETAILS": {
        "columns": [
            "Delivery Status","Title","URL","Campaign Name",
            "Viewable Impressions","CTR","Clicks","Spent"
        ],
        "types": {
            "Delivery Status":"nvarchar","Title":"nvarchar",
            "URL":"nvarchar","Campaign Name":"nvarchar",
            "Viewable Impressions":"int","CTR":"decimal",
            "Clicks":"int","Spent":"decimal"
        }
    }
},

# ─────────────────────────────────────────
# PUBLISHER
# ─────────────────────────────────────────
"Publisher": {
    "AD DETAILS": {
        "columns": [
            "Website","Position","Model","Campaign Name","Date",
            "Impressions","Clicks","%CTR","Amount_Spent"
        ],
        "types": {
            "Website":"nvarchar","Position":"nvarchar","Model":"nvarchar",
            "Campaign Name":"nvarchar","Date":"date",
            "Impressions":"int","Clicks":"int",
            "%CTR":"nvarchar","Amount_Spent":"decimal"
        }
    }
},

# ─────────────────────────────────────────
# OTHERS
# ─────────────────────────────────────────
"Others": {
    "AD DETAILS": {
        "columns": [
            "Campaign Name","Impressions","Clicks","Views","Amount_Spent"
        ],
        "types": {
            "Campaign Name":"nvarchar","Impressions":"int",
            "Clicks":"int","Views":"int","Amount_Spent":"decimal"
        }
    }
}
}