import requests
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

from inconvenient_resume_app.config import settings

def get_resume() -> bytes:
    # TODO: create service class for API interactions
    response = requests.get(
        f"{settings.API_HOST}{settings.API_V1_STR}/user/resume",
        headers={"Authorization": f"Bearer {st.session_state.access_token}"},
    )
    response.raise_for_status()
    # TODO: pydantic models! :)
    return response.content

def resume_page():
    st.header("RESUME")
    resume = get_resume()
    pdf_viewer(resume)

RESUME_PAGE = st.Page(resume_page, title="Resume", icon="📄")
