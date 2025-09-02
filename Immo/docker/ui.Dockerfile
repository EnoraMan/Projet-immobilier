FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ui /app/ui

# API_URL points to the docker-compose service name
ENV API_URL=http://api:8000

EXPOSE 8501

CMD ["streamlit", "run", "ui/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
