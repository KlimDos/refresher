# A tool for refreshing wer page in local browser 
### How to run

- `python3 -m venv venv`
- `source venv/bin/activate`
- pip install --upgrade pip
- pip install setuptools
- `pip install -r requirements.txt`

### install and whitelist chromedriver
### MacOS
- download chromedriver
- `cp bin/chromedriver venv/bin/chromedriver`
- `spctl --add --label 'Approved' chromedriver` or `xattr -d com.apple.quarantine <name-of-executable>`

- export tg_token

example:
`python src/main.py "aaaaaabbbbbbxxxxxx" "https://google.com/" "10" "450, 1000, 800, 1130"`