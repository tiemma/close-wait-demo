CMD="echo -e 'Watching connections with ss\n'; sudo ss | awk '{print \$2}' | sort | uniq -c"
echo "Watching connections (press Ctrl+C to stop)..."
watch -n 1 "$CMD"