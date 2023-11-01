# importing neccessary libraries
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

#setting page config
st.set_page_config(page_title='E-COM Churn Analysis',page_icon=':bar_chart:',layout='wide')
st.title(':white[E-Commerce Customer Churn Analysis Dashboard]')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

#Loading Data
@st.cache_data
def get_data():
    return pd.read_csv('ecom_clean_data.csv')

df=get_data()

#Addding toggle to view structure of data
data_toggle=st.toggle(label='View Data',value=False)
if data_toggle:
    st.dataframe(df.head())
else:
    pass

#Creating sidebar filters
st.sidebar.header("Filter the Customers by below facets" )
gen=list(df['Gender'].unique())
age_grp=list(df['Age_Group'].unique())
gender=st.sidebar.multiselect('Filter Customer by Gender',gen,placeholder='Select Gender',default=gen)
age_group=st.sidebar.multiselect('Filter Customer by Age Group',age_grp, placeholder='Select Age Group',default=age_grp)

st.markdown('---')


#Creating metrics for churn data
df2=df.query("Gender == @gender and Age_Group == @age_group")
# Check if the dataframe is empty:
if df2.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.

col1, col2,col3 = st.columns(3)
with col1:
     st.subheader(':green[Total Customers]:busts_in_silhouette:')
     st.subheader(df2['Customer ID'].nunique())
with col2:
    st.subheader(':blue[Customers Left]:man-running:')
    st.subheader( df2[df2['Churn']==1]['Customer ID'].nunique())
percentage=((df2[df2['Churn']==1]['Customer ID'].nunique())/df['Customer ID'].nunique())*100
percentage=round(percentage,2)
with col3:
    st.subheader(':red[Customer Churn Rate]:chart_with_downwards_trend:')
    st.subheader(str(percentage)+"%")

st.markdown('---')

col11, col12,col13 = st.columns(3)
with col11:
      st.subheader(':green[Number of Purchases By Churn Customers]')
      st.subheader(df2[df2['Churn']==1]['Purchase Date'].count())
with col12:
     st.subheader(':blue[Number Of Returns By Churn Customers]')
     st.subheader(df2[df2['Churn']==1]['Returns'].sum())
with col13:
    st.subheader(':red[Percentage of Returns]')
    percentage_r=((df2[df2['Churn']==1]['Returns'].sum())/(df2[df2['Churn']==1]['Purchase Date'].count()))*100
    percentage_r=percentage_r.round(2)
    st.subheader(str(percentage_r)+"%")
st.markdown('---')

#creating plots
c1,c2=st.columns(2)
with c1:
     product_count=df2[df2['Churn']==1]['Product Category'].value_counts()
     product_count=pd.DataFrame({'Category':product_count.index,'Number of Purchases':product_count.values})
     fig2 = px.bar(product_count, x='Category', y='Number of Purchases',title='Purchase Made By Churn Customers in Different Product Category',color='Category',orientation='v')
     st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
with c2:
     st.dataframe(product_count,use_container_width=True,hide_index=True)


c11,c12=st.columns(2)
with c11:
    payment_type=df2[df2['Churn']==1]['Payment Method'].value_counts()
    payment_type=pd.DataFrame({'Payment Type':payment_type.index,'Number of Purchases':payment_type.values})
    fig1=px.pie(data_frame=payment_type,values='Number of Purchases',names='Payment Type',title='Payment Method Preferred by Churn Customers',color='Payment Type')
    st.plotly_chart(fig1,theme="streamlit", use_container_width=True)
with c12:
     st.dataframe(payment_type,use_container_width=True,hide_index=True) 

c21,c22=st.columns(2)
with c21:
    returns=df2[df2['Churn']==1].groupby('Product Category')['Returns'].sum()
    returns=pd.DataFrame(dict(Product_Category=returns.index,Number_of_Returns=returns.values))
    fig4 = px.bar(returns,x='Number_of_Returns', y='Product_Category',title='Products Retrurned By Churn Customers',color='Product_Category',orientation='h')
    st.plotly_chart(fig4, theme="streamlit", use_container_width=True)
with c22:
    returns=df2[df2['Churn']==1].groupby('Product Category')['Returns'].sum()
    st.dataframe(returns,use_container_width=True)  

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
