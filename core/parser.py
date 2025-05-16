import json
import csv

def parse_log_file(path):
    entries = []
    if path.endswith(".json"):
        with open(path) as f:
            for line in f:
                try:
                    log = json.loads(line)
                    entries.append(log)
                except:
                    continue
    elif path.endswith(".csv"):
        with open(path) as f:
            reader = csv.DictReader(f)
            entries.extend(reader)
    elif path.endswith(".log"):
        with open(path) as f:
            for line in f:
                entries.append({"raw": line.strip()})
    return entries