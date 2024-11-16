import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as ggi

# App interface
st.title('AI Expense Tracker')
st.info('This AI model will help u your finance')
user_name=st.text_input('enter your name')
st.write()
monthly_income=st.number_input('your monthly income')
st.write()
savings=st.number_input('monthly savings')
st.write()
product_category = st.selectbox(
    "Select your Category",
    options=["Food", "Travel", "Entertainment", "Bills", "Others"]
)
product_amount = st.number_input("Enter the Amount", min_value=0, step=1)

if "expense" not in st.session_state:
    st.session_state["expense"] = pd.DataFrame(columns=["Name", "monthly income", "product category", "product amount","savings"])
    
if st.button("Add Expenditure"):
    if user_name and product_amount>0:
        entry=pd.DataFrame([{'Name':user_name,'monthly income':monthly_income,'product category':product_category,'product amount':product_amount,'savings':savings}])
        st.session_state["expense"]=pd.concat([st.session_state["expense"], entry])
        st.success("Expenditure added successfully")
    else:
        st.error("please fill entry correctly")
if not st.session_state["expense"].empty:
    st.header("your expenditure")
    st.dataframe(st.session_state["expense"])
total_amount_spend=st.session_state["expense"]["product amount"].sum()
st.write(f"Total expenditure is {total_amount_spend}")

# Graph
fig,ax = plt.subplots(figsize=(3,3))
ax.bar(['monthly income', 'Total Expenditure'], [monthly_income, total_amount_spend], color=['green', 'red'])
ax.set_ylabel('Amount')
ax.set_title('Monthly Income vs Total Expenditure')
st.pyplot(fig)

# model using gemini api

