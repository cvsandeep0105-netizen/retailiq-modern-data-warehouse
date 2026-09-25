@echo off
cd /d "%~dp0.."
".\dashboard\.venv\Scripts\python.exe" -m streamlit run ".\dashboard\app\main.py" --server.headless=true --server.address=127.0.0.1 --server.port=8501 > ".\data\output\dashboard\streamlit-run.log" 2>&1

