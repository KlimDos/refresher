#!venv/bin/python

from selenium import webdriver
from time import sleep
import telegram
import config # private data set
import pickle

screnshot_path  = 'screenshot.png'
url_first_page  = "/applicanthome"
url_last_page   = "/scheduleappointment"
new_applocation = '//*[@id="j_id0:SiteTemplate:j_id52:j_id53:j_id54:j_id58"]/a'


def init(cookies_file) -> object: 

    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_experimental_option("w3c", False)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    print(f"Opening {config.url} in Chrome...")
    driver.get(config.url)
    cookies = pickle.load(open(cookies_file, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(config.url+url_first_page)
    return(driver)

def send(image_path, chat_id=config.tg_user, token=config.tg_token):
    bot = telegram.Bot(token=token)
    try:
        bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
    except Exception as e:
        print(f"Cant send. Error: \n {e}")

def main():
    driver = init("cookies.pkl")
    i = 0
    while True:
        i += 1
        driver.get(config.url+url_first_page)
        #div = getElement(driver, new_applocation).screenshot(screnshot_path)
        driver.save_screenshot(screnshot_path)
        #print(type(div))
        send(screnshot_path)
        print(f"sent screnshot #{i}")
        sleep(config.refresh_int)
    return()

if __name__ == '__main__':
    main()