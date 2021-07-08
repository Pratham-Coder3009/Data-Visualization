import pandas as pd
import plotly_express as px

df = pd.read_csv(r"C:\Users\prath\OneDrive\Desktop\Data-Visualization\Data-visualization-master\csv files\covidData.csv")
fig = px.scatter(df, x="date", y="cases", color="country")
fig.show()