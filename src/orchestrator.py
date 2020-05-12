#!venv/bin/python

import subprocess
import logging
from time import sleep

logging.basicConfig(
    filename="logs/orchestrator.log",
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(message)s', 
    )

def main():
    try:
        process = subprocess.Popen(["python", "src/ngrok.py"], stdout=subprocess.PIPE)
        logging.info("ngrok.py started")

        
    except Exception as e:
        logging.error(["ngrok.py failed to start"], [e])
    try:
        subprocess.Popen(["python", "src/webserver.py"])
        logging.info("webserver.py started")
    except Exception as e:
        logging.error(["webserver.py failed to start"], [e])
    try:
        p3 = subprocess.Popen(["python", "src/botlistener.py"])
        logging.info("botlistener.py started")
        while p3.poll() is None:
            sleep(0.5)
    except Exception as e:
        logging.error(["botlistener.py failed to start"], [e])
    #start login.py
    #close webserver.py
    #close login.py
    #start watcher.py
    return()

if __name__ == '__main__':
    main()