import config
import requests
from pyngrok import ngrok


def main():
    public_url = ngrok.connect(8080, "http")
    url = "https://api.telegram.org/bot" + config.tg_token + \
        "/setWebhook?url=https://" + public_url[7:] + "/postjson"
    requests.get(url)
    input("ngrok has been set up \n tg bot set up \n press any key to exit")
    ngrok.kill()
    return()


if __name__ == '__main__':
    main()
