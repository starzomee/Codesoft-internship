# -*- coding: utf-8 -*-
"""shayan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18GOnq4zXIAAfl-KeRNL5c2JknNakTC0P
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

full_data = pd.read_csv('/content/IMDb Movies India.csv', encoding='ISO-8859-1')

full_data

full_data.head()

full_data.tail()

full_data.info()

sns.heatmap(full_data.isnull() , cmap ='tab20c_r' , yticklabels = False , cbar = False)
plt.title("HEATMAP")
plt.show()

full_data.dropna(subset=['Actor 1','Actor 2','Actor 3', 'Director'], inplace=True)

full_data['Rating'].fillna('0' , inplace= True)

full_data.dropna(subset = ['Duration' , 'Genre' , 'Votes'], inplace= True)

sns.heatmap(full_data.isnull() , cmap ='tab20c_r' , yticklabels = False , cbar = False)
plt.title("HEATMAP")
plt.show()

full_data.shape

full_data.drop_duplicates( inplace=True)

full_data.shape

sns.countplot(x = 'Rating' , data= full_data)
fig = plt.gcf()
fig.set_size_inches(30, 30)
#figure=full_data(figsize(10, 10))
plt.title("countplot IMDb Movies dataset")
plt.show()

full_data['Rating'].value_counts().plot.pie( shadow= True , figsize=(8,5))
plt.show()

data = full_data['Rating']

# Create the histogram
plt.hist(data, bins=10)  # You can adjust the number of bins as needed

# Add labels and a title to the plot
plt.xlabel('X-Axis ')
plt.ylabel('Frequency')
plt.title('Histogram of IMDb Movies')

# Show the histogram
plt.show()

sns.scatterplot(full_data)

