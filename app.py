import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data  
def load_data(csv):
    df = pd.read_csv(csv)
    return df

media = load_data("data/social_media.csv")

fig = plt.figure(figsize=(10, 6))
bar =sns.countplot(x="platform", hue="gender", data=media)
for i, container in enumerate(bar.containers):
    bar.bar_label(container, fontsize=10)
st.pyplot(fig)