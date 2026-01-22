# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY app.py .

# Expose the port that Flask uses
EXPOSE 5000

# Default command
CMD ["python", "app.py"]

# docker tag my-python-k8s-app:latest faruk67/my-python-k8s-app:latest