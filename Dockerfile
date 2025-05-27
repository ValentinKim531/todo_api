# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y curl && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    playwright install --with-deps

COPY . .

RUN chmod +x entrypoint.sh

COPY .env .env

CMD ["sh", "entrypoint.sh"]
