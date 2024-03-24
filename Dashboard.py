import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate sample data for each chart type
# Line chart (Sales trend over time)

st.set_page_config(layout="wide")

dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
sales_data = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(100, 1000, len(dates))
})
line_data = sales_data.set_index('Date')

# Area chart (Cumulative sales over time)
area_data = pd.DataFrame({
    'Date': dates,
    'Cumulative Sales': sales_data['Sales'].cumsum()
}).set_index('Date')

# Bar chart (Sales by product category)
product_categories = ['Electronics', 'Clothing', 'Books', 'Home Decor', 'Toys']
bar_data = pd.DataFrame({
    'Product Category': product_categories,
    'Sales': np.random.randint(1000, 5000, len(product_categories))
})

# Scatter plot (Sales vs. Expenses)
scatter_data = pd.DataFrame({
    'Sales': np.random.randint(1000, 10000, 100),
    'Expenses': np.random.randint(100, 1000, 100)
})

# Pie chart (Sales distribution by product category)
pie_data = pd.Series([30, 20, 10, 25, 15], index=product_categories)

col1, col2 = st.columns(2, gap="medium")
col3, col4 = st.columns(2, gap="medium")
col5, col6 = st.columns(2, gap="medium")

# Display charts
# Line chart (Sales trend over time)
with col1:
    st.subheader('Sales Trend Over Time')
    st.line_chart(line_data)

with col2:
    st.subheader('Cumulative Sales Over Time')
    st.area_chart(area_data)

with col3:
    st.subheader('Sales by Product Category')
    st.bar_chart(bar_data.set_index('Product Category'))

# Scatter plot (Sales vs. Expenses)
with col4:
    st.subheader('Sales vs. Expenses')
    st.scatter_chart(scatter_data)

# Pie chart (Sales distribution by product category)
with col5:
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Sales Distribution by Product Category')
    st.pyplot(fig)
