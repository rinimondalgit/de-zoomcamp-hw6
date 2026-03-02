
\# Workshop 1 — Ingestion with dlt (Data Engineering Zoomcamp 2026)



\[!\[Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

\[!\[CI](https://github.com/rinimondalgit/de-zoomcamp-hw6/actions/workflows/ci.yml/badge.svg)](https://github.com/rinimondalgit/de-zoomcamp-workshop1-dlt/actions/workflows/ci.yml)



Ingestion pipeline for \*\*Workshop 1: Ingestion with dlt\*\* from \*\*Data Engineering Zoomcamp 2026\*\*.  

Loads NYC taxi data using `dlt` and computes submission answers:

\- Dataset start/end date

\- % of trips paid by credit card

\- Total tips amount



---



\## Project Structure



```text

de-zoomcamp-workshop1-dlt/

├─ README.md

├─ requirements.txt

├─ .gitignore

├─ .env.example

├─ src/

│  ├─ pipeline.py

│  └─ ...

└─ scripts/

&nbsp;  ├─ run\_pipeline.py

&nbsp;  └─ compute\_answers.py







python -m venv .venv

\# Windows

.venv\\Scripts\\activate

\# Mac/Linux

\# source .venv/bin/activate



pip install -r requirements.txt

\# Windows

copy .env.example .env

\# Mac/Linux

\# cp .env.example .env

✅ Question 1: What is the start date and end date of the dataset?

answer:
2024-06-01 to 2024-07-01

Explanation:
The workshop ingests NYC taxi data for June 2024, and the dataset covers trips from:

Start: 2024-06-01

End: 2024-07-01 (exclusive upper bound)

✅ Question 2: What proportion of trips are paid with credit card?

answer:
26.66%

Explanation:
The payment_type column contains payment methods, and credit card corresponds to:
payment_type = 1
26.66%

✅ Question 3: What is the total amount of money generated in tips?

answer:
$8,063.41

Explanation:
Summing the tip_amount column across all trips gives:Total tips = $8,063.41




# de-zoomcamp-hw6
e2da7a33b22bb21ffeb9cb36c776b3e35c7614df
