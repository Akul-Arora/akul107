import csv
import pandas as pd
import plotly_express as px

df=pd.read_csv("data.csv")
fig = px.scatter(df, x="student_id", y="attempt",
	          size="Percentage",color="level",
                   size_max=60)
fig.show()