# Close Wait Demo

A demonstration repository for network connection states and socket monitoring.

## Prerequisites

Before running this demo, you need to install the following dependencies:

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install socat iproute2 python3 lsof
```

### CentOS/RHEL/Fedora
```bash
# For CentOS/RHEL
sudo yum install socat iproute python3 lsof

# For Fedora
sudo dnf install socat iproute python3 lsof
```

### macOS
```bash
brew install socat iproute2mac python3 lsof
```

## Tools Overview

- **socat**: A command-line based utility that establishes two bidirectional byte streams and transfers data between them
- **ss**: A utility to investigate sockets (replacement for netstat)
- **lsof**: Lists open files and network connections
- **Python**: Used for the demo server implementation

## Scripts

### Server Scripts
- `close-wait-server.py`: Python server that demonstrates CLOSE_WAIT state scenarios

### Client Scripts  
- `local-client.sh`: Basic client connection script
- `client-no-block.sh`: Non-blocking client implementation
- `client-blocking-background.sh`: Background client with blocking behavior

### Monitoring Scripts
- `watch-connections.sh`: Monitor TCP connection states in real-time
- `watch-lsof.sh`: Monitor open files and connections using lsof
- `count-socat-forks.sh`: Count and monitor socat process forks

## Usage

### Basic Monitoring
Use `ss` to monitor socket states:
```bash
# Monitor TCP connections
ss -tuln

# Watch for CLOSE_WAIT states
ss -o state close-wait

# Monitor specific port
ss -tuln sport :5555
```

### Running the Demo
1. Start the Python server:
```bash
python3 close-wait-server.py
```

2. Run monitoring in another terminal:
```bash
./watch-connections.sh
```

3. Execute client scripts to generate different connection patterns:
```bash
./local-client.sh
./client-no-block.sh
./client-blocking-background.sh
```

### Advanced Monitoring
```bash
# Monitor socat processes
./count-socat-forks.sh

# Watch file descriptors and connections
./watch-lsof.sh
```

Use `socat` for network testing:
```bash
# Create a simple TCP server
socat TCP-LISTEN:5555,fork EXEC:/bin/cat

# Connect to a TCP server
socat - TCP:localhost:5555
```