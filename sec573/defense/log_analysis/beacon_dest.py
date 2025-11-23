from collections import Counter

# Load logs (list of tuples like: (src_ip, dest_ip, timestamp))
logs = [
    ("10.0.0.5", "51.22.19.5", "12:05"),
    ("10.0.0.8", "51.22.19.5", "12:05"),
    ("10.0.0.9", "8.8.8.8", "12:06"),
    ("10.0.0.7", "51.22.19.5", "12:07"),
    ("10.0.0.12", "1.1.1.1", "12:08"),
    ("10.0.0.10", "51.22.19.5", "12:09"),
]

# Count how many times each destination was contacted
dest_counts = Counter([entry[1] for entry in logs])

print("Most contacted destinations:")
for dest, count in dest_counts.most_common():
    print(f"{dest} → {count} connections")

# The highest one is likely the C2 destination