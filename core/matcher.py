MITRE_PATTERNS = {
    "T1059": ["powershell", "cmd.exe"],
    "T1071": ["ftp", "curl", "wget"],
    "T1021": ["rdp", "smb", "psexec"],
    "T1086": ["script", "macro", ".vbs"],
    "T1566": ["phish", "suspicious link", "email with attachment"]
}

def match_mitre_patterns(logs):
    matches = []
    for log in logs:
        combined = " ".join([str(v).lower() for v in log.values()])
        for tactic, keywords in MITRE_PATTERNS.items():
            if any(k in combined for k in keywords):
                matches.append({
                    "time": log.get("timestamp") or log.get("date") or "unknown",
                    "technique": tactic,
                    "desc": f"Possible {tactic} ({', '.join(keywords)})",
                    "log": log
                })
                break
    return matches