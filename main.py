import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Read data from CSV
df = pd.read_csv('data.csv', parse_dates=[['Date', 'Time']])

# Drop rows with missing or NaN values in the 'Line to Neutral Voltage' column
df.dropna(subset=['Line to Neutral Voltage'], inplace=True)

# Calculate the bin edges automatically
num_bins = 5  # Adjust the number of bins as needed
bin_edges = np.histogram_bin_edges(df['Line to Neutral Voltage'], bins=num_bins)

# Use pd.cut to create bins for each day based on calculated bin edges
df['Voltage_Bin'] = pd.cut(df['Line to Neutral Voltage'], bins=bin_edges)

# Group by day and count the occurrences in each bin
grouped = df.groupby([df['Date_Time'].dt.day_name(), 'Voltage_Bin'])['Voltage_Bin'].count().unstack().fillna(0)

# Create the clustered bar graph
grouped.plot(kind='bar', stacked=False, figsize=(10, 6))  # Adjust the figure size as needed

# Format the chart
plt.xlabel('Voltage Bins')
plt.ylabel('Frequency')
plt.title('Line to Neutral Voltage Binned by Day')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability

# Display the plot
plt.tight_layout()
plt.show()
