from selenium import webdriver
import config
import pickle
from watcher import send
import telegram
from time import sleep
import json

input_login     = '//*[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username"]'
input_password  = '//*[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password"]'
input_privacy   = '/html/body/div[1]/div/div/div/span/form/div[2]/div[2]/table/tbody/tr[3]/td/label/input'
input_captcha_response = '//*[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:recaptcha_response_field"]'
input_captcha_pic = '//*[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:theId"]'
input_login_bt = '//*[@id="loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton"]'
screnshot_path  = 'captcha.png'

def getCookies(cookies_file): 

    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_experimental_option("w3c", False)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    print(f"Opening {config.url} in Chrome...")
    driver.get(config.url)
    getElement(driver, input_login).send_keys(config.user)
    getElement(driver, input_password).send_keys(config.password)
    getElement(driver, input_privacy).click()
    sleep(3)
    getElement(driver, input_captcha_pic).screenshot(screnshot_path)
    with open('bot-response.json', 'r', encoding='utf-8') as f:
        code = json.load(f)
        msg_id = msg_id_new = code['message']['message_id']
        f.close()
    send(screnshot_path)
    while True:
        sleep(1)
        with open('bot-response.json', 'r', encoding='utf-8') as f:
            code = json.load(f)
            msg_id_new = code['message']['message_id']
            if msg_id_new != msg_id:
                f.close()
                break
    getElement(driver, input_captcha_response).send_keys(code['message']['text'])
    getElement(driver, input_login_bt).click()
    sleep(5)
    pickle.dump(driver.get_cookies(), open(cookies_file, "wb"))
    driver.close()
    return()

def getElement(driver: object, element: str) -> object:
    try:
        button = driver.find_element_by_xpath(element)
    except Exception as e:
        print(f"Cant find {element} Error: \n {e}")
        exit(1)
    return (button)

def main():
    getCookies("cookies.pkl")
    return()

if __name__ == '__main__':
    main()