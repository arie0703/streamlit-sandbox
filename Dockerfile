FROM python:3.8

COPY requirements.txt .
COPY ./app/ ./app/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /app