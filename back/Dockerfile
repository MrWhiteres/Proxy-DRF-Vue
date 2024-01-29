FROM python:3.11.7  as python-base
LABEL authors="MrWhite"

RUN pip install poetry

WORKDIR /back
COPY poetry.lock pyproject.toml ./
ENV PYTHONUNBUFFERED=1
RUN poetry install --no-dev

COPY . /back


CMD ["poetry", "run", "python", "manage.py", "makemigrations"]
CMD ["poetry", "run", "python", "manage.py", "migrate"]
CMD ["poetry", "run", "python", "manage.py", "collectstatic", "--no-input"]
CMD ["poetry", "run", "uvicorn", "project.network.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]