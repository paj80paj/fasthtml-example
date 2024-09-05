#!/bin/bash

# Check if a Python file is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <python_file>"
    exit 1
fi

PYTHON_FILE="$1"

# Check if the provided file exists
if [ ! -f "$PYTHON_FILE" ]; then
    echo "Error: File '$PYTHON_FILE' not found"
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install requirements from requirements.txt
pip install -r requirements.txt

# Run the provided Python file
python3 "$PYTHON_FILE"

# Deactivate the virtual environment
deactivate

