FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN pip3 install poetry
RUN poetry install