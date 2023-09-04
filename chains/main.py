import streamlit as st
import app

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Mexican","Italian","Arabic"))


if cuisine:
    response = generate_restaurant_name_and_iteams(cuisine)

    st.header(response["restaurant_name"])
    menu_iteams = response["menu_iteams"].split(",")

    st.write("**Menu Iteams**")

    for iteam in menu_iteams:
        st.write("-",iteam)

