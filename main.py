import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from iso3166 import countries
from datetime import datetime, timedelta


pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('mission_launches.csv')

print(df_data.describe())

df_cleaned = df_data.dropna()
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned['Price'].fillna(0)
df_cleaned = df_cleaned.drop(df_cleaned.columns[0], axis=1)

print(df_cleaned.describe(include='all'))


