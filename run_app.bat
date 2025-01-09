@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM Create a virtual environment if it doesn't exist
IF NOT EXIST "venv" (
    python -m venv venv
)

REM Activate the virtual environment
CALL venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Run the Flask application in the background
start /B python scriptpython.py

REM Wait for a moment to ensure the server starts
timeout /t 2 > nul

REM Open the application in the default web browser
start http://127.0.0.1:3214

ENDLOCAL
