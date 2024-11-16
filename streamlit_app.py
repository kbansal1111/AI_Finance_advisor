import streamlit as st
import pandas as pd
st.title('AI Expense Tracker')
st.info('This AI model will help u your finance')
user_name=st.text_input('enter your name')
st.write()
monthly_income=st.number_input('your monthly income')
st.write()
product_category = st.selectbox(
    "Select your Category",
    options=["Food", "Travel", "Entertainment", "Bills", "Others"]
)
product_amount = st.number_input("Enter the Amount", min_value=0.0, step=0.1)

if st.button("Add Expenditure"):
    if user_name and product_amount>0:
        entry={'Name':user_name,'monthly income':monthly_income,'product category':product_category,'product amount':product_amount}
        st.session_state["expense"]=st.session_state["expense"].append(entry)
        st.success("Expenditure added successfully")
    else:
        st.error("please fill entry correctly")
if not st.session_state["expense"].empty:
    st.header("your expenditure")
    st.dataframe(st.session_state["expense"])
