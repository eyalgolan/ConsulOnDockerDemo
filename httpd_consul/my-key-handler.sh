#!/bin/bash

echo "New event: ${SERF_EVENT}. Data follows..."

while read line; do
{
    printf "${line}\n"
    printf "${line}\n" >> /var/www/html/eventlog.txt
}

curl http://172.17.4.161:8500/v1/kv/test/index.html?raw > /var/www/html/index.html
done
