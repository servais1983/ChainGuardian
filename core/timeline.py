from datetime import datetime

def build_timeline(entries):
    def extract_time(e):
        for k in ["time", "timestamp", "date"]:
            if k in e:
                try:
                    return datetime.fromisoformat(e[k])
                except:
                    continue
        return datetime.min

    return sorted(entries, key=extract_time)