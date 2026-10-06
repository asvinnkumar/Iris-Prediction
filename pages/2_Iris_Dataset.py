import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Iris Dataset",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

[data-testid="stSidebar"] {
    background-color: #000000 !important;
}

[data-testid="stSidebar"] [data-testid="stSidebarNav"] a,
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a * {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stSidebarNav"] svg {
    fill: #ffffff !important;
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
    color: #ffffff !important;
    background-color: #222222 !important;
}

[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #333333 !important;
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] * {
    color: #ffffff !important;
}

/* ==========================================================
   MAIN APPLICATION
   ========================================================== */

.stApp {
    background-color: #ffffff;
}


/* ==========================================================
   ALL HEADINGS
   ========================================================== */

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #000000 !important;
}


/* ==========================================================
   NORMAL TEXT
   ========================================================== */

p,
li,
span,
label {
    color: #000000 !important;
}


/* ==========================================================
   MAIN TITLE
   ========================================================== */

.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #000000 !important;
}


/* ==========================================================
   SUBTITLE
   ========================================================== */

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555555 !important;
}


/* ==========================================================
   METRIC
   ========================================================== */

/* Metric number */
[data-testid="stMetricValue"] {
    color: #000000 !important;
    font-size: 30px !important;
    font-weight: bold !important;
}


/* Metric label */
[data-testid="stMetricLabel"] {
    color: #000000 !important;
}


/* Metric delta */
[data-testid="stMetricDelta"] {
    color: #000000 !important;
}


/* ==========================================================
   SELECTBOX
   ========================================================== */

/* Selectbox label */
[data-testid="stSelectbox"] label {
    color: #000000 !important;
}


/* Selected value */
[data-testid="stSelectbox"] div {
    color: #000000 !important;
}


/* Selectbox text */
[data-baseweb="select"] {
    color: #000000 !important;
}


/* ==========================================================
   DATAFRAME
   ========================================================== */

[data-testid="stDataFrame"] {
    color: #000000 !important;
}


/* ==========================================================
   INFORMATION / SUCCESS BOXES
   ========================================================== */

[data-testid="stAlert"] p {
    color: #000000 !important;
}

[data-testid="stAlert"] li {
    color: #000000 !important;
}


/* ==========================================================
   DIVIDER
   ========================================================== */

hr {
    border-color: #cccccc !important;
}


/* ==========================================================
   CAPTION
   ========================================================== */

.stCaption {
    color: #555555 !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD IRIS DATASET
# ============================================================

iris = load_iris()


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(
    iris.data,
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)


# ============================================================
# ADD SPECIES
# ============================================================

df["species"] = iris.target_names[iris.target]


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="title">📊 Iris Dataset Visualization</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Explore the relationship between sepal and petal measurements'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# ABOUT DATASET
# ============================================================

st.header("📚 About the Dataset")

st.write("""
The Iris dataset contains measurements of **150 Iris flowers**.

Each flower has four measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The flowers belong to three species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica
""")


# ============================================================
# DATASET SUMMARY
# ============================================================

st.header("📌 Dataset Summary")

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        label="Total Flowers",
        value="150"
    )


with col2:
    st.metric(
        label="Species",
        value="3"
    )


with col3:
    st.metric(
        label="Features",
        value="4"
    )


with col4:
    st.metric(
        label="Dataset Type",
        value="Classification"
    )


# ============================================================
# SHOW DATASET
# ============================================================

st.header("🔎 Iris Dataset")

st.write("""
Here is the complete Iris dataset used for the visualizations.
""")

st.dataframe(
    df,
    use_container_width=True
)


# ============================================================
# SPECIES FILTER
# ============================================================

st.header("🌺 Select Species")

species_options = [
    "All Species",
    "setosa",
    "versicolor",
    "virginica"
]

selected_species = st.selectbox(
    "Choose a species to visualize:",
    species_options
)


if selected_species == "All Species":

    filtered_df = df

else:

    filtered_df = df[
        df["species"] == selected_species
    ]


# ============================================================
# SEPAL LENGTH VS SEPAL WIDTH
# ============================================================

st.header("📏 Sepal Length vs Sepal Width")

st.write("""
This scatter plot shows the relationship between **sepal length**
and **sepal width**.

Each point represents one Iris flower.
""")


fig1 = px.scatter(
    filtered_df,
    x="sepal_length",
    y="sepal_width",
    color="species",
    title="Sepal Length vs Sepal Width",
    labels={
        "sepal_length": "Sepal Length (cm)",
        "sepal_width": "Sepal Width (cm)",
        "species": "Species"
    },
    hover_data=[
        "petal_length",
        "petal_width"
    ]
)


fig1.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(
        color="black"
    ),
    title_font=dict(
        color="black"
    ),
    xaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    yaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    legend=dict(
        font=dict(color="black")
    )
)


st.plotly_chart(
    fig1,
    use_container_width=True
)


# ============================================================
# PETAL LENGTH VS PETAL WIDTH
# ============================================================

st.header("🌸 Petal Length vs Petal Width")

st.write("""
This graph shows the relationship between **petal length**
and **petal width**.

Petal measurements can be very useful for distinguishing
between the three Iris species.
""")


fig2 = px.scatter(
    filtered_df,
    x="petal_length",
    y="petal_width",
    color="species",
    title="Petal Length vs Petal Width",
    labels={
        "petal_length": "Petal Length (cm)",
        "petal_width": "Petal Width (cm)",
        "species": "Species"
    },
    hover_data=[
        "sepal_length",
        "sepal_width"
    ]
)


fig2.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color="black"),
    title_font=dict(color="black"),
    xaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    yaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    legend=dict(
        font=dict(color="black")
    )
)


st.plotly_chart(
    fig2,
    use_container_width=True
)


# ============================================================
# SEPAL LENGTH VS PETAL LENGTH
# ============================================================

st.header("📐 Sepal Length vs Petal Length")

st.write("""
This visualization compares the length of the sepal
with the length of the petal.
""")


fig3 = px.scatter(
    filtered_df,
    x="sepal_length",
    y="petal_length",
    color="species",
    title="Sepal Length vs Petal Length",
    labels={
        "sepal_length": "Sepal Length (cm)",
        "petal_length": "Petal Length (cm)",
        "species": "Species"
    }
)


fig3.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color="black"),
    title_font=dict(color="black"),
    xaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    yaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    legend=dict(
        font=dict(color="black")
    )
)


st.plotly_chart(
    fig3,
    use_container_width=True
)


# ============================================================
# SEPAL WIDTH VS PETAL WIDTH
# ============================================================

st.header("↔️ Sepal Width vs Petal Width")

st.write("""
This graph compares the width of the sepal with the width
of the petal.
""")


fig4 = px.scatter(
    filtered_df,
    x="sepal_width",
    y="petal_width",
    color="species",
    title="Sepal Width vs Petal Width",
    labels={
        "sepal_width": "Sepal Width (cm)",
        "petal_width": "Petal Width (cm)",
        "species": "Species"
    }
)


fig4.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color="black"),
    title_font=dict(color="black"),
    xaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    yaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    legend=dict(
        font=dict(color="black")
    )
)


st.plotly_chart(
    fig4,
    use_container_width=True
)


# ============================================================
# SPECIES COMPARISON
# ============================================================

st.header("🌺 Species Comparison")

st.write("""
The following graph compares the average measurements
of the three Iris species.
""")


average_df = df.groupby("species")[
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
].mean().reset_index()


fig5 = px.bar(
    average_df,
    x="species",
    y=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ],
    barmode="group",
    title="Average Flower Measurements by Species",
    labels={
        "species": "Species",
        "value": "Measurement (cm)",
        "variable": "Feature"
    }
)


fig5.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color="black"),
    title_font=dict(color="black"),
    xaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    yaxis=dict(
        title_font=dict(color="black"),
        tickfont=dict(color="black")
    ),
    legend=dict(
        font=dict(color="black")
    )
)


st.plotly_chart(
    fig5,
    use_container_width=True
)


# ============================================================
# STATISTICAL SUMMARY
# ============================================================

st.header("📊 Statistical Summary")

st.write("""
The table below shows the basic statistical information
for the four numerical features.
""")


st.dataframe(
    df[
        [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ]
    ].describe(),
    use_container_width=True
)


# ============================================================
# KEY OBSERVATIONS
# ============================================================

st.header("🔍 Key Observations")

st.info("""
**🌸 Setosa**

Setosa generally has much smaller petal length and petal width
compared with the other species.

**🌼 Versicolor**

Versicolor generally has measurements between Setosa and
Virginica.

**🌺 Virginica**

Virginica generally has larger petal measurements.

**📊 Important**

Petal length and petal width show a strong visual difference
between the three species, making them useful features for
classification.
""")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Iris Flower Explorer • Dataset Visualization • Streamlit"
)