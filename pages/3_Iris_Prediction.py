import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Iris Prediction",
    page_icon="🤖",
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
    background-color: #ffffff;
}

/* All headings */
h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

/* Normal text */
p, li, label {
    color: #000000 !important;
}

/* Main title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #000000 !important;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555555 !important;
}

/* Number input labels */
[data-testid="stNumberInput"] label {
    color: #000000 !important;
}

/* Number input text */
[data-testid="stNumberInput"] input {
    color: #000000 !important;
    background-color: #ffffff !important;
}

/* Number input buttons */
[data-testid="stNumberInput"] button {
    color: #000000 !important;
}

/* Metric labels */
[data-testid="stMetricLabel"] {
    color: #000000 !important;
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: #000000 !important;
}

/* Button */
.stButton button {
    color: #000000 !important;
    background-color: #ffffff !important;
    border: 2px solid #000000 !important;
    border-radius: 8px;
    font-weight: bold;
}

/* Button hover */
.stButton button:hover {
    color: #ffffff !important;
    background-color: #000000 !important;
}

/* Alert text */
[data-testid="stAlert"] p {
    color: #000000 !important;
}

/* Divider */
hr {
    border-color: #cccccc !important;
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
# FEATURES AND TARGET
# ============================================================

X = df[
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
]

y = iris.target


# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ============================================================
# CREATE MODEL
# ============================================================

model = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression())
    ]
)


# ============================================================
# TRAIN MODEL
# ============================================================

model.fit(
    X_train,
    y_train
)


# ============================================================
# MODEL ACCURACY
# ============================================================

accuracy = model.score(
    X_test,
    y_test
)


# ============================================================
# PAGE TITLE
# ============================================================

st.markdown(
    '<div class="title">🤖 Iris Flower Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter the flower measurements and predict its species'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# INTRODUCTION
# ============================================================

st.header("🌸 Predict the Iris Flower")

st.write("""
Enter the measurements of an Iris flower below.

The Machine Learning model will use these four measurements
to predict the species of the flower.
""")


# ============================================================
# USER INPUT
# ============================================================

st.header("📏 Enter Flower Measurements")


col1, col2 = st.columns(2)


with col1:

    sepal_length = st.number_input(
        "🌿 Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )


with col2:

    sepal_width = st.number_input(
        "🌿 Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )


col3, col4 = st.columns(2)


with col3:

    petal_length = st.number_input(
        "🌸 Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )


with col4:

    petal_width = st.number_input(
        "🌸 Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )


# ============================================================
# ENTERED VALUES
# ============================================================

st.header("📋 Entered Measurements")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Sepal Length",
        f"{sepal_length:.1f} cm"
    )


with col2:

    st.metric(
        "Sepal Width",
        f"{sepal_width:.1f} cm"
    )


with col3:

    st.metric(
        "Petal Length",
        f"{petal_length:.1f} cm"
    )


with col4:

    st.metric(
        "Petal Width",
        f"{petal_width:.1f} cm"
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Flower",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # Create input dataframe

    input_data = pd.DataFrame(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]],
        columns=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ]
    )


    # Make prediction

    prediction = model.predict(
        input_data
    )


    # Get probabilities

    probabilities = model.predict_proba(
        input_data
    )


    # Get predicted class

    predicted_class = prediction[0]


    # Get flower name

    predicted_name = iris.target_names[
        predicted_class
    ]


    # Calculate confidence

    confidence = (
        probabilities[0][predicted_class] * 100
    )


    # ========================================================
    # PREDICTION RESULT
    # ========================================================

    st.divider()

    st.header("🌺 Prediction Result")


    if predicted_name == "setosa":

        st.success("🌸 The predicted flower is **Iris Setosa**")


    elif predicted_name == "versicolor":

        st.success("🌼 The predicted flower is **Iris Versicolor**")


    else:

        st.success("🌺 The predicted flower is **Iris Virginica**")


    # ========================================================
    # CONFIDENCE
    # ========================================================

    st.subheader("🎯 Prediction Confidence")

    st.progress(
        int(confidence)
    )

    st.write(
        f"Model confidence: **{confidence:.2f}%**"
    )


    # ========================================================
    # PROBABILITY TABLE
    # ========================================================

    st.subheader("📊 Prediction Probabilities")


    probability_df = pd.DataFrame(
        {
            "Species": [
                "Iris Setosa",
                "Iris Versicolor",
                "Iris Virginica"
            ],

            "Probability": [
                probabilities[0][0] * 100,
                probabilities[0][1] * 100,
                probabilities[0][2] * 100
            ]
        }
    )


    probability_df["Probability"] = (
        probability_df["Probability"]
        .round(2)
    )


    st.dataframe(
        probability_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# MACHINE LEARNING MODEL
# ============================================================

st.divider()

st.header("🧠 About the Machine Learning Model")

st.write("""
This application uses **Logistic Regression** to classify
the Iris flower.

The four input features are:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Before classification, the features are standardized using
**StandardScaler**.
""")


# ============================================================
# MODEL ACCURACY
# ============================================================

st.header("📈 Model Performance")

st.metric(
    "Test Accuracy",
    f"{accuracy * 100:.2f}%"
)


# ============================================================
# HOW IT WORKS
# ============================================================

st.header("🔄 How Prediction Works")

st.info("""
**Step 1:** Enter the four flower measurements.

↓

**Step 2:** The input values are passed to the model.

↓

**Step 3:** StandardScaler standardizes the measurements.

↓

**Step 4:** Logistic Regression predicts the species.

↓

**Step 5:** The predicted flower name and confidence are displayed.
""")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Iris Flower Explorer • Machine Learning Prediction • Streamlit"
)