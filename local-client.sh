for i in $(seq 1 1000); do  
    socat -T 1 -u tcp4:127.0.0.1:5555 - &
    echo $i
done
wait