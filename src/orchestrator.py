#!venv/bin/python

import subprocess

def main():
    start ngrok.py
    start webserver.py
    start login.py
    close webserver.py
    close login.py
    start watcher.py
    return()

if __name__ == '__main__':
    main()