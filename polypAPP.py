import streamlit as st
from streamlit_option_menu import option_menu

hide_st_style = """
    <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
#
# selected = option_menu(
#     menu_title=None,
#     options=["Polyp AI", "predict"],
#     default_index=0,
#     orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"},
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "#0f386d"},
#     }
# )
#
# # st.title('Polyp Detection App')
#
# container = st.container()
# container.write("So what Can i used instead of box?")

# [theme]
# base="light"
# primaryColor="#0f386d"

# __________________ CREATING NAVBAR ____________________

st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #0A1929;">
        <span class="navbar-brand h1 mx-2 fs-3" style="margin-bottom: -5px; font-weight: 500px;">Polyp<span class="navbar-brand h1 mx-2 fs-3">AI</span></span>
        
    </nav>
""", unsafe_allow_html=True)

container = st.container()

container.markdown("""
    <div class="container" style="background-color: #0A1929; border-radius: 10px; margin-top: -35px;">
    <h3 class="h1 text-center">Polyp Detector</h3>
    </div>
""", unsafe_allow_html=True)

# button = st.markdown("""
#     <button type="button" class="btn btn-primary">Primary</button>
# """, unsafe_allow_html=True)

