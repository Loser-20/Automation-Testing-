from datetime import datetime, timedelta
import os

FILE_NAME = "output.txt"
START_FILE = "start_time.txt"

# Load or set start time
if not os.path.exists(START_FILE):
    start_time = datetime.now()
    with open(START_FILE, "w") as f:
        f.write(start_time.isoformat())
else:
    with open(START_FILE, "r") as f:
        start_time = datetime.fromisoformat(f.read().strip())

end_time = start_time + timedelta(days=7)
now = datetime.now()

# Stop after 7 days
if now >= end_time:
    print("7 days completed. Skipping write.")
    exit(0)

# Write current time
with open(FILE_NAME, "a") as f:
    f.write(f"Hello + current time is: {now}\n")

print(f"Written at {now}")
