#!bin/bash

source venv/bin/activate
pip install -r requirements.txt
python src/ngrok.py
python src/webserver.py
python src/login.py