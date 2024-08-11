import requests
import streamlit as st

from inconvenient_resume_app.config import settings

def get_user() -> dict[str, str]:
    # TODO: create service class for API interactions
    response = requests.get(
        f"{settings.API_HOST}{settings.API_V1_STR}/user/me",
        headers={"Authorization": f"Bearer {st.session_state.access_token}"},
    )
    response.raise_for_status()
    # TODO: pydantic models! :)
    return response.json()

def logout() -> None:
    # TODO: actually log out in API
    st.session_state.clear()
    st.rerun()

def user_page():
    st.header("USER")
    user = get_user()
    st.write(f"Welcome, {user['email']}!")
    st.write(f"Your user ID is: {user['id']}")
    st.write(f"I shouldn't tell you this, but your JWT is: {st.session_state.get('access_token')}")
    if st.button("Log out"):
        logout()

USER_PAGE = st.Page(user_page, title="User", icon="👤")
