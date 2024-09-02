#!/bin/bash

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install requirements from requirements.txt
pip install -r requirements.txt

# Run the application
python3 main.py

# Deactivate the virtual environment
deactivate