#!/bin/bash

# Activate virtual environment
source venv_bing/bin/activate

# Run Python script with any additional arguments passed to the script
python automate_mac.py chrome quiz "$@"

