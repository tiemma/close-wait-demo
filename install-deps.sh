#!/usr/bin/env bash
set -e

docker stop ubuntu || true
docker rm ubuntu || true

docker run -d -p 5555:5555 --name ubuntu ubuntu:24.04 sleep infinity

docker exec -it ubuntu bash -c "apt-get update && apt-get install -y socat python3 nano iproute2 lsof procps sudo cowsay tmux"

docker exec -it ubuntu bash -c 'echo PATH="$PATH:/usr/games" >> /root/.bashrc'

docker cp watch-connections.sh ubuntu:/root/watch-connections.sh
docker cp watch-lsof.sh ubuntu:/root/watch-lsof.sh
docker cp close-wait-server.py ubuntu:/root/close-wait-server.py
