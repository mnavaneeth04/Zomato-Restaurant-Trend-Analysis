import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv(r"C:\Users\navan\Documents\Zomato Data Analysis\Zomato-data- (1).csv")
print(dataframe.head())
dataframe['rate'] = dataframe['rate'].str.replace('/5', '').astype(float)
print(dataframe.head()) 
dataframe.info() #Check for NULL values

custom_colors = ['#FF5733', '#33FF57', '#3357FF', '#FAD02E', '#8E44AD']
sns.countplot(x=dataframe['listed_in(type)'], palette=custom_colors)
plt.xlabel("Type of Restaurant") 
plt.show() #Popular Restaurant Types

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result.index, result['votes'], c='red', marker='o', linestyle='-')
plt.xlabel('Type of Restaurant', c='blue',size = 20)
plt.ylabel('Votes', c='blue', size=20)
plt.show() #Votes for each type of restaurant

max_votes = dataframe['votes'].max()
max_votes_restaurant = dataframe.loc[dataframe['votes'] == max_votes,'name']
print(f"Restaurant with maximum votes:")
print(max_votes_restaurant) # Restaurant with maximum votes

sns.countplot(x=dataframe['online_order'])
plt.show()

plt.hist(dataframe['rate'],bins=5, color='blue', edgecolor='black')
plt.title('Distribution of Ratings')
plt.show() #Distribution of Restaurant Ratings

couple = dataframe['approx_cost(for two people)']
sns.countplot(x=couple)
plt.show() #Approximate cost for two people(couples)

plt.figure(figsize=(6, 6))
sns.boxplot(x='online_order', y='rate', data=dataframe, palette=custom_colors)
plt.show() #Comparison of online order vs offline orders

pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()# Heatmap of Online Order vs Listed In Type
