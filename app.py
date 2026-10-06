# import streamlit as st
# import pandas as pd
# st.title("My First Streamlit Application")

# st.header("Welcome to my app!")
# st.subheader("This is a simple Streamlit application.")
# st.write("You can use Streamlit to create interactive web applications with Python.")   
# st.text("This is a text element.")

# df = pd.DataFrame({
#     "Name": ["Alice", "Bob", "Charlie", "David"],
#     "Age": [25, 30, 35, 40],
#     "City": ["New York", "Los Angeles", "Chicago", "Houston"]
# })

# st.table(df)
# st.bar_chart(df,x="Name",y="Age")

# import streamlit as st

import streamlit as st

# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="Iris Explorer",
    page_icon="🌸",
    layout="wide"
)

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>

/* =================================
   MAIN PAGE
   ================================= */

.stApp {
    background-color: #ffffff;
}

/* Main headings */
h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

/* Main text */
p, li, label {
    color: #000000 !important;
}


/* =================================
   SIDEBAR
   ================================= */

[data-testid="stSidebar"] {
    background-color: #000000 !important;
}

/* Keep sidebar navigation readable on every page */
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


/* =================================
   SIDEBAR COLLAPSE BUTTON
   ================================= */

[data-testid="stSidebar"] button {
    color: #ffffff !important;
}


/* =================================
   DIVIDER
   ================================= */

hr {
    border-color: #cccccc !important;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# MAIN PAGE
# ==============================

st.title("🌸 Iris Flower Explorer")

st.write(
    """
    Welcome to the Iris Flower Explorer.

    Use the pages in the sidebar to learn about the Iris flower,
    explore the Iris dataset, and make predictions using machine learning.
    """
)

st.info("👈 Select **Iris Overview** from the sidebar to get started.")