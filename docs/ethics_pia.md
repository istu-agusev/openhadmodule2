# Privacy Impact Assessment (PIA)

## 1. Опис системи
IoT система для керування теплицею з Edge AI та MQTT комунікацією.

## 2. Типи даних
- сенсорні дані (non-personal)
- системні логи
- device identifiers (potentially personal in enterprise use)

## 3. Ризики

### 3.1 Privacy risk
- MQTT clientID tracking
- logs in InfluxDB/Grafana

### 3.2 Security risk
- MQTT без TLS
- відсутність ACL

### 3.3 AI risk
- автономні рішення без explainability

## 4. Мітигація
- TLS для MQTT
- access control (ACL)
- data retention policies
- audit logging

## 5. GDPR relevance
- застосовується лише при наявності операторів/користувачів
- основні дані: технічні, не персональні

## 6. Висновок
Рівень приватнісного ризику: СЕРЕДНІЙ