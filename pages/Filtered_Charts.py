import streamlit as st
import numpy as np
import pandas as pd

# Title of the dashboard
st.title('Sales Dashboard')

# Generate sample data
np.random.seed(0)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
sales_data = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(100, 1000, len(dates))
})

# Randomly generate additional columns (adjust as needed)
sales_data['Profit Margin'] = np.random.randint(10, 30, size=len(sales_data))  # Profit margin as %
sales_data['Units Sold'] = np.random.randint(10, 100, size=len(sales_data))  # Units sold

# Sidebar section
st.sidebar.header('Filters')

# Date range selector with initial values set to full dataset range
start_date = st.sidebar.date_input('Start Date', min(sales_data['Date']))
end_date = st.sidebar.date_input('End Date', max(sales_data['Date']))

# Convert start_date and end_date to pandas Timestamp
def convert_to_timestamp(date):
    return pd.Timestamp(date)

start_date = convert_to_timestamp(start_date)
end_date = convert_to_timestamp(end_date)

# Filter function to be called whenever the date selection changes
def filter_data(data, start_date, end_date):
    return data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Initially, use the entire dataset before user interaction
filtered_data = sales_data.copy()  # Make a copy to avoid modifying original data

# Line chart (call filter function before plotting)
st.subheader('Sales Trend Over Time')
st.line_chart(filter_data(filtered_data.copy(), start_date, end_date).set_index('Date'))

# Bar chart (call filter function before plotting)
st.subheader('Total Sales by Month')
monthly_sales = filter_data(filtered_data.copy(), start_date, end_date).resample('M', on='Date').sum()
st.bar_chart(monthly_sales)

# Summary statistics (call filter function before applying)
st.subheader('Summary Statistics')
st.write(filter_data(filtered_data.copy(), start_date, end_date).describe())

# Data table (call filter function before displaying)
st.subheader('Sales Data')
st.write(filter_data(filtered_data.copy(), start_date, end_date))
