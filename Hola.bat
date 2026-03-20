@echo off
cd /d "%~dp0"

call venv\Scripts\activate

py src/Main.py

pause