import streamlit as st
import numpy as np
import pandas as pd

# Title of the dashboard
st.title('Sales Data Table')

# Generate sample data
np.random.seed(0)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
sales_data = pd.DataFrame({
    'Date': dates,
    'Product': np.random.choice(['Product A', 'Product B', 'Product C'], len(dates)),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Books'], len(dates)),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
})

# Display the data table with 20 records
st.table(sales_data.head(20))
