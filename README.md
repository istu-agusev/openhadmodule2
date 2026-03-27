1. Архітектура системи

openhadmodule2/
│
├── edge_ai/
│ ├── disease_detection.py
│ ├── edge_runtime.py
│ ├── hybrid_ai.py
│ ├── Dockerfile
│
├── sensor_simulator/
│ ├── full_simulator.py
│ ├── Dockerfile
│
├── openhab/
│ ├── addons/
│ ├── conf/
│ │ ├── automation/
│ │ ├── html/
│ │ ├── icons/
│ │ ├── items/
│ │ │ ├── greenhouse.items
│ │ │ ├── readme.txt
│ │ ├── persistence/
│ │ │ ├── influxdb.persist
│ │ │ ├── readme.txt
│ │ ├── rules/
│ │ │ ├── alerts.rules
│ │ │ ├── climate.rules
│ │ │ ├── edge_ai.rules
│ │ │ ├── irrigation.rules
│ │ │ ├── light.rules
│ │ ├── scripts/
│ │ ├── services/
│ │ ├── sitemaps/
│ │ │ ├── greenhouse.sitemap
│ │ │ ├── readme.txt
│ │ ├── sounds/
│ │ ├── tags/
│ │ ├── things/
│ │ │ ├── mqtt.things
│ │ │ ├── readme.txt
│ │ ├── transform/
│ │ ├── yaml/
│ ├── userdata/
│
├── grafana/
│ ├── dashboards/
│ │ ├── openhab-dashboard.json
│ ├── provisioning/
│
├── mosquitto/
│
├── node-red/
│ ├── flows/
│ │ ├── wot_bridge.json
│
├── wot/
│ ├── edge-ai.td.json
│ ├── greenhouse-actuators.td.json
│ ├── greenhouse-sensors.td.json
│
├── tests/
│ ├── integration/
│ │ ├── test_full_pipeline.py
│ │ ├── test_mqtt_pipeline.py
│ │ ├── test_stress_pipeline.py
│ ├── unit/
│ │ ├── test_disease_model.py
│ │ ├── test_hybrid_ai.py
│ ├── test_edge_logic.py
│ ├── Dockerfile
│ ├── pytest.ini
│
├── scripts/
│
├── docs/
│ ├── architecture.md
│ ├── data_pipeline.md
│ ├── ethics_pia.md
│ ├── diagrams/
│ │ ├── architecture.mmd
│ │ ├── dataflow.mmd
│
├── backups/
│
├── docker-compose.yml
├── docker-compose.override.yml
├── Makefile
├── README.md
├── .env.example
├── .env
├── .gitignore

Система побудована як багаторівнева IoT-архітектура:

Sensor Layer (simulator / реальні сенсори)
MQTT Broker (Mosquitto)
Edge AI Layer (Python inference engine)
IoT Orchestration (OpenHAB)
Data Storage (InfluxDB)
Visualization (Grafana)
Integration Layer (Node-RED + WoT TD)
Основні потоки:
Sensors → MQTT (greenhouse/#)
Edge AI → MQTT (edge/*)
OpenHAB → Actuators (greenhouse/cmd/*)
Data → InfluxDB → Grafana
2. Data Pipeline (опис)
Етапи:
Збір даних (sensor_simulator / IoT devices)
Передача через MQTT (QoS 0)
Обробка на Edge AI:
growth index
disease risk
anomaly detection
Публікація результатів:
edge/growth_index
edge/disease_risk
edge/action
Збереження в InfluxDB
Візуалізація в Grafana
3. Edge AI компонент

Модулі:

HybridAI (growth model)
DiseaseModel (logistic risk model)
anomaly detection (z-score based)

Функції:

автономне управління теплицею
генерація alerts
fallback rule-based control через OpenHAB
4. CI/CD Pipeline
Docker Compose deployment
healthchecks для сервісів
auto-restart політики
future extension:
GitHub Actions (tests + build + deploy)
blue-green deployment (optional)
5. Етично-правовий аналіз
GDPR: потенційні device identifiers
Risk: MQTT без TLS
AI risk: autonomous actuation
Mitigation:
ACL MQTT
encryption (TLS)
logging & audit trail
6. Висновки

Система є повноцінною Edge AI IoT платформою з:

реальним data pipeline
автономною аналітикою
інтеграцією WoT стандарту
розширюваною DevOps архітектурою
