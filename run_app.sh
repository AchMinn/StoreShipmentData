#!/bin/bash

# Exit on any error
set -e

# Create a virtual environment (optional)
if [ ! -d "bettyprk" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source bettyprk/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python3 scriptpython.py &

# Wait for a moment to ensure the server starts
sleep 2

# Open the application in the default web browser
xdg-open http://127.0.0.1:3214  # On macOS, use `open` instead of `xdg-open`.

# Open the CSV file
xdg-open dati_carico.csv &

wait
