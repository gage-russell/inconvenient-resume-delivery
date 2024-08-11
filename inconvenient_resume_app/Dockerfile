FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY inconvenient_resume_app/ ./inconvenient_resume_app
RUN touch README.md

RUN poetry install --no-dev

EXPOSE 8080

CMD ["poetry", "run", "streamlit", "run", "inconvenient_resume_app/main.py", "--server.port=8080", "--server.address=0.0.0.0"]
