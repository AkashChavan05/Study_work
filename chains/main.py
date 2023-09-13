import streamlit as st
from app  import *

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Mexican","Italian","Arabic"))


if cuisine:
    response = generate_restaurant_name_and_iteams(cuisine)

    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")

    st.write("**Menu Iteams**")

    for i in menu_items:
        st.write("-",i)

