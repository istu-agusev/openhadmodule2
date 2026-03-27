FROM python:3.11-slim

WORKDIR /app
COPY full_simulator.py .

RUN pip install paho-mqtt

CMD ["python3", "full_simulator.py"]