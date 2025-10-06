import re

def analyze_log(file_path):
    with open(file_path, 'r') as f:
        logs = f.readlines()

    failed_logins = [line for line in logs if "Failed password" in line]
    ssh_attempts = [line for line in logs if "sshd" in line]

    print(f"Total log lines: {len(logs)}")
    print(f"Failed logins: {len(failed_logins)}")
    print(f"SSH connection attempts: {len(ssh_attempts)}")

    ip_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', ' '.join(failed_logins))
    print(f"Unique IPs with failed logins: {len(set(ip_addresses))}")
    print("Top 5 IPs:")
    for ip in list(set(ip_addresses))[:5]:
        print(f" - {ip}")

if __name__ == "__main__":
    file_path = input("Enter the path to your log file: ")
    analyze_log(file_path)
