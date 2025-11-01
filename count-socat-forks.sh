CMD="echo -e 'Watching connections with python\n'; sudo ps aux | grep close-wait-server | wc -l"
watch -n 1 "$CMD"