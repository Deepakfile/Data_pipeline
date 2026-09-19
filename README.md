# DataFlow AI v2

Universal Data Cleaning + Data Quality + Automated Analytics platform built with Python, Pandas, Plotly and Streamlit.

## Workflow

Upload → Profile → AI Cleaning Plan → Approve → Clean → Validate → AI Insights Studio → Export

## Features

- CSV, TSV, TXT, XLSX, XLS, JSON, Parquet, XML and ZIP ingestion
- Data profiling and issue detection
- Deterministic Pandas cleaning engine
- Optional OpenAI/Gemini recommendation layer
- Before/after quality measurement
- Audit/change log
- Validation checks
- Automated Plotly visualizations
- Automated insight generation
- Clean CSV export

## Architecture

LLM recommends operations. Python executes them. The LLM never directly modifies the dataframe.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```

Linux/macOS activation:
`source .venv/bin/activate`

## AI

AI is optional. Without an API key, deterministic rule-based recommendations are used.

Only metadata, profiling information and issue summaries should be sent to an external model. Do not upload sensitive datasets to external AI services without reviewing the provider's terms and your data policy.

## Project goal

Demonstrate data ingestion, profiling, cleaning, validation, auditability, visualization and AI-assisted analytics in one portfolio project.
