from collections import defaultdict


logs = [
    ("10.0.0.5", "51.22.19.5", "12:05:01"),
    ("10.0.0.8", "51.22.19.5", "12:05:03"),
    ("10.0.0.9", "8.8.8.8", "12:06:15"),
    ("10.0.0.7", "51.22.19.5", "12:07:20"),
    ("10.0.0.12", "1.1.1.1", "12:08:17"),
    ("10.0.0.10", "51.22.19.5", "12:09:44"),
]

host_times = defaultdict(list)

for src, dest, timestamp in logs:
    if dest == "51.22.19.5":
        minute = int(timestamp.split(":")[1])
        host_times[src].append(minute)

beacon_results = {}

for host, minutes in host_times.items():
    if len(minutes) > 1:
        diffs = [minutes[i+1] - minutes[i] for i in range(len(minutes)-1)]
        all_equal = len(set(diffs)) == 1
        beacon_results[host] = {
            "minutes": minutes,
            "intervals": diffs,
            "beaconing": all_equal
        }

