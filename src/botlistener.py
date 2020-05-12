#!venv/bin/python

import json
from time import sleep
import subprocess

def listen(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        message_text = data['message']['text']
        f.close()
    return(message_text)

def runApp(file):
    p = subprocess.call(["python", "src/"+file])
    return(p)

def main():
    prev_message = message = ""
    while True:
        message = listen("bot-response.json")
        if prev_message != message:
            print(message)
            prev_message = message
        elif message.lower() == "stop":
            print(f"stop listening")
            return()
        elif message == "login":
            runApp("login.py")
        sleep(1)
    return()

if __name__ == '__main__':
    main()