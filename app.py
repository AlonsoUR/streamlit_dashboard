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
st.sidebar.header("Data Upload")

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
st.sidebar.subheader("Data Visualization")

plot_types = ["Histogram", "Scatter", "Bar Graph"]
fig = None
plot_title = "### Choose a Plot Type and Columns to create a graph"

selected_plot = st.sidebar.selectbox("Select Plot Type", plot_types, index=None)



match selected_plot:
    case "Histogram":
        x_column = st.sidebar.selectbox("Select Column to Plot Histogram", df.columns)
        legends_column = st.sidebar.selectbox("Select Column for Legend", df.columns.drop(x_column))
        plot_title = f"### Distribution of `{x_column}` by `{legends_column}`"
        fig = px.histogram(df, x=x_column, color=legends_column)
    case "Scatter":
        x_column = st.sidebar.selectbox("Select X Column", df.columns)
        y_column = st.sidebar.selectbox("Select Y Column", df.columns.drop(x_column))
        legends_column = st.sidebar.selectbox("Select Column for Legend", df.columns.drop([x_column, y_column]), index=None)
        plot_title = f"### Scatter Plot of `{y_column}` vs `{x_column}`"
        fig = px.scatter(df, x=x_column, y=y_column, color=legends_column)
    case "Bar Graph":
        x_column = st.sidebar.selectbox("Select X Column", df.columns)
        y_column = st.sidebar.selectbox("Select Y Column", df.columns.drop(x_column))
        legends_column = st.sidebar.selectbox("Select Column for Legend", df.columns.drop([x_column, y_column]), index=None)
        plot_title = f"### Bar Graph of `{y_column}` vs `{x_column}`"
        fig = px.bar(df, x=x_column, y=y_column, color=legends_column)        

        

st.markdown(plot_title)
if fig is not None:
    st.plotly_chart(fig, use_container_width=True)

# ================================================
# Footer or Additional Info
# ================================================
st.markdown("---")
st.markdown("Made by AlonsoUR🦉 using Streamlit")