for i in $(seq 1 1000); do  
    socat -T 1 -u tcp4:192.168.1.182:5555 - &
    echo $i
done
wait