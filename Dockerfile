FROM python:3.11-alpine3.15

ENV PYTHONUNBUFFERED = 1
ENV PYTHONPATH=/app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt tmp/requirements.txt
RUN pip install no-cache-dir -r requirements.txt
COPY . .

RUN mkdir -p /app/logs

CMD ["python", "-m", "app.main.py"]
