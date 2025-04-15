"""
Simple Network Scanner Example (for educational purposes)
"""
import socket

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((host, port)) == 0:
                    open_ports.append(port)
        except Exception:
            continue
    return open_ports

if __name__ == "__main__":
    host = "127.0.0.1"
    ports = range(75, 85)
    print(f"Scanning {host} on ports {list(ports)}...")
    print("Open ports:", scan_ports(host, ports))
