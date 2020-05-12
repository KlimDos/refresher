# A tool for refreshing wer page in local browser 

## How to run
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install setuptools`
- `pip install -r requirements.txt`

## Install chromedriver

### MacOS
- download chromedriver
- `cp <path to downloaded binary> venv/bin/chromedriver`
- `spctl --add --label 'Approved' chromedriver` or `xattr -d com.apple.quarantine <name-of-executable>`

## Add config.py file to src directory
```
url         = str
user        = str
password    = str
tg_user     = str
tg_token    = str
refresh_int = int
```

## Run:
`python src/refresher.py`
    
## ngrok

curl https://api.telegram.org/bot{BOT_KEY}/setWebhook?url={NGROK_URL}
curl "https://api.telegram.org/bot{config.tg_token}/setWebhook?url=https://bc038cae.ngrok.io/postjson"


todo

- mkdir logs
- add `bot-response.json` some how