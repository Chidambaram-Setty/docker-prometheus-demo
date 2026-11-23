FROM python:3.11-slim

WORKDIR /app

# Install the Prometheus Python client
RUN pip install --no-cache-dir prometheus-client

COPY app.py .

# Expose both the web app port and the metrics port
EXPOSE 5000 8000

CMD ["python", "app.py"]