import streamlit as st
import pandas as pd
import altair as alt

# Function to load data
def load_data(csv_file):
    return pd.read_csv(csv_file)

# Load the data
df = load_data('data/social_media.csv')

# Streamlit app title
st.title('Social Media Analysis')

# Sidebar for dynamic selection
st.sidebar.header('Select Visualization and Analysis Options')

# Option to select visualization
visualization_option = st.sidebar.radio("Select Visualization:",
                                       ("Count of Users by Platform", "Count of Users by Gender and Platform"))

# Option to select analysis
analysis_option = st.sidebar.checkbox("Show Analysis")

# Visualization 1: Bar chart showing count of users by platform
if visualization_option == "Count of Users by Platform":
    st.header('Count of Users by Platform')

    # Dynamic selection of variables
    x_variable = st.selectbox("Select X Variable:", df.columns)
    y_variable = 'count()'

    platform_counts = df.groupby(x_variable).size().reset_index(name='count()')
    platform_chart = alt.Chart(platform_counts).mark_bar().encode(
        x=alt.X(f'{x_variable}:N', title=x_variable),
        y=alt.Y(y_variable, title='Count'),
        color=alt.Color(f'{x_variable}:N', legend=None)
    ).properties(width=600, height=400)
    st.altair_chart(platform_chart)

    # Analysis for platform count
    if analysis_option:
        st.subheader("Analysis for Count of Users by Platform")
        st.write("The chart above shows the distribution of users across different social media platforms. "
                 "From the analysis")

# Visualization 2: Stacked bar chart showing count of users by gender and platform
elif visualization_option == "Count of Users by Gender and Platform":
    st.header('Count of Users by Gender and Platform')

    # Dynamic selection of variables
    x_variable = st.selectbox("Select X Variable:", df.columns)
    y_variable = 'count()'
    color_variable = st.selectbox("Select Color Variable:", df.columns)

    gender_platform_counts = df.groupby([x_variable, 'gender']).size().reset_index(name='count()')
    gender_platform_chart = alt.Chart(gender_platform_counts).mark_bar().encode(
        x=alt.X(f'{x_variable}:N', title=x_variable),
        y=alt.Y(y_variable, title='Count'),
        color=alt.Color(f'{color_variable}:N', legend=alt.Legend(title=color_variable))
    ).properties(width=600, height=400)
    st.altair_chart(gender_platform_chart)

    # Analysis for gender-platform count
    if analysis_option:
        st.subheader("Analysis for Count of Users by Gender and Platform")
        st.write("The chart above shows the distribution of users across different social media platforms "
                 "based on gender. From the analysis")

# Basic Analysis
st.header("Basic Analysis of the Dataset")
st.write("Let's explore some basic insights from the dataset.")

# Display basic statistics
st.subheader("Dataset Summary")
st.write(df.describe())

# Display first few rows of the dataset
st.subheader("First Few Rows of the Dataset")
st.write(df.head())
