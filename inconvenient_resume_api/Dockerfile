FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY inconvenient_resume_api/ ./inconvenient_resume_api
COPY alembic.ini ./
COPY alembic/ ./alembic
RUN touch README.md

RUN poetry install --no-dev

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "inconvenient_resume_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
