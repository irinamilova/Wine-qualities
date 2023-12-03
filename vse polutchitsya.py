import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats as st
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import streamlit as str

df = pd.read_csv(r"C:\Users\irina\HSE PROJECT WINE\hse_project_wine-1\wines_SPA.csv")
df["year"] = df["year"].replace("N.V.", np.NaN)
df = df.dropna()

str.title("Spanish Wine Quality Dataset")

types = str.multiselect("Choose a wine type", df["type"].unique())
year = str.multiselect("Choose a year", df["year"].unique())
new_df = df[(df["type"].isin(types)) & (df["year"].isin(year))]
str.write(new_df)

str.subheader("Statistics")
col1, col2, col3, col4 = str.columns(4)
with col1:
   _value = df.wine.unique().size
   str.metric(label="Wines", value=_value)
with col2:
   _value = df.winery.unique().size
   str.metric(label="Wineries", value=_value)
with col3:
   _value = df.region.unique().size
   str.metric(label="Regions", value=_value)
with col4:
   _value = df.type.unique().size
   str.metric(label="Types", value=_value)

fig1 = px.bar(df, 
             x="type", y="wine", color_discrete_sequence=["Agsunset"],
             color="rating", color_continuous_scale="RdBu")


top = df["type"].value_counts().head(5)
dfrr1 = df[df.type == "Rioja Red"]
dfrr2 = df[df.type == "Ribera Del Duero Red"]
dfrr3 = df[df.type == "Red"]
dfrr4 = df[df.type == "Priorat Red"]
dfrr5 = df[df.type == "Tempranillo"]
framess = [dfrr1, dfrr2, dfrr3, dfrr4, dfrr5]
dfrrr = pd.concat(framess)
fig2 = px.sunburst(dfrrr, path=['type', 'winery'], values='year',
                  color='rating',
                  color_continuous_scale='RdBu')

fig3 = px.scatter(df, x="type", y="body", color="acidity", color_continuous_scale="RdBu")


fig4 = px.scatter_3d(df, x='year', y='body', z='rating',
              color='price', color_continuous_scale="RdBu")


table = str.sidebar.button(label="Rating of Spanish wines")
line = str.sidebar.button("Wine types")
scatter = str.sidebar.button("Wine types body and acidity")
td = str.sidebar.button("Correlations between four parametres")

if table:
    str.subheader("Rating of Spanish wines")
    str.plotly_chart(fig1)

if line :
    str.subheader("Wine types")
    str.plotly_chart(fig2)

if scatter:
    str.subheader("Wine types body and acidity")
    str.plotly_chart(fig3)

if td:
    str.subheader("Correlations between four parametres")
    str.plotly_chart(fig4)
