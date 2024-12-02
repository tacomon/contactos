FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential pkg-config && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y build-essential pkg-config && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

