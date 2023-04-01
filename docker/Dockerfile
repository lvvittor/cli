FROM python:3.10-slim-buster 

ENV PATH="/root/.local/bin:$PATH"

RUN pip install pipx
RUN pipx install poetry
ENV PATH="/root/.local/pipx/venvs/poetry/bin/:$PATH"

COPY pyproject.toml /che-sandbox/pyproject.toml
COPY poetry.lock /che-sandbox/poetry.lock

RUN poetry config virtualenvs.create false

WORKDIR /che-sandbox

RUN --mount=type=cache,target=/root/.cache/pip \
    poetry install --with dev --no-root

COPY . /che-sandbox

RUN --mount=type=cache,target=/root/.cache/pip \
    poetry install --with dev --no-interaction