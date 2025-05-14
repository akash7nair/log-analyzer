to the code enter this (python -m streamlit run app.py)
# Interactive Log Analyzer

A Python-based tool for analyzing application logs with an interactive dashboard, designed to identify critical events and anomalies in log files.

## Features

- 🕒 Time-windowed analysis (1h/6h/24h/custom)
- ⚠️ Error & warning detection with regex patterns
- 📊 Interactive Streamlit dashboard
- 📈 Frequency analysis of log messages
- 🆕 Unique message identification
- 🐳 Docker container support

## Prerequisites

- Python 3.8+
- pip package manager
- Docker for containerization

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer

# Install dependencies
pip install -r requirements.txt

log-analyzer/
├── analyzer.py          # Core analysis logic
├── app.py               # Streamlit dashboard
├── Dockerfile           # Container configuration
├── requirements.txt     # Python dependencies
└── sample_data/         # Example logs
## Acknowledgments
- DeepSeek AI for development assistance and code suggestions
- [LogHub](https://github.com/logpai/loghub) for sample log datasets
