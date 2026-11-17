# CyberShield – Security Log Analyzer

CyberShield is a beginner-friendly defensive cybersecurity project. It analyzes CSV security logs and highlights patterns that may indicate repeated failed logins or port scanning.

## Features
- Upload a CSV log file or use the included sample data.
- Detect repeated failed login attempts by source IP.
- Detect possible port scanning based on distinct destination ports.
- Assign Medium or High severity.
- View event summaries and download alerts as CSV.
- Includes a small automated test suite.

## Tech stack
- Python
- Streamlit
- Pandas
- Pytest

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit (usually http://localhost:8501).

## CSV format

Required columns:

| Column | Description |
|---|---|
| timestamp | Date/time of the event |
| source_ip | Source IP address |
| event_type | `login`, `authentication`, `port_scan`, or `connection_attempt` |
| status | `failed`, `failure`, `denied`, `success`, or other status |

Optional column: `destination_port` (used to count distinct ports).

Use the included `data/sample_logs.csv` to try the dashboard. The sample IP addresses are documentation-only ranges and are not real attack sources.

## Run tests

```bash
pytest
```

## GitHub upload

Create a new repository named `cybershield-security-log-analyzer`, then run these commands from this project folder:

```bash
git init
git add .
git commit -m "Initial CyberShield security log analyzer"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cybershield-security-log-analyzer.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Important safety note
This project is for defensive analysis of logs you own or are authorized to inspect. It does not scan networks, exploit systems, or block traffic. Detection thresholds are simple educational heuristics and should not be treated as proof of compromise.
