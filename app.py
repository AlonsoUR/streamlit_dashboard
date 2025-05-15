# ================================================
# Imports
# ================================================
import streamlit as st
import pandas as pd
import plotly.express as px

# ================================================
# Page Configuration
# ================================================
st.set_page_config(
    page_title="Streamlit Data Viewer",
    page_icon="📊",
    layout="wide"
)

# ================================================
# App Title and Description
# ================================================
st.title("Streamlit Quick Data Viewer")
st.markdown("Simple Streamlit Web App for quick data clean up and vizualization")

# ================================================
# Sidebar Controls
# ================================================
st.sidebar.header("Data Handling")

uploaded_file = st.sidebar.file_uploader("Upload a CSV", type="csv")


st.sidebar.header("NA Values Handler")


# ================================================
# Data Loading
# ================================================
sample_file = ("vehicles_us.csv")

@st.cache_data
def load_data(file):
    if file == None:
        df = pd.read_csv(sample_file)
        st.sidebar.markdown("Using Sample Vehicle Sales Data. Upload a CSV File to begin data visualization")
    else:
        df = pd.read_csv(file)
    return df


if "df" not in st.session_state:
    st.session_state.df = load_data(uploaded_file)


# ================================================
# Data Cleaning / Preprocessing
# ================================================



# Show columns with missing values only
if st.sidebar.button("Reset"):
    st.session_state.df = load_data(uploaded_file)

df = st.session_state.df
na_columns = df.columns[df.isna().any()].tolist()

if na_columns:
    selected_columns = st.sidebar.multiselect("Select columns with missing values", na_columns)

    action = st.sidebar.radio("Choose action", ("Drop rows with NA", "Fill NA with value"))

    if action == "Fill NA with value":
        fill_value = st.sidebar.text_input("Value to fill NA with", value="0")

def clean_data(df):
    clean_df = df.copy()

    if na_columns and selected_columns:
        if action == "Drop rows with NA":
            clean_df.dropna(subset=selected_columns, inplace=True)
        elif action == "Fill NA with value":
            clean_df[selected_columns] = clean_df[selected_columns].fillna(fill_value)

    return clean_df

if st.sidebar.button("Clean"):
    st.session_state.df = clean_data(st.session_state.df)


# ================================================
# Data Display
# ================================================
df = st.session_state.df
st.subheader("Raw Data")
st.dataframe(df)



# ================================================
# Visualization
# ================================================
st.subheader("Sample Plot")
fig = px.line(df, x='A', y='B', title="Line Chart")
st.plotly_chart(fig, use_container_width=True)

# ================================================
# Footer or Additional Info
# ================================================
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")