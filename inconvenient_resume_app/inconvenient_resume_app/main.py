import requests
import streamlit as st

from inconvenient_resume_app.screens.login_screen import LOGIN_PAGE
from inconvenient_resume_app.screens.resume_screen import RESUME_PAGE
from inconvenient_resume_app.screens.user_screen import USER_PAGE


st.title("Inconvenient Resume App")

if st.session_state.get("access_token") is not None:
    pg = st.navigation([USER_PAGE, RESUME_PAGE])
else:
    pg = st.navigation([LOGIN_PAGE])

pg.run()
