FROM python:3.12-slim AS base

FROM base AS non-root
RUN useradd -ms /bin/bash app
USER app

FROM base AS requirements-builder

WORKDIR /build/

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --no-cache && \
    uv pip freeze | grep -v 'file:///build' > requirements.txt

FROM non-root AS app
WORKDIR /app
COPY --from=requirements-builder /build/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY alembic.ini .
COPY alembic ./alembic

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYTHONPATH=/app/src \
    PATH=/home/app/.local/bin:$PATH

CMD ["sh", "-c", "alembic upgrade head && python -m src.main_bot"]