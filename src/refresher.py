#!venv/bin/python

from selenium import webdriver
from time import sleep
import telegram
import config # private data set

screnshot_path  = 'screenshot.png'
input_login     = '//*[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username"]'
input_password  = '//*[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password"]'
input_privacy   = '/html/body/div[1]/div/div/div/span/form/div[2]/div[2]/table/tbody/tr[3]/td/label/input'
input_captcha_response = '//*[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:recaptcha_response_field"]'
input_some_data = '//*[@id="ctl00_nav_side1"]/ul/div'
url_first_page  = "/applicanthome"
url_last_page   = "/scheduleappointment"

def init() -> object: 
    driver = webdriver.Chrome()
    print(f"Opening {config.url} in Chrome...")
    driver.get(config.url)
    return(driver)

def getElement(driver: object, element: str, mode: str) -> object:
    print("Looking for element")
    if mode == "id":
        try:
            button = driver.find_element_by_id(element)
            print(f"{element} found")
        except Exception as e:
            print(f"Cant find {element} Error: \n {e}")
            exit(1)
    if mode == "xpath":
        try:
            button = driver.find_element_by_xpath(element)
            print(f"{element} found")
        except Exception as e:
            print(f"Cant find {element} Error: \n {e}")
            exit(1)
    else:
        print(f"function exception")
    return (button)

def send(image_path, chat_id=config.tg_user, token=config.tg_token):
    bot = telegram.Bot(token=token)
    try:
        bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
    except Exception as e:
        print(f"Cant send. Error: \n {e}")

def main():
    
    driver = init()
    getElement(driver, input_login, "xpath").send_keys(config.user)
    getElement(driver, input_password, "xpath").send_keys(config.password)
    getElement(driver, input_privacy, "xpath").click()
    getElement(driver, input_captcha_response, "xpath").click()
    # add capcha # some_data = getElement(input_some_data, "xpath")
    input("Proceed with login then press any key to continue...")
    i = 0
    while True:
        i += 1
        driver.refresh
        driver.save_screenshot(screnshot_path)
        send(screnshot_path)
        print(f"sent screnshot #{i}")
        sleep(config.refresh_int)
    return()

if __name__ == '__main__':
    main()