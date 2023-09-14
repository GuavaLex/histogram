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

# Create a histogram of the 'Line to Neutral Voltage' column using the same bin edges
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(df['Line to Neutral Voltage'], bins=bin_edges, edgecolor='k', alpha=0.7)

# Create labels for each bin indicating the bin width
bin_widths = [f'{bins[i]:.2f}-{bins[i+1]:.2f}' for i in range(len(bins) - 1)]

# Create a legend with bin width information
legend_labels = [f'Bin {i+1}: {bin_width}' for i, bin_width in enumerate(bin_widths)]
plt.legend(legend_labels)

# Format the chart
plt.xlabel('Line to Neutral Voltage')
plt.ylabel('Frequency')
plt.title('Histogram of Line to Neutral Voltage with Specified Bin Width')
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
