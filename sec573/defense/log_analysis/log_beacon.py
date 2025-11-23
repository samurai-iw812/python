#Log grouping and Beacon detection
from collections import defaultdict
from datetime import datetime

#sample log data
logs=[
    ("12/Jul/2025:10:00:00", "192.168.1.100", "8.8.8.8"),
    ("12/Jul/2025:10:00:01", "192.168.1.100", "8.8.8.8"),
    ("12/Jul/2025:10:00:02", "192.168.1.100", "8.8.8.8"),
    ("12/Jul/2025:10:00:03", "192.168.1.100", "8.8.8.8"),
    ("12/Jul/2025:10:00:04", "192.168.1.100", "8.8.8.8"),
    ("12/Jul/2025:10:00:05", "192.168.1.101", "8.8.8.9"),
    ("12/Jul/2025:10:00:06", "192.168.1.110", "8.8.8.10"),
    ("12/Jul/2025:10:00:07", "192.168.1.101", "8.8.8.11"),
    ("12/Jul/2025:10:00:08", "192.168.1.120", "8.8.8.12"),
    ("12/Jul/2025:10:00:09", "192.168.1.130", "8.8.8.13"),
]

#group logs by src_ip
groups=defaultdict(list)

for ts,src,dst in logs:
    groups[src].append((ts,dst))

#create minute buckets
def minute_bucket(ts):
    return datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S").minute

buckets=defaultdict(lambda: defaultdict(list))

for src,log_entries in groups.items():
    for ts,dst in log_entries:
        minute=minute_bucket(ts)
        buckets[src][minute].append(dst)


#detect beacons
def detect_beacons(buckets):
    for src,minutes in buckets.items():
        for minute,dsts in minutes.items():
            if len(dsts) > 1:
                print(f"Beacon detected from {src} at {minute}: {dsts}\n")
                return True
            else:
                return False

print(detect_beacons(buckets))

