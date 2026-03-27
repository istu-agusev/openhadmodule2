#!/bin/bash

DATE=$(date +%Y-%m-%d_%H-%M)
BACKUP_DIR=./backups/$DATE

mkdir -p $BACKUP_DIR

echo "Backing up OpenHAB..."
cp -r ./openhab $BACKUP_DIR/

echo "Backing up InfluxDB..."
docker exec influxdb151 influx backup /tmp/backup
docker cp influxdb151:/tmp/backup $BACKUP_DIR/influxdb

echo "Cleaning old backups..."
find ./backups -type d -mtime +7 -exec rm -rf {} \;

echo "Backup completed: $BACKUP_DIR"