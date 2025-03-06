FROM python:3.12-alpine AS base

WORKDIR /backend

# README.md needed to hatchling build
COPY pyproject.toml requirements.lock README.md /backend/
RUN	pip install uv --no-cache
RUN	uv pip install --no-cache --system -r requirements.lock

COPY . .

CMD ["granian", "--interface", "asgi", "src/app.py", "--host", "0.0.0.0"]
# granian --interface asgi src/app.py --reload --access-log --host 0.0.0.0

