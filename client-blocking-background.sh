IP_ADDRESS=$(docker inspect ubuntu | jq -r '.[0].NetworkSettings.IPAddress')
for i in $(seq 1 1000); do
    socat -u tcp4:${IP_ADDRESS}:5555 - &
    echo $i
done
wait