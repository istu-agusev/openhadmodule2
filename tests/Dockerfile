FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pytest paho-mqtt numpy

CMD ["pytest", "-q", "tests/integration"]