#!/usr/bin/env python3
import socket
import os
import tempfile
import signal
import sys
from datetime import datetime
import resource
import time

# Set soft and hard limit for number of open file descriptors to 500
max_connections = 10
resource.setrlimit(resource.RLIMIT_NOFILE, (max_connections, max_connections))


def log(msg, *args, **kwargs):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{ts} - {msg}", *args, **kwargs, flush=True)

def handle_connection(conn, addr):
    pid = os.getpid()

    # Stop the process (simulating SIGSTOP)
    log(f"Child process PID: {pid} (will be stopped)")

    # File remains open, connection enters CLOSE_WAIT
    # os.kill(pid, signal.SIGSTOP)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)

    log("Server listening on port 5555")
    log("To simulate CLOSE_WAIT:")
    log("1. Connect with: nc localhost 5555")
    log("2. In another shell, find the child PID and `kill -STOP <child_pid>` to pause it")
    log("3. Observe the connection state with: ss -tanp | grep 5555")

    while True:
        conn, addr = server.accept()
        log(f"Connection from {addr}")

        pid = os.fork()
        if pid == 0:  # Child process
            server.close()
            handle_connection(conn, addr)
            sys.exit(0)
        else:  # Parent process
            # count processes from ps and count entries with 'close-wait' in the command
            procs = os.popen("ps -eo cmd").read().splitlines()
            close_wait_count = sum(1 for p in procs if 'close-wait' in p.lower())
            log(f"Processes with `close-wait` in name: {close_wait_count}")
            if close_wait_count > max_connections:
                log("Too many processes in CLOSE_WAIT state, sleeping...")
                time.sleep(10)

            conn.close()  # Parent should close its copy of the connection

if __name__ == "__main__":
    main()