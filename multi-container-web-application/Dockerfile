FROM python:3.10-slim
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN pip install flask psycopg2
CMD ["python" , "app.py"]
