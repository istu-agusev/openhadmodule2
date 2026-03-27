#!/bin/bash

BACKUP_PATH=$1

if [ -z "$BACKUP_PATH" ]; then
  echo "Usage: restore.sh <backup_folder>"
  exit 1
fi

echo "Restoring OpenHAB..."
cp -r $BACKUP_PATH/openhab/* ./openhab/

echo "Restoring InfluxDB..."
docker cp $BACKUP_PATH/influxdb influxdb151:/tmp/backup
docker exec influxdb151 influx restore /tmp/backup

echo "Restore complete!"