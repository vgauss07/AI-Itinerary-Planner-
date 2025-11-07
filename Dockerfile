# Parent Image
FROM python:3.10-slim

# Essential environment variable
ENV PYTHONDONTWRITEBYTECODE= \
    PYTHONBUFFERED=1

# work Directory inside the docker container
WORKDIR /app

# Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying ur all contents from local to app
COPY . .

# RUN setup.py
RUN pip install --no-cache-dir -e .

# Used PORTS
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]

