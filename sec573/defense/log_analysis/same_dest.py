from collections import defaultdict

logs = [
    ("10.0.0.5", "51.22.19.5", "12:05"),
    ("10.0.0.8", "51.22.19.5", "12:05"),
    ("10.0.0.9", "8.8.8.8", "12:06"),
    ("10.0.0.7", "51.22.19.5", "12:07"),
    ("10.0.0.12", "1.1.1.1", "12:08"),
    ("10.0.0.10", "51.22.19.5", "12:09"),
]
# Map destination to list of hosts contacting it
dest_to_hosts = defaultdict(set)

for src, dest, ts in logs:
    dest_to_hosts[dest].add(src)

# Show destinations shared by many hosts only suspicious ones
for dest, hosts in dest_to_hosts.items():
    if len(hosts) > 1:  # only suspicious ones
        print(f"Destination: {dest}")
        print(f"Connected Hosts: {hosts}")
        print(f"Host Count: {len(hosts)}\n")