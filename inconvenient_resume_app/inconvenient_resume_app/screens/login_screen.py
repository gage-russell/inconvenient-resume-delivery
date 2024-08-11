import requests
import streamlit as st

from inconvenient_resume_app.config import settings


def login(email: str, password: str) -> str:
    # TODO: create service class for API interactions
    response = requests.post(
        f"{settings.API_HOST}{settings.API_V1_STR}/login/access-token",
        data={"username": email, "password": password},
    )
    response.raise_for_status()
    return response.json()["access_token"]

def login_page():
    st.title("Inconvenient Resume App")

    # check session state for JWT token and user
    if st.session_state.get("access_token") is None:
        st.write("Please log in to access this app.")
        email = st.text_input("Email (hint: localdev@example.com)")
        password = st.text_input("Password (hint: localdev)", type="password")
        if st.button("Log in"):
            try:
                access_token = login(email, password)
                st.session_state.access_token = access_token
                st.write("Login successful!")
                st.rerun()
            except requests.HTTPError as e:
                st.write(f"Login failed: {e}")
    else:
        st.write("You are logged in!")
        st.write("Here's your access token:")
        st.write(st.session_state.get("access_token") )

LOGIN_PAGE = st.Page(login_page)
