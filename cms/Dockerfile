FROM python:3.12-alpine AS base

WORKDIR /backend

# README.md needed to hatchling build
COPY pyproject.toml requirements.lock README.md /backend/
RUN	pip install uv --no-cache
RUN	uv pip install --no-cache --system -r requirements.lock

COPY . .

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--forwarded-allow-ips='*'", "--proxy-headers"]
# uvicorn src.app:app --host 0.0.0.0 --forwarded-allow-ips='*' --proxy-headers  
# uvicorn src.app:app --reload
