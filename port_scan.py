import socket
import threading
from termcolor import cprint

target_host = input("Enter the target host (e.g., example.com or 192.168.1.1): ")
start_port = 1
end_port = 1024
open_ports = []

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        open_ports.append(port)
        cprint(f"Port {port} is OPEN", "green")
    sock.close()

def scan_ports_concurrently(host, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports

if __name__ == "__main__":
    print(f"Scanning ports on {target_host}...\n")
    open_ports = scan_ports_concurrently(target_host, start_port, end_port)

    if open_ports:
        print("\nOpen ports found:")
        for port in open_ports:
            print(f"Port {port} is OPEN")
    else:
        print("\nNo open ports found in the given range.")
