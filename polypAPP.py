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


# __________________ CREATING NAVBAR ____________________

st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #0B233C;">
        <span class="navbar-brand h1 mx-3 fs-3" style="margin-bottom: -5px; font-weight: 500px; margin-top: -5px;">Polyp AI</span>
    </nav>
""", unsafe_allow_html=True)

# __________________ CREATING MAIN HEADING ____________________

st.title("Polyp Detector")
title_styling="""
<style>
#polyp-detector {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  margin-top: -65px;
  color: #0B233C;
}
</style>
"""
st.markdown(title_styling, unsafe_allow_html=True)

buttonStyle = """
    <style>
        div.stButton > button:first-child {
            height: 3em;
            width: 100%; 
        }
    </style>
"""
st.markdown(buttonStyle, unsafe_allow_html=True)

# __________________ CREATING INPUTS ____________________
col1, col2 = st.columns(2)


with col1:
    patient_name = st.text_input("Enter your name")

with col2:
    gender = st.selectbox("Select your gender.", ('Male', 'Female', 'Binary'))

age = st.slider("How old are you?", 0, 130, 35)
image_file = st.file_uploader("Upload image for detection purposes")
if image_file is not None:
    size_mb = image_file.size/(1024**2)
    file_details = {
        "filename": image_file.name,
        "filetype": image_file.type,
        "filesize": "{:,.2f} MB".format(size_mb)
    }
    if file_details['filetype'] in ('image/png', 'imgage/jpg', 'image/jpeg'):
        st.success("Valid Format!", icon="✅")
        btnCol1, btnCol2 = st.columns(2)
        with btnCol1:
            st.button("Check Results", type="primary")
        with btnCol2:
            st.button("Generate Report", type="primary")
    else:
        st.error("Invalid Format! Only \'.jpeg\', \'.jpg\', \'.png\' format are accepted", icon="🚨")