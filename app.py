import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(
    page_title="Local Food Wastage Management",
    layout="wide"
)

conn = sqlite3.connect("food.db")

try:
    df = pd.read_sql(
        "SELECT * FROM food",
        conn
    )

except Exception as e:

    st.error(
        f"Database Error: {e}"
    )

    st.stop()

st.title(
    "🍱 Local Food Wastage Management Dashboard"
)

st.sidebar.title(
    "🛠️ Dashboard Control Panel"
)

city = st.sidebar.multiselect(
    "📍 Filter by City Location",
    sorted(df["city"].unique())
)

provider = st.sidebar.multiselect(
    "🏢 Filter by Provider Type",
    sorted(df["provider_type"].unique())
)

meal = st.sidebar.multiselect(
    "⏰ Filter by Meal Time Windows",
    sorted(df["meal_type"].unique())
)

diet = st.sidebar.multiselect(
    "🥦 Filter by Dietary Food Type",
    sorted(df["diet_type"].unique())
)

filtered = df.copy()

if city:
    filtered = filtered[
        filtered.city.isin(city)
    ]

if provider:
    filtered = filtered[
        filtered.provider_type.isin(provider)
    ]

if meal:
    filtered = filtered[
        filtered.meal_type.isin(meal)
    ]

if diet:
    filtered = filtered[
        filtered.diet_type.isin(diet)
    ]

st.subheader(
    "📊 Executive Dashboard"
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Listings",
    len(filtered)
)

c2.metric(
    "Total Quantity",
    int(filtered["quantity"].sum())
)

c3.metric(
    "Cities Covered",
    filtered["city"].nunique()
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        filtered,
        x="city",
        y="quantity",
        color="meal_type",
        title="Food Quantity by City"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig2 = px.pie(
        filtered,
        names="diet_type",
        values="quantity",
        title="Diet Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

st.subheader(
    "🗄️ SQL Query Analysis"
)

query = st.text_area(
    "Write SQL Query",
    "SELECT city, SUM(quantity) AS total FROM food GROUP BY city"
)

if st.button(
    "Run SQL"
):

    try:

        result = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            result,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            str(e)
        )

st.divider()

st.subheader(
    "📋 Raw Dataset"
)

st.dataframe(
    filtered,
    use_container_width=True
)