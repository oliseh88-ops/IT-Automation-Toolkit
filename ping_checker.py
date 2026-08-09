import subprocess
import re

target = input("Enter a website or IP address: ")

result = subprocess.run(
    ["ping", "-c", "4", target],
    capture_output=True,
    text=True
)

print("\n===== NETWORK CHECK =====")
print(f"Target: {target}")

if result.returncode == 0:
    print("Status: ONLINE")

    packet_loss = re.search(r"(\d+\.?\d*)% packet loss", result.stdout)

    latency = re.search(
        r"round-trip min/avg/max/stddev = [\d.]+/([\d.]+)/",
        result.stdout
    )

    if packet_loss:
        print(f"Packet Loss: {packet_loss.group(1)}%")

    if latency:
        print(f"Average Latency: {latency.group(1)} ms")

else:
    print("Status: OFFLINE")

print("=========================")