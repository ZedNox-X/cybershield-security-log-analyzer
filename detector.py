from pathlib import Path
import pandas as pd

REQUIRED = {"timestamp", "source_ip", "event_type", "status"}

def load_logs(source):
    if hasattr(source, "read"):
        df = pd.read_csv(source)
    else:
        df = pd.read_csv(Path(source))
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    df["source_ip"] = df["source_ip"].astype(str)
    df["event_type"] = df["event_type"].astype(str).str.lower()
    df["status"] = df["status"].astype(str).str.lower()
    return df

def analyze_logs(logs, failed_login_threshold=5, port_threshold=10):
    alerts = []
    failed = logs[
        (logs["event_type"].isin(["login", "authentication"])) &
        (logs["status"].isin(["failed", "failure", "denied"]))
    ]
    for ip, group in failed.groupby("source_ip"):
        if len(group) >= failed_login_threshold:
            alerts.append({
                "source_ip": ip,
                "alert": "Repeated failed login attempts",
                "count": len(group),
                "severity": "High" if len(group) >= failed_login_threshold * 2 else "Medium",
                "first_seen": str(group["timestamp"].min()),
                "last_seen": str(group["timestamp"].max()),
            })

    scans = logs[logs["event_type"].isin(["port_scan", "connection_attempt"])]
    for ip, group in scans.groupby("source_ip"):
        ports = group["destination_port"].nunique() if "destination_port" in group.columns else len(group)
        if ports >= port_threshold:
            alerts.append({
                "source_ip": ip,
                "alert": "Possible port scanning activity",
                "count": int(ports),
                "severity": "High" if ports >= port_threshold * 2 else "Medium",
                "first_seen": str(group["timestamp"].min()),
                "last_seen": str(group["timestamp"].max()),
            })

    return pd.DataFrame(alerts, columns=[
        "source_ip", "alert", "count", "severity", "first_seen", "last_seen"
    ]).sort_values(["severity", "count"], ascending=[True, False], ignore_index=True)
