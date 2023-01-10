import streamlit as st
from streamlit_option_menu import option_menu

hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        body {background-color: powderblue;}
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Polyp AI", "predict"],
    default_index=0,
    orientation="horizontal",

)

st.title('Polyp Detection App')