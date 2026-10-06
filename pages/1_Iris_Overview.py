import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Iris Overview",
    page_icon="🌸",
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

.stApp {
    background-color: white;
}

/* Main title */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #000000;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555555;
}

/* All headings */
h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

/* Normal text */
p {
    color: #222222;
}

/* Streamlit markdown text */
.stMarkdown {
    color: #222222;
}

/* Information boxes */
.stAlert {
    color: #000000;
}

/* Metric labels */
[data-testid="stMetricLabel"] {
    color: #000000 !important;
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: #000000 !important;
}

/* Divider */
hr {
    border-color: #dddddd;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="title">🌸 Iris Flower</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Understanding the Iris Flower and the Iris Dataset'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# WHAT IS IRIS?
# ============================================================

st.header("🌱 What is Iris?")

st.write("""
Iris is a genus of flowering plants known for its beautiful
and colorful flowers.

The Iris flower is also very important in the field of
Machine Learning because measurements of Iris flowers are
used in one of the most famous beginner datasets.
""")


# ============================================================
# IRIS DATASET
# ============================================================

st.header("📊 What is the Iris Dataset?")

st.write("""
The Iris dataset is a collection of measurements taken from
Iris flowers.

It contains **150 flower samples** belonging to three different
Iris species.

Each flower is described using four measurements:
""")

st.info("""
**1. Sepal Length**

**2. Sepal Width**

**3. Petal Length**

**4. Petal Width**
""")


# ============================================================
# THREE IRIS SPECIES
# ============================================================

st.header("🌺 Three Iris Species")

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("### 🌸 Iris Setosa")

    st.write("""
    Iris Setosa is one of the three species in the
    classic Iris dataset.

    It generally has smaller petals compared with
    the other two species.

    Setosa is usually easier to distinguish because
    its petal measurements are considerably smaller.
    """)


with col2:

    st.markdown("### 🌼 Iris Versicolor")

    st.write("""
    Iris Versicolor is another species included in
    the dataset.

    Its measurements generally fall between Setosa
    and Virginica.

    It can sometimes be more difficult to distinguish
    from Virginica.
    """)


with col3:

    st.markdown("### 🌺 Iris Virginica")

    st.write("""
    Iris Virginica is the third species in the dataset.

    It generally has larger petals compared with
    Setosa.

    It usually has larger flower measurements than
    the other species.
    """)


# ============================================================
# SEPAL AND PETAL
# ============================================================

st.divider()

st.header("🌿 Understanding the Flower")

col1, col2 = st.columns(2)


with col1:

    st.markdown("### 🍃 What is a Sepal?")

    st.write("""
    A **sepal** is a leaf-like structure found underneath
    the flower.

    Its main purpose is to protect the flower while it is
    developing as a bud.

    In the Iris dataset, we measure:

    • Sepal Length

    • Sepal Width
    """)


with col2:

    st.markdown("### 🌸 What is a Petal?")

    st.write("""
    A **petal** is one of the colorful parts of a flower.

    Petals can help attract pollinators such as bees and
    butterflies.

    In the Iris dataset, we measure:

    • Petal Length

    • Petal Width
    """)


# ============================================================
# FOUR MEASUREMENTS
# ============================================================

st.header("📏 The Four Measurements")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown("### 📏 Sepal Length")

    st.write("""
    Measures how long the sepal is.

    It is usually measured in centimeters (cm).
    """)


with col2:

    st.markdown("### ↔️ Sepal Width")

    st.write("""
    Measures how wide the sepal is at its widest point.

    It is usually measured in centimeters (cm).
    """)


with col3:

    st.markdown("### 📏 Petal Length")

    st.write("""
    Measures the length of the petal from its base
    towards its tip.

    It is usually measured in centimeters (cm).
    """)


with col4:

    st.markdown("### ↔️ Petal Width")

    st.write("""
    Measures the width of the petal at its widest point.

    It is usually measured in centimeters (cm).
    """)


# ============================================================
# LENGTH VS WIDTH
# ============================================================

st.header("📐 Length vs Width")

col1, col2 = st.columns(2)


with col1:

    st.markdown("### 📏 Length")

    st.write("""
    **Length** tells us how long a particular part
    of the flower is.

    For example, if a petal has a length of **5 cm**,
    it means the petal is approximately 5 centimeters
    long.
    """)


with col2:

    st.markdown("### ↔️ Width")

    st.write("""
    **Width** tells us how wide a particular part
    of the flower is.

    For example, if a petal has a width of **1.5 cm**,
    it means the petal is approximately 1.5 centimeters
    wide.
    """)


# ============================================================
# EXAMPLE FLOWER
# ============================================================

st.header("🔍 Example Flower")

st.write("""
Imagine that we measure a flower and obtain the following
values:
""")

example_col1, example_col2, example_col3, example_col4 = st.columns(4)


with example_col1:

    st.metric(
        label="Sepal Length",
        value="5.1 cm"
    )


with example_col2:

    st.metric(
        label="Sepal Width",
        value="3.5 cm"
    )


with example_col3:

    st.metric(
        label="Petal Length",
        value="1.4 cm"
    )


with example_col4:

    st.metric(
        label="Petal Width",
        value="0.2 cm"
    )


# ============================================================
# WHY IRIS IS IMPORTANT
# ============================================================

st.header("🤖 Why is Iris Important in Machine Learning?")

st.write("""
The Iris dataset is commonly used to demonstrate
**classification** in Machine Learning.

The four flower measurements become the input features
of the machine learning model.
""")

st.info("""
### Machine Learning Process

**Input Features**

Sepal Length

Sepal Width

Petal Length

Petal Width

↓

**Machine Learning Model**

↓

**Predicted Species**

Setosa / Versicolor / Virginica
""")


# ============================================================
# WHAT WE LEARNED
# ============================================================

st.header("📝 What We Learned")

st.success("""
🌸 Iris is a flowering plant.

🍃 Sepals protect the developing flower.

🌺 Petals are the colorful parts of the flower.

📏 The Iris dataset uses four measurements:
Sepal Length, Sepal Width, Petal Length and Petal Width.

🌼 The dataset contains three species:
Setosa, Versicolor and Virginica.

🤖 These measurements can be used to classify an Iris flower
using Machine Learning.
""")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Iris Flower Explorer • Streamlit Machine Learning Project"
)