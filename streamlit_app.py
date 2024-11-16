import streamlit as st

st.title('AI Expense Tracker')
st.info('This AI model will help u your finance')
user_name=st.text_input('enter your name')
st.write()
monthly_income=st.number_input('your monthly income')
st.write()
product_category = st.selectbox(
    "Select the Category",
    options=["Food", "Travel", "Entertainment", "Bills", "Others"]
)
product_amount = st.number_input("Enter the Amount", min_value=0.0, step=0.01)
if st.button("Add Expenditure"):
    if amount > 0:
        st.success(f"amount spend ₹ {product_amount} on {product_category}")
    else:
        st.error("Please enter a valid amount.")
