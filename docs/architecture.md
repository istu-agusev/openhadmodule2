# Smart Greenhouse IoT System with Edge AI

## Опис
IoT система для автоматизованого керування теплицею з використанням Edge AI, MQTT, OpenHAB, InfluxDB та Grafana.

## Архітектура
Sensors → MQTT → Edge AI → MQTT → OpenHAB → Actuators  
            ↘ InfluxDB → Grafana

## Компоненти
- Mosquitto MQTT broker
- Edge AI (Python)
- OpenHAB automation
- Node-RED integration
- InfluxDB time-series DB
- Grafana dashboards
- WoT Thing Descriptions

## Запуск
```bash
docker-compose up --build
Web UI
OpenHAB: http://localhost:8080
Grafana: http://localhost:3000
InfluxDB: http://localhost:8086
Edge AI функції
Growth prediction
Disease risk detection
Anomaly detection
Auto irrigation & ventilation control
Документація
docs/architecture.md
docs/data_pipeline.md
docs/ethics_pia.md

# Архітектура системи

## Рівні системи

### 1. Sensor Layer
- temperature, humidity, CO2, pH, light sensors
- sensor_simulator (Docker service)

### 2. Communication Layer
- MQTT broker (Mosquitto)
- topic structure: greenhouse/#

### 3. Edge AI Layer
- HybridAI (growth model)
- DiseaseModel (risk prediction)
- anomaly detection (z-score)

### 4. Orchestration Layer
- OpenHAB rules engine
- actuator control logic

### 5. Data Layer
- InfluxDB (time-series storage)
- retention policies

### 6. Visualization Layer
- Grafana dashboards

## Потоки даних
Sensors → MQTT → Edge AI → MQTT → OpenHAB → Actuators  
            ↘ InfluxDB → Grafana

## Протоколи
- MQTT (telemetry + control)
- HTTP (UI access)
- InfluxDB line protocol
- WoT MQTT bindings