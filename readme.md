**Project Title:** E-commerce Customer Churn Analysis

**Project Description:**

In this data analysis project, we aim to understand and analyze customer churn in an e-commerce business. We will utilize the pandas library for data loading and cleaning, and employ data analysis and visualization techniques with pandas, plotly and streamlit to gain insights into the factors contributing to customer churn.

**Data Loading:**

The first step in our analysis is data loading, which is achieved using the pandas library. We will load the dataset and prepare it for analysis.

**Data Cleaning:**

1. **Handling Missing Values:** We will begin by checking for missing values in the dataset. Our investigation reveals that the Returns column has missing values. To address this, we employ a statistical imputation technique by replacing the missing values with the mode (most frequent) value of the Returns column. This ensures that we have a complete dataset to work with.

2. **Duplicate Rows and Columns:** We check for both duplicate rows and columns in the dataset. It is discovered that the Age column contains duplicate data, which serves no analytical purpose. Therefore, we remove the duplicated Age column, streamlining the dataset.

3. **Outlier Detection:** Outliers can significantly affect our analysis. To ensure robust results, we apply the Box plot technique to check for outliers in the Customer Age and Total Purchase Amount columns. Our examination concludes that there are no outliers in these two columns.

**Churn Analysis Dashboard:**

With clean and well-prepared data, we move on to the core of our project - data analysis. We focus our analysis on the data related to customers who have left, as understanding the reasons behind customer churn is crucial.

We will utilize pandas for data loading and exploration, and plotly for interactive data visualization. 
Streamlit is used here for Dashobard Web app development. Through these tools, we will create informative visualizations and conduct in-depth analysis to uncover patterns, trends, and potential factors contributing to customer churn.

By the end of this project, we aim to provide actionable insights and recommendations to help the e-commerce business reduce customer churn and improve overall customer satisfaction. Our analysis will be based on sound data cleaning and visualization techniques, enabling data-driven decisions for the organization.

Click on below link to view the application deployed in render platform using free account. so, it would take take sometime to load. 

https://ecom-dashboard-qt9b.onrender.com/

File Information:
ECOM_Churn_Case_Study.ipynb   -> In this file, data cleaning and exported cleaned using pandas.
ecom_dash_app.py  -> Stored clean data is loaded and dashboard app developed using streamlit.
ecom_data.csv -> Raw Data
ecom_clean_data.csv -> Cleaned Data