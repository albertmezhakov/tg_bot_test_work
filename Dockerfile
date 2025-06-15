FROM python:3.12-slim AS base

FROM base AS non-root
RUN useradd -ms /bin/bash app
USER app

FROM base AS requirements-builder

WORKDIR /build/

RUN pip --no-cache-dir install poetry

COPY pyproject.toml poetry.lock /build/

RUN poetry self add poetry-plugin-export

RUN poetry export --without-hashes -f requirements.txt -o requirements.txt

FROM non-root AS app
WORKDIR /app
COPY --from=requirements-builder /build/requirements.txt /app/requirements.txt

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY src ./src
ENV PYTHONPATH="/app/src:${PYTHONPATH}"
COPY alembic.ini .
COPY alembic ./alembic

# run app
WORKDIR /app
CMD ["sh", "-c", "python -m alembic upgrade head && python src/main_bot.py"]