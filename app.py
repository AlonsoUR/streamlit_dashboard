# ================================================
# Imports
# ================================================
import pandas as pd
import streamlit as st
import plotly.express as px

# ================================================
# Constants and Global Variables
# ================================================


# ================================================
# Data Loading and Preprocessing
# ================================================
#load data set
vehicles = pd.read_csv("C:/Git/streamlit_dashboard/vehicles_us.csv")

#remove and fill NaN's
vehicles = vehicles.dropna(subset=["model_year","cylinders","odometer"])
vehicles["paint_color"] = vehicles["paint_color"].fillna("unkown")
vehicles["is_4wd"] = vehicles["is_4wd"].fillna(0) 

#change data types  
vehicles["model_year"] = vehicles["model_year"].astype("int32")
vehicles["cylinders"] = vehicles["cylinders"].astype("int32")
vehicles["odometer"] = vehicles["odometer"].astype("int64")
vehicles["is_4wd"] = vehicles["is_4wd"].astype("bool")
vehicles["date_poset"] = vehicles["date_posted"].astype("datetime64[ns]")


#vehicles.info()


# ================================================
# Helper Functions
# ================================================


# ================================================
# Streamlit UI Layout and Widgets
# ================================================


# ================================================
# Data Visualization
# ================================================


# ================================================
# Main Execution Logic
# ================================================


# ================================================
# Entry Point
# ================================================
if __name__ == "__main__":
    pass

