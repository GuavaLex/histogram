import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
df = pd.read_csv('data.csv', parse_dates=[['Date', 'Time']])

# Drop rows with missing or NaN values in the 'Line to Neutral Voltage' column
df.dropna(subset=['Line to Neutral Voltage'], inplace=True)

# Calculate the frequency of values in the 'Line to Neutral Voltage' column
frequency_counts = df['Line to Neutral Voltage'].value_counts().sort_index()

# Define a rolling window size (e.g., 10 data points)
rolling_window = 10

# Calculate the rolling average of frequency counts
rolling_avg = frequency_counts.rolling(rolling_window).mean()

# Create a line chart for the rolling average
plt.figure(figsize=(10, 6))

# Use blue solid line with circle markers for the line chart
plt.plot(rolling_avg.index, rolling_avg.values, marker='o', linestyle='-', color='blue', markersize=6, label=f'Rolling Avg ({rolling_window}-point)')

plt.xlabel('Line to Neutral Voltage')
plt.ylabel('Frequency (Rolling Avg)')
plt.title(f'Line Chart of Line to Neutral Voltage Frequency (Rolling Avg - {rolling_window}-point)')
plt.grid(True)

# Add gridlines to the chart
plt.grid(True, linestyle='--', alpha=0.6)

# Customize the legend
plt.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()
