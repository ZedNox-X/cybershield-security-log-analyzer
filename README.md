# CyberShield – Security Log Analyzer

CyberShield is a beginner-friendly defensive cybersecurity project. It analyzes CSV security logs and highlights patterns that may indicate repeated failed logins or port scanning.

## Features
- Upload a CSV log file or use the included sample data.
- Detect repeated failed login attempts by source IP.
- Detect possible port scanning based on distinct destination ports.
- Assign Medium or High severity.
- View event summaries and download alerts as CSV.
- Includes a small automated test suite.
<img width="1600" height="1200" alt="RgSo4kjo98aMMfMHZ3xYqT_4ez3I0rBXVjj5J569Us2LDlHfxkAwNRfNhBFUNISxaryME8duVHC744bwPlOd4OarwoGn4gy0EDaSueaO2naAKvMVfU8vGNc19HhWYR4oKC7BQuzN7XwsJ5oO_u0c2xqPPRwAOhqSm7okx81UuLtxz3XgcFcVGywEet9uMrG8" src="https://github.com/user-attachments/assets/21d028bc-82bb-4395-af6a-31352797f144" />
<img width="1724" height="916" alt="-IgCGwahzhmZD7_emrRmo4gLog83jOo5IwSU8pTxdjqvxz819glejARryM4qjAVw_zMmqE-KUeJNsoWF54GRLvKuZfaRN2ZO3eP9NGD5fKIdhtOVzj0a6gHq5GVdWt2HS8hwKuT53SQxDeNd18U2NBptIvAI7FbxeNHnrnU9lZlAauqj-UDdliHikOVkZn-u" src="https://github.com/user-attachments/assets/c88c46d5-3351-4699-aa42-f6d51ff63331" />
<img width="1222" height="844" alt="O_GSAsw_5UsFuEWzBGToRaDtDUSL7eUYzqD34NFMcGiXKcqzaqEe9L1kZDxTNalkogtXKgM8_QLzBCCHf5u2xEI6w5Y4UzP95Bc2NxPGLtuzHTuuA2UpJ1Ib4YUqXkLGHfv35EHAg47ep5r-ou4T2A00wtyhEJxN-rHKL0hiYklcw5pmW_RnmLxicPSUYun3" src="https://github.com/user-attachments/assets/66f1f8f1-191d-4c51-a6b5-4488e094c22f" />

<img width="3778" height="2119" alt="4v7IUDur3ZFz2G7eqRPsZx4spbEa4Ctl5vMjD_pnQ2kg2devoLXlcY100VfQsp7sGrTRHT_IN60OOdvLcemeZjEbyVsMBG-QMiG790KqQm0118Bc07ZBEoKlxFKuhu-IIEpR7z-o8YWutERS2TSepjSU3H4ssoBT6V7biCL3pG7_40NeAJNdXFOriIWSLNFX" src="https://github.com/user-attachments/assets/3614f18f-70fd-4813-9924-cdd73aba09cf" />
<img width="1800" height="935" alt="Ng6ZOO5gHzRKlwAw_qexcuB9QKVDSXuFk40f5rmp_fOImDa0e5yAZuYkSjY_OXZNN29IMLP3vghaYFClDsLdEHzuWdRUxZwITTmd7mUVBI09E2pCQTiSvwsk30-UjAnpJ1Bb1T_6AOo85UovZuaFKPQELi_5SNANs8z7UIerdp-VlDklFF2QXAbwEhsjk1Cz" src="https://github.com/user-attachments/assets/c3ab9925-ee68-4866-85cb-512c52701a19" />
<img width="2551" height="1259" alt="jMObWIDhZRppKVl2oF9YjuDnmPBmD-upVOE4feKGINUO-iRxi84xW2Z7POBxKG1gcj_4mILm5l5eGfnBXqqhPfQpjGJ9LOAensmLqCG5qwLrFUWgXMs6o0y73amhtilRrEY_IMVVeAyMfkHE__u4A7q9PYHkrG0n42-30_yCQ3464E7QZrbgqxpzJOxbYjz5" src="https://github.com/user-attachments/assets/16f9a782-9cc1-48e6-bbc2-ac6bdc1ca323" />
<img width="780" height="396" alt="Of9SX-8vu6_IvMHN9mPB3mUcTMjqiGg4FgIL4YC5rwaYMYrRBVJ7p9WfVU-ViXA65XKniKAF04FvTHmMtmLOSOUMfS6uK19LeZt63JSJ8ZbLvJKLPFNTbGsIFPswoXjZinu2r-6P4da_5KEJdu49tB3auW7fPcrrzLNp7qSymUmutN5Gj89D5jHq27kd08qG" src="https://github.com/user-attachments/assets/cacc952e-8a42-416d-8391-09f8ec5f5309" />
<img width="1024" height="768" alt="quSyLPjhVfbcAPdEdbWKd5ZglhiRghxq48bZIeNzur3N3NxwLYXi0VvAn9ivZy_34vyaJLqWEFugrq9gKlq1ExDqqHgmfpae0JUxjP-UC7eVFdin5lsue1gh3cvk-5lFu8OTj_6opSHy5VzWIuxhlkq0pP-Qa085P5ulUF01XoRGy-goMHtFiq9-d4uTXEzL" src="https://github.com/user-attachments/assets/ebe0d2ce-2d1e-4a34-a01e-5f3cf9522f41" />
<img width="1180" height="673" alt="diYeZ5tIHEUOo_o3RXWO0kTi8EJ9G5eKxMBRrlbldjNHLrv_gyMbHC5MJceFz4WMP5pIWAJ6G3NJbuYVX6PTkQDOw4z8l3yOVLZXYWeoe0drbnZDG5zhnzK-xzA_HdmlJTQpgK7sLTkCe7ijNBUq9sLRcGS0DZg0VhP0dIRxSemTYwMo-1TsDTTe-2ptR8XA" src="https://github.com/user-attachments/assets/e228b7ba-3701-434a-acda-b3a486275ecd" />
<img width="1400" height="788" alt="FJ8iLvYDiUuQp_BSMJaed0fELLx2Q4ljMNZwAcaCgeKptQwHaWmUU85coznMMIpDaFkNyZxXr6aE0VQwXiiNzMqoQ8JduVvzumk1-c5jFejsuSMf_6veusNR7uDvMoGGB1gzDoGgeRNQh7EM8nGSB-QWhMehRm2vF-EmufQwxP4msv6_u8vUj2IdILX2sJjO" src="https://github.com/user-attachments/assets/0e5f72a4-7dad-4a31-8726-19159fde8899" />
<img width="1024" height="682" alt="GqNfgTTPYxgyHdd8H8F1n7M8IBNeLgOamMK2S8HugMQPKn2tkmxU32TL5n9z8j6Vvgsip7YrsTs_8-W4ntVqLcNTcXNuhDpEahsNLdYDvp3p5IJOIG4L0Tg2iF0okcxBD3Xh6ddFKPmo6jJsaLNsdwCX6sPMt_Ic870h4oPKYDse3cmiSm98DxaGhM5-dzhK" src="https://github.com/user-attachments/assets/1e21165e-bf74-4c9d-8d95-7de22d2a5778" />
<img width="1920" height="1088" alt="SzTDqXkG8uQmLXPj-ZzvJ4flQRhyut9ROf3vYncCZIvDSrE-gnid8PMhnaTZCBAWicv2tHIPatwTpnh4ryr9VFk0PtY_Tnhs-TYanK7QkA6lsyzqgZrqra7RLgUYPoXIuTG26Zn7CCBVMVcqXaYAOcVKR9xBHDJbjNJG0xLYUnZRapxqA2vOIsOfnD2jXivt" src="https://github.com/user-attachments/assets/5396234e-3512-4649-98ed-c0e19c6ad7eb" />


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
