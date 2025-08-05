# Dockerfile

FROM python:3.11-slim

# Install pip dependencies if needed
# (you can remove this if you don't use any external packages)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || true

WORKDIR /app
COPY . /app

# Default command
CMD ["python", "app.py"]
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . /app

CMD ["python", "app.py"]
