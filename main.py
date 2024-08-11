import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from iso3166 import countries
from datetime import datetime, timedelta
import matplotlib.colors as mcolors

pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('mission_launches.csv')

df_cleaned = df_data.dropna()
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned['Price'].fillna(0)
df_cleaned = df_cleaned.drop(df_cleaned.columns[0], axis=1)

launches_by_org = df_cleaned.groupby('Organisation').size().reset_index(name='Launches')
launches_by_org = launches_by_org.sort_values('Launches', ascending=True)

plt.figure(figsize=(12, 6))

cmap = mcolors.LinearSegmentedColormap.from_list("", ["#ADD8E6", "#3498db"])
colors = [cmap(i / max(launches_by_org['Launches'])) for i in launches_by_org['Launches']]

plt.barh(range(len(launches_by_org)), launches_by_org['Launches'], color=colors)

plt.title('Number of Space Mission Launches by Organisation')
plt.xlabel('Number of Launches')
plt.ylabel('Organisation')
plt.xticks(range(0, max(launches_by_org['Launches']) + 10, 10))  
plt.yticks(range(len(launches_by_org)), launches_by_org['Organisation']) 
plt.grid(axis='x', linestyle='--', alpha=0.5)  
plt.tight_layout()  
plt.legend(['Launches'], loc='lower right', bbox_to_anchor=(1, 0), frameon=False)

plt.show()

