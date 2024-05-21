import pandas as pd
 
# Use double backslashes or a raw string
data_set = 'C:\\Users\\Aravi\\OneDrive\\Desktop\\employement analysis.csv'
# Or
# data_set = r'C:\\Users\\Aravi\\OneDrive\\Desktop\\employement analysis.csv'
 
# Read the dataset
data = pd.read_csv(data_set)
 
# Display the first few rows of the dataset
print(data.head())
 
# Basic statistics of the dataset
print(data.describe())
 
# Group the data by Region and compute the average unemployment rate
avg_unemployment_by_region = data.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
print(avg_unemployment_by_region)
 
# Group the data by Date and compute the average unemployment rate
avg_unemployment_by_date = data.groupby('Date')['Estimated Unemployment Rate (%)'].mean()
print(avg_unemployment_by_date)
 
# Plotting the average unemployment rate over time
import matplotlib.pyplot as plt
 
plt.plot(avg_unemployment_by_date.index, avg_unemployment_by_date.values)
plt.xlabel('Date')
plt.ylabel('Average Unemployment Rate (%)')
plt.title('Average Unemployment Rate Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
 