import config
import requests
from pyngrok import ngrok
import logging

logging.basicConfig(
    filename="logs/ngrok.log",
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(message)s', 
    )

def main():
    try:
        public_url = ngrok.connect(8080, "http")
        logging.info("ngrok has been started")
    except Exception as e:
        logging.error(f"ngrok start error \n{e}")
    url = "https://api.telegram.org/bot" + config.tg_token + \
        "/setWebhook?url=https://" + public_url[7:] + "/postjson"
    try:
        requests.get(url)
        logging.info("Bot has been connected to ngrok")
    except Exception as e:
        logging.error(f"Bot connecting error \n{e}")
    logging.info("ngrok service running")
    input("ngrok service running \npress any key to exit")
    logging.info("ngrok service stop")
    ngrok.kill()
    return()


if __name__ == '__main__':
    main()
