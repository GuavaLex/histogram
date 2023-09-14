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

# Create a line chart for each bin on separate pages
for bin_label, bin_data in df.groupby('Voltage_Bin'):
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.plot(bin_data['Date_Time'].dt.day_name().value_counts().reindex(df['Date_Time'].dt.day_name().unique(),
                                                                        fill_value=0), marker='o', label=bin_label)

    # Format the chart
    plt.xlabel('Day of the Week')
    plt.ylabel('Frequency')
    plt.title(f'Frequency of Voltage Bin {bin_label}')
    plt.xticks(rotation=45)
    plt.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()
