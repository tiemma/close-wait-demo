for i in $(seq 1 2000); do
    socat -u tcp4:192.168.1.182:5555 - &
    echo $i
done
wait