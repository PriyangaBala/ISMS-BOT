FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements (if you have one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=isms_qms_server.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Professional ISMS & QMS Assistant
CMD ["flask", "run", "--host=0.0.0.0"]