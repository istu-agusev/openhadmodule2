FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install paho-mqtt numpy

CMD ["python", "edge_runtime.py"]