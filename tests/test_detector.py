import pandas as pd
from detector import analyze_logs

def test_detects_repeated_failed_logins():
    rows = [{
        "timestamp": pd.Timestamp("2026-11-16T09:00:00Z"),
        "source_ip": "198.51.100.24",
        "event_type": "login",
        "status": "failed",
        "destination_port": 22,
    }] * 5
    alerts = analyze_logs(pd.DataFrame(rows))
    assert len(alerts) == 1
    assert alerts.iloc[0]["alert"] == "Repeated failed login attempts"
