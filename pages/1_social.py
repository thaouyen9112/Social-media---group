import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    file_path = "data/social_media.csv"
    data = pd.read_csv(file_path)
    return data

def main():
    st.title("Dynamic Numerical Analysis and Visualization")
    
    # Load data
    data = load_data()
    
    # Show histogram
    st.subheader("Histogram")
    column = st.selectbox("Select a column for the histogram", data.columns)
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], bins=20, kde=True)
    st.pyplot()

if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Ignore Matplotlib warning
    main()