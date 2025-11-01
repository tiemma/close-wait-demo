#!/usr/bin/env python3
import socket
import os
import tempfile
import signal
import sys

def handle_connection(conn, addr):
    pid = os.getpid()

    # Stop the process (simulating SIGSTOP)
    print(f"Child process PID: {pid} (will be stopped)")


    # File remains open, connection enters CLOSE_WAIT
    os.kill(pid, signal.SIGSTOP)
    
    # Keep the file open indefinitely - process will be killed externally
    # File descriptor will only be closed when process dies
    while True:
        pass  # Infinite loop to keep process alive with open file

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    
    print("Server listening on port 5555")
    print("To simulate CLOSE_WAIT:")
    print("1. Connect with: nc localhost 5555")
    print("2. Check socket state: ss -tuln | grep 5555")
    print("3. Send SIGSTOP to pause: kill -STOP <child_pid>")

    open_files = []  # Keep references to prevent garbage collection

    while True:
        conn, addr = server.accept()
        print(f"Connection from {addr}")
        
        pid = os.fork()
        if pid == 0:  # Child process
            server.close()
            handle_connection(conn, addr)
            sys.exit(0)
        else:  # Parent process
            try:
                # Create and open a random file in /tmp
                temp_file = tempfile.NamedTemporaryFile(dir='/tmp', delete=False, prefix='close_wait_')
                open_files.append(temp_file)  # Keep reference to maintain open file
                print(f"Opened file: {temp_file.name} from parent process PID: {os.getpid()}")
            except Exception as e:
                print(f"Error opening file: {e}")

            conn.close()  # Parent should close its copy of the connection

if __name__ == "__main__":
    main()