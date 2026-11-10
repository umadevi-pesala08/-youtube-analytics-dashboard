import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="YouTube Analytics | Big Data Project",
    page_icon="▶️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS - COMPLETE TEAL BLUE THEME
# =========================================================

st.markdown("""
<style>

/* =========================================
   COMPLETE APP BACKGROUND
========================================= */

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"] {
    background-color: #008B8B !important;
}

/* Top header area */
[data-testid="stHeader"] {
    background-color: #008B8B !important;
}

/* Main page text */
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6,
.stApp p,
.stApp li {
    color: #FFFFFF;
}

/* =========================================
   SIDEBAR - WHITE BACKGROUND
========================================= */

section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div {
    background-color: #FFFFFF !important;
}

/* Sidebar text - black */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] small {
    color: #000000 !important;
}

/* Sidebar buttons */
section[data-testid="stSidebar"] button {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    border: 1px solid #D1D5DB !important;
}

/* Sidebar uploader */
section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    background-color: #FFFFFF !important;
    border: 1px solid #D1D5DB;
    border-radius: 10px;
    padding: 10px;
}

section[data-testid="stSidebar"] [data-testid="stFileUploader"] * {
    color: #000000 !important;
}

/* =========================================
   ALL INPUT BOXES - WHITE WITH BLACK TEXT
========================================= */

/* Search and text input boxes */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTimeInput input {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    border: 1px solid #D1D5DB !important;
    border-radius: 8px !important;
    -webkit-text-fill-color: #000000 !important;
}

/* Dropdown and multiselect boxes */
.stSelectbox [data-baseweb="select"],
.stMultiSelect [data-baseweb="select"] {
    background-color: #FFFFFF !important;
    border-radius: 8px !important;
}

/* Selected values */
.stSelectbox [data-baseweb="select"] *,
.stMultiSelect [data-baseweb="select"] * {
    color: #000000 !important;
}

/* Dropdown popup */
[data-baseweb="popover"],
[data-baseweb="menu"],
[data-baseweb="list"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] *,
[data-baseweb="list"] * {
    color: #000000 !important;
}

/* =========================================
   DOWNLOAD AND ACTION BUTTONS
========================================= */

.stDownloadButton button,
.stButton button,
.stFormSubmitButton button {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    border: 1px solid #D1D5DB !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

/* Button inner text */
.stDownloadButton button *,
.stButton button *,
.stFormSubmitButton button * {
    color: #000000 !important;
}

/* Button hover */
.stDownloadButton button:hover,
.stButton button:hover,
.stFormSubmitButton button:hover {
    background-color: #E6FFFB !important;
    color: #000000 !important;
    border: 1px solid #006D77 !important;
}

/* =========================================
   METRIC CARDS
========================================= */

div[data-testid="stMetric"] {
    background-color: #006D77 !important;
    border: 1px solid #B2F5EA !important;
    padding: 18px !important;
    border-radius: 14px !important;
}

div[data-testid="stMetric"] label,
div[data-testid="stMetric"] [data-testid="stMetricLabel"],
div[data-testid="stMetric"] [data-testid="stMetricValue"],
div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    color: #FFFFFF !important;
}

/* =========================================
   FILE UPLOADER - WHITE BOX
========================================= */

[data-testid="stFileUploader"] {
    background-color: #FFFFFF !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

[data-testid="stFileUploader"] * {
    color: #000000 !important;
}

/* =========================================
   DATA TABLES
========================================= */

[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background-color: #FFFFFF !important;
    border-radius: 10px !important;
}

/* =========================================
   CHECKBOXES AND RADIO OPTIONS
========================================= */

.stCheckbox label,
.stRadio label,
.stCheckbox p,
.stRadio p {
    color: #FFFFFF !important;
}

/* Sidebar checkbox and radio text remains black */
section[data-testid="stSidebar"] .stCheckbox label,
section[data-testid="stSidebar"] .stRadio label,
section[data-testid="stSidebar"] .stCheckbox p,
section[data-testid="stSidebar"] .stRadio p {
    color: #000000 !important;
}

/* =========================================
   SLIDERS
========================================= */

.stSlider label,
.stSlider p {
    color: #FFFFFF !important;
}

/* =========================================
   LINKS AND DIVIDERS
========================================= */

.stApp a {
    color: #FFFFFF !important;
}

hr {
    border-color: rgba(255, 255, 255, 0.4) !important;
}

/* =========================================
   MAIN PAGE SPACING
========================================= */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
/* Fix top header and prevent text clipping */

[data-testid="stHeader"] {
    background-color: #008B8B !important;
}

/* Main title and subtitle - white */

.stApp .main-title {
    color: #FFFFFF !important;
    font-size: 34px !important;
    font-weight: 800 !important;
    line-height: 1.4 !important;
    margin-top: 10px !important;
    margin-bottom: 10px !important;
    overflow: visible !important;
}

.stApp .subtitle {
    color: #FFFFFF !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    margin-top: 5px !important;
    margin-bottom: 25px !important;
    overflow: visible !important;
}

/* Sidebar title remains black */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #000000 !important;
}

/* Keep main content headings white */

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #FFFFFF !important;
}

/* Ensure top content has enough space */

.block-container {
    padding-top: 2.5rem !important;
    padding-bottom: 2rem !important;
    overflow: visible !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# PROJECT CONSTANTS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

DEFAULT_FILE = DATA_DIR / "trending_videos.csv"


# =========================================================
# DATA LOADING
# =========================================================

@st.cache_data
def load_csv_file(file_bytes):
    from io import BytesIO
    return pd.read_csv(BytesIO(file_bytes))


def normalize_columns(data):
    data = data.copy()
    data.columns = data.columns.str.strip()
    return data


def get_numeric(data, column):
    if column not in data.columns:
        return pd.Series(np.nan, index=data.index)

    return pd.to_numeric(data[column], errors="coerce")


def format_number(value):
    if pd.isna(value):
        return "N/A"

    value = float(value)

    if abs(value) >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"

    if abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"

    if abs(value) >= 1_000:
        return f"{value / 1_000:.2f}K"

    return f"{value:,.0f}"


def find_column(data, candidates):
    for candidate in candidates:
        if candidate in data.columns:
            return candidate

    return None


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">▶ YouTube Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'YouTube Videos Performance Analysis Using Big Data Analytics'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("▶ YouTube Analytics")

st.sidebar.caption("Big Data Analytics Mini Project")

st.sidebar.divider()

page = st.sidebar.radio(
    "ANALYSIS LISTS",
    [
        "Dashboard",
        "Video Performance",
        "Category Analysis",
        "Country Analysis",
        "Yearly Analysis",
        "Engagement Analysis",
        "Dataset Explorer",
        "Data Quality"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("📂 Dataset Upload")

uploaded_file = st.sidebar.file_uploader(
    "Upload a YouTube CSV dataset",
    type=["csv"],
    help="Upload a CSV containing YouTube video analytics."
)

st.sidebar.caption(
    "If no file is uploaded, the default dataset will be used."
)


# =========================================================
# LOAD SELECTED DATASET
# =========================================================

if uploaded_file is not None:

    try:
        raw_df = load_csv_file(uploaded_file.getvalue())
        dataset_name = uploaded_file.name

    except Exception as error:
        st.error(f"Unable to read uploaded CSV: {error}")
        st.stop()

else:

    if not DEFAULT_FILE.exists():

        st.error(
            "Default dataset not found. Please upload a CSV file "
            "using the sidebar or place trending_videos.csv inside "
            "the project's data folder."
        )

        st.stop()

    try:

        raw_df = pd.read_csv(DEFAULT_FILE)
        dataset_name = DEFAULT_FILE.name

    except Exception as error:

        st.error(f"Unable to read default dataset: {error}")
        st.stop()


raw_df = normalize_columns(raw_df)

if raw_df.empty:
    st.error("The selected dataset contains no records.")
    st.stop()


# =========================================================
# COLUMN DETECTION
# =========================================================

title_col = find_column(
    raw_df,
    ["title", "video_title", "name"]
)

channel_col = find_column(
    raw_df,
    ["channel_name", "channel_title", "channel"]
)

views_col = find_column(
    raw_df,
    ["views", "view_count", "total_views"]
)

likes_col = find_column(
    raw_df,
    ["likes", "like_count"]
)

comments_col = find_column(
    raw_df,
    ["comments", "comment_count"]
)

category_col = find_column(
    raw_df,
    ["category", "video_category"]
)

country_col = find_column(
    raw_df,
    ["trending_country", "country", "region"]
)

year_col = find_column(
    raw_df,
    ["year"]
)

date_col = find_column(
    raw_df,
    ["trending_date", "publish_date", "date", "published_at"]
)

subscribers_col = find_column(
    raw_df,
    ["subscriber_count", "subscribers"]
)

engagement_col = find_column(
    raw_df,
    ["engagement_score", "engagement_rate"]
)


# =========================================================
# PREPARE DATA
# =========================================================

df = raw_df.copy()

numeric_columns = [
    views_col,
    likes_col,
    comments_col,
    subscribers_col,
    engagement_col
]

for column in numeric_columns:

    if column is not None:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


if date_col is not None:

    df[date_col] = pd.to_datetime(
        df[date_col],
        errors="coerce"
    )


# Create year from date when year is unavailable
if year_col is None and date_col is not None:

    df["_analysis_year"] = df[date_col].dt.year
    year_col = "_analysis_year"


# =========================================================
# FILTERS
# =========================================================

st.sidebar.subheader("🔎 Filters")

filtered_df = df.copy()


if category_col is not None:

    categories = sorted(
        filtered_df[category_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_categories = st.sidebar.multiselect(
        "Category",
        categories,
        default=categories
    )

    filtered_df = filtered_df[
        filtered_df[category_col]
        .astype(str)
        .isin(selected_categories)
    ]


if country_col is not None:

    countries = sorted(
        filtered_df[country_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_countries = st.sidebar.multiselect(
        "Country",
        countries,
        default=countries
    )

    filtered_df = filtered_df[
        filtered_df[country_col]
        .astype(str)
        .isin(selected_countries)
    ]


if year_col is not None:

    year_values = pd.to_numeric(
        filtered_df[year_col],
        errors="coerce"
    ).dropna()

    available_years = sorted(
        year_values.astype(int).unique().tolist()
    )

    if available_years:

        selected_years = st.sidebar.multiselect(
            "Year",
            available_years,
            default=available_years
        )

        filtered_df = filtered_df[
            pd.to_numeric(
                filtered_df[year_col],
                errors="coerce"
            ).isin(selected_years)
        ]


# =========================================================
# KPI VALUES
# =========================================================

total_records = len(filtered_df)

total_views = (
    filtered_df[views_col].sum()
    if views_col else np.nan
)

total_likes = (
    filtered_df[likes_col].sum()
    if likes_col else np.nan
)

total_comments = (
    filtered_df[comments_col].sum()
    if comments_col else np.nan
)

unique_videos = (
    filtered_df["video_id"].nunique()
    if "video_id" in filtered_df.columns
    else total_records
)

average_views = (
    filtered_df[views_col].mean()
    if views_col else np.nan
)

average_engagement = (
    filtered_df[engagement_col].mean()
    if engagement_col else np.nan
)


# =========================================================
# HELPER: DOWNLOAD CSV
# =========================================================

def download_csv(data, filename, label):

    csv_bytes = data.to_csv(
        index=False
    ).encode("utf-8-sig")

    st.download_button(
        label=label,
        data=csv_bytes,
        file_name=filename,
        mime="text/csv"
    )


# =========================================================
# DASHBOARD PAGE
# =========================================================

if page == "Dashboard":

    st.subheader("📊 Performance Overview")

    st.caption(
        f"Current dataset: {dataset_name} | "
        f"Showing {len(filtered_df):,} filtered records"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Videos / Records",
        format_number(unique_videos)
    )

    col2.metric(
        "Total Views",
        format_number(total_views)
    )

    col3.metric(
        "Total Likes",
        format_number(total_likes)
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Total Comments",
        format_number(total_comments)
    )

    col5.metric(
        "Average Views",
        format_number(average_views)
    )

    col6.metric(
        "Average Engagement",
        (
            f"{average_engagement:.2f}"
            if pd.notna(average_engagement)
            else "N/A"
        )
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.markdown("### 🏆 Top Videos by Views")

        if title_col and views_col:

            top_videos = (
                filtered_df
                .dropna(subset=[views_col])
                .nlargest(10, views_col)
            )

            if not top_videos.empty:

                chart_data = top_videos.copy()

                chart_data["_title"] = (
                    chart_data[title_col]
                    .astype(str)
                    .str.slice(0, 45)
                )

                fig = px.bar(
                    chart_data,
                    x=views_col,
                    y="_title",
                    orientation="h",
                    title="Top 10 Videos",
                    labels={
                        views_col: "Views",
                        "_title": "Video"
                    },
                    template="plotly_dark"
                )

                fig.update_layout(
                    yaxis={"categoryorder": "total ascending"}
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No view data available.")

        else:
            st.info("Video title or views column is missing.")

    with right:

        st.markdown("### 📂 Category Performance")

        if category_col and views_col:

            category_data = filtered_df.copy()

            category_data[views_col] = pd.to_numeric(
                category_data[views_col],
                errors="coerce"
            )

            category_summary = (
                category_data
                .groupby(category_col, dropna=False)[views_col]
                .sum()
                .reset_index()
                .sort_values(views_col, ascending=False)
                .head(10)
            )

            fig = px.pie(
                category_summary,
                names=category_col,
                values=views_col,
                title="Views by Category",
                template="plotly_dark",
                hole=0.45
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.info("Category or views column is missing.")

    st.markdown("### 📈 Views, Likes and Comments")

    available_metrics = [
        column
        for column in [views_col, likes_col, comments_col]
        if column is not None
    ]

    if available_metrics:

        trend_data = (
            filtered_df[available_metrics]
            .sum()
            .reset_index()
        )

        trend_data.columns = ["Metric", "Total"]

        fig = px.bar(
            trend_data,
            x="Metric",
            y="Total",
            color="Metric",
            title="Overall Engagement Metrics",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# VIDEO PERFORMANCE PAGE
# =========================================================

elif page == "Video Performance":

    st.subheader("🎬 Video Performance Analysis")

    if title_col is None:
        st.warning("The dataset does not contain a video title column.")

    else:

        search_text = st.text_input(
            "Search by video title or channel",
            placeholder="Enter video or channel name..."
        )

        search_df = filtered_df.copy()

        if search_text:

            title_match = (
                search_df[title_col]
                .astype(str)
                .str.contains(
                    search_text,
                    case=False,
                    na=False
                )
            )

            if channel_col:

                channel_match = (
                    search_df[channel_col]
                    .astype(str)
                    .str.contains(
                        search_text,
                        case=False,
                        na=False
                    )
                )

                search_df = search_df[
                    title_match | channel_match
                ]

            else:

                search_df = search_df[title_match]


        metric_choice = st.selectbox(
            "Rank videos by",
            [
                column
                for column in [
                    views_col,
                    likes_col,
                    comments_col
                ]
                if column is not None
            ] or [title_col]
        )

        if metric_choice != title_col:

            top_df = (
                search_df
                .dropna(subset=[metric_choice])
                .nlargest(10, metric_choice)
            )

        else:

            top_df = search_df.head(10)


        st.markdown("### 🏆 Top 10 Videos")

        st.dataframe(
            top_df,
            use_container_width=True,
            hide_index=True
        )

        download_csv(
            top_df,
            "top_youtube_videos.csv",
            "⬇️ Download Top 10 Videos"
        )


        if views_col and likes_col:

            st.markdown("### 👍 Views vs Likes")

            scatter_df = search_df.dropna(
                subset=[views_col, likes_col]
            )

            if len(scatter_df) > 2000:

                scatter_df = scatter_df.sample(
                    2000,
                    random_state=42
                )

            hover_columns = [
                column
                for column in [title_col, channel_col]
                if column is not None
            ]

            fig = px.scatter(
                scatter_df,
                x=views_col,
                y=likes_col,
                hover_data=hover_columns,
                title="Relationship Between Views and Likes",
                template="plotly_dark"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


# =========================================================
# CATEGORY ANALYSIS PAGE
# =========================================================

elif page == "Category Analysis":

    st.subheader("📂 Category Analysis")

    if category_col is None:

        st.warning("Category information is not available.")

    else:

        aggregation = {}

        if views_col:
            aggregation[views_col] = ["sum", "mean"]

        if likes_col:
            aggregation[likes_col] = "sum"

        if comments_col:
            aggregation[comments_col] = "sum"

        if aggregation:

            category_summary = (
                filtered_df
                .groupby(category_col)
                .agg(aggregation)
            )

            category_summary.columns = [
                "_".join(
                    str(part)
                    for part in column
                    if part
                )
                for column in category_summary.columns
            ]

            category_summary = (
                category_summary
                .reset_index()
            )

            st.dataframe(
                category_summary,
                use_container_width=True,
                hide_index=True
            )

            download_csv(
                category_summary,
                "category_analysis.csv",
                "⬇️ Download Category Analysis"
            )

            if views_col:

                view_column = f"{views_col}_sum"

                fig = px.bar(
                    category_summary.sort_values(
                        view_column,
                        ascending=False
                    ),
                    x=category_col,
                    y=view_column,
                    title="Total Views by Category",
                    template="plotly_dark"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


# =========================================================
# COUNTRY ANALYSIS PAGE
# =========================================================

elif page == "Country Analysis":

    st.subheader("🌍 Country-wise Analysis")

    if country_col is None:

        st.warning("Country information is not available.")

    else:

        aggregation = {}

        if views_col:
            aggregation[views_col] = ["sum", "mean"]

        if likes_col:
            aggregation[likes_col] = "sum"

        if comments_col:
            aggregation[comments_col] = "sum"

        if aggregation:

            country_summary = (
                filtered_df
                .groupby(country_col)
                .agg(aggregation)
            )

            country_summary.columns = [
                "_".join(
                    str(part)
                    for part in column
                    if part
                )
                for column in country_summary.columns
            ]

            country_summary = country_summary.reset_index()

            st.dataframe(
                country_summary,
                use_container_width=True,
                hide_index=True
            )

            download_csv(
                country_summary,
                "country_analysis.csv",
                "⬇️ Download Country Analysis"
            )

            if views_col:

                view_column = f"{views_col}_sum"

                fig = px.bar(
                    country_summary.sort_values(
                        view_column,
                        ascending=False
                    ),
                    x=country_col,
                    y=view_column,
                    title="Total Views by Country",
                    template="plotly_dark"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


# =========================================================
# YEARLY ANALYSIS PAGE
# =========================================================

elif page == "Yearly Analysis":

    st.subheader("📅 Yearly Performance Analysis")

    if year_col is None:

        st.warning("Year information is not available.")

    else:

        yearly_data = filtered_df.copy()

        yearly_data[year_col] = pd.to_numeric(
            yearly_data[year_col],
            errors="coerce"
        )

        yearly_data = yearly_data.dropna(
            subset=[year_col]
        )

        yearly_data[year_col] = (
            yearly_data[year_col].astype(int)
        )

        aggregation = {}

        if views_col:
            aggregation[views_col] = "mean"

        if likes_col:
            aggregation[likes_col] = "mean"

        if comments_col:
            aggregation[comments_col] = "mean"

        if aggregation:

            yearly_summary = (
                yearly_data
                .groupby(year_col)
                .agg(aggregation)
                .reset_index()
                .sort_values(year_col)
            )

            st.dataframe(
                yearly_summary,
                use_container_width=True,
                hide_index=True
            )

            if views_col:

                fig = px.line(
                    yearly_summary,
                    x=year_col,
                    y=views_col,
                    markers=True,
                    title="Average Views by Year",
                    template="plotly_dark"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            download_csv(
                yearly_summary,
                "yearly_analysis.csv",
                "⬇️ Download Yearly Analysis"
            )


# =========================================================
# ENGAGEMENT ANALYSIS PAGE
# =========================================================

elif page == "Engagement Analysis":

    st.subheader("💬 Engagement Analysis")

    if views_col and likes_col and comments_col:

        engagement_df = filtered_df.copy()

        engagement_df["_views"] = pd.to_numeric(
            engagement_df[views_col],
            errors="coerce"
        )

        engagement_df["_likes"] = pd.to_numeric(
            engagement_df[likes_col],
            errors="coerce"
        )

        engagement_df["_comments"] = pd.to_numeric(
            engagement_df[comments_col],
            errors="coerce"
        )

        engagement_df = engagement_df.dropna(
            subset=["_views", "_likes", "_comments"]
        )

        engagement_df = engagement_df[
            engagement_df["_views"] > 0
        ].copy()

        engagement_df["calculated_engagement_pct"] = (
            (
                engagement_df["_likes"]
                + engagement_df["_comments"]
            )
            / engagement_df["_views"]
        ) * 100

        st.metric(
            "Average Calculated Engagement Rate",
            f"{engagement_df['calculated_engagement_pct'].mean():.2f}%"
            if not engagement_df.empty
            else "N/A"
        )

        st.caption(
            "Calculated as (likes + comments) / views × 100. "
            "This is a simplified project metric."
        )

        if not engagement_df.empty:

            fig = px.scatter(
                engagement_df,
                x="_views",
                y="calculated_engagement_pct",
                title="Views vs Calculated Engagement Rate",
                labels={
                    "_views": "Views",
                    "calculated_engagement_pct": "Engagement Rate (%)"
                },
                template="plotly_dark"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.markdown("### 📊 Correlation Matrix")

            correlation = engagement_df[
                ["_views", "_likes", "_comments"]
            ].corr()

            st.dataframe(
                correlation,
                use_container_width=True
            )

            download_csv(
                engagement_df,
                "engagement_analysis.csv",
                "⬇️ Download Engagement Analysis"
            )

    else:

        st.warning(
            "Engagement analysis requires views, likes and comments columns."
        )


# =========================================================
# DATASET EXPLORER PAGE
# =========================================================

elif page == "Dataset Explorer":

    st.subheader("📁 Dataset Explorer")

    st.write(f"**Dataset:** {dataset_name}")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", f"{len(raw_df):,}")
    col2.metric("Columns", f"{len(raw_df.columns):,}")
    col3.metric(
        "Duplicate Rows",
        f"{raw_df.duplicated().sum():,}"
    )

    st.markdown("### 👀 Data Preview")

    preview_rows = st.slider(
        "Number of rows to display",
        min_value=5,
        max_value=100,
        value=10
    )

    st.dataframe(
        raw_df.head(preview_rows),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 🧾 Column Information")

    column_info = pd.DataFrame({
        "Column": raw_df.columns,
        "Data Type": [
            str(raw_df[column].dtype)
            for column in raw_df.columns
        ],
        "Non-Null Values": [
            int(raw_df[column].notna().sum())
            for column in raw_df.columns
        ],
        "Missing Values": [
            int(raw_df[column].isna().sum())
            for column in raw_df.columns
        ]
    })

    st.dataframe(
        column_info,
        use_container_width=True,
        hide_index=True
    )

    download_csv(
        raw_df,
        "dataset_export.csv",
        "⬇️ Download Current Dataset"
    )


# =========================================================
# DATA QUALITY PAGE
# =========================================================

elif page == "Data Quality":

    st.subheader("🧹 Data Quality & Cleaning")

    missing_count = int(raw_df.isna().sum().sum())

    duplicate_count = int(raw_df.duplicated().sum())

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Rows",
        f"{len(raw_df):,}"
    )

    col2.metric(
        "Missing Cells",
        f"{missing_count:,}"
    )

    col3.metric(
        "Duplicate Rows",
        f"{duplicate_count:,}"
    )

    st.markdown("### 🔎 Missing Values by Column")

    missing_data = pd.DataFrame({
        "Column": raw_df.columns,
        "Missing Values": [
            int(raw_df[column].isna().sum())
            for column in raw_df.columns
        ]
    })

    missing_data = missing_data.sort_values(
        "Missing Values",
        ascending=False
    )

    st.dataframe(
        missing_data,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 🧽 Create a Cleaned Dataset")

    remove_duplicates = st.checkbox(
        "Remove duplicate rows",
        value=True
    )

    fill_missing = st.checkbox(
        "Fill missing numeric values with column median",
        value=False
    )

    cleaned_df = raw_df.copy()

    if remove_duplicates:

        cleaned_df = cleaned_df.drop_duplicates()

    if fill_missing:

        numeric_cols = cleaned_df.select_dtypes(
            include=np.number
        ).columns

        for column in numeric_cols:

            median_value = cleaned_df[column].median()

            if pd.notna(median_value):

                cleaned_df[column] = (
                    cleaned_df[column].fillna(median_value)
                )

    st.success(
        f"Cleaned dataset prepared: {len(cleaned_df):,} rows."
    )

    st.dataframe(
        cleaned_df.head(20),
        use_container_width=True,
        hide_index=True
    )

    download_csv(
        cleaned_df,
        "cleaned_youtube_dataset.csv",
        "⬇️ Download Cleaned Dataset"
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "YouTube Videos Performance Analysis Using Big Data Analytics "
    "| Python • Pandas • Streamlit • Plotly"
)