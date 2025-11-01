CMD="echo -e 'Watching connections with lsof\n'; sudo lsof -i | awk '{print \$10}' | sort | uniq -c"
watch -n 1 "$CMD"