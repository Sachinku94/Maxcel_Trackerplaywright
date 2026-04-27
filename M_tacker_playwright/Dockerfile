FROM mcr.microsoft.com/playwright/python:v1.48.2-focal

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN playwright install

COPY . .

CMD ["python", "-m", "pytest", "--alluredir=allure-results", "-v"]