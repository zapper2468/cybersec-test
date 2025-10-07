import socket

def scan_ports(target, ports=[21,22,23,25,53,80,110,443,8080]):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            banner = s.recv(1024).decode().strip() if port in [21,22,80,443] else ""
            print(f"[+] Port {port} open{' | Banner: ' + banner if banner else ''}")
            s.close()
        except:
            pass

if __name__ == "__main__":
    target = input("Enter IP or hostname: ")
    scan_ports(target)
