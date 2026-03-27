# Data Pipeline

## 1. Data Collection
Sensors publish to MQTT topics:
- greenhouse/air_temp
- greenhouse/air_humidity
- greenhouse/soil_humidity
- greenhouse/co2
- greenhouse/ph

## 2. Transport Layer
- MQTT (Mosquitto)
- QoS: 0 (default)

## 3. Edge Processing
Edge AI computes:
- growth_index
- disease_risk
- anomaly detection

## 4. Output Topics
- edge/growth_index
- edge/disease_risk
- edge/alerts
- edge/action

## 5. Storage
- InfluxDB time-series DB
- retention: 30–90 days

## 6. Visualization
- Grafana dashboards

## Standards
- W3C WoT Thing Description
- MQTT 3.1.1
- JSON payloads