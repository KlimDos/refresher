from selenium import webdriver
from time import sleep
import telegram
import logging
import sys
from PIL import Image

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

tg_token = sys.argv[1]
tg_user = '242426387'
screenshot = 'welcome_page.png'
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--window-size=1200,1000")
#chrome_options.add_argument("--start-minimized")
driver = webdriver.Chrome(chrome_options=chrome_options)

def send(image_path, chat_id=tg_user, token=tg_token):
    bot = telegram.Bot(token=token)
    try:
        bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
    except Exception as e:
        print("Cant send. Error:")
        print(e)


def getElement(element: str, mode: str) -> object:
    '''
    
    '''
    print("Looking for element")
    if mode == "id":
        try:
            button = driver.find_element_by_id(element)
            print(f"{element} found")
        except:
            print(f"Cant find {element}")
    if mode == "xpath":
        try:
            button = driver.find_element_by_xpath(element)
            print(f"{element} found")
        except:
            print(f"Cant find {element}")
    else:
        print(f"function exception")
    return (button)

def refresh(url: str, interval: int, count: int):
    while count > 0:
        print(f"Refreshing the page #{count}...")
        #driver.refresh
        driver.get(url)
    return()

def takeScr(url, path):
    print(f"Opening {url} in Chrome...")
    driver.get(url)
    sleep(5)
    driver.save_screenshot(path)
    print(f"Closing Chrome...")
    driver.quit()
    return (path)

def main():
    url = sys.argv[2]
    find_element = 'loginPage\:SiteTemplate\:siteLogin\:loginComponent\:loginForm\:loginButton'
    find_element_2 = '/html/body/div[1]/div/div/div/span/form/div[2]/div[2]/table/tbody/tr[3]/td/label/input'
    refresh_interval = int(sys.argv[3])
    frame = eval(sys.argv[4])
    i = 0
    print(f"Opening {url} in Chrome...")
    driver.get(url)
    input("Proceed with login then press any key to continue...")
    while True:
        i += 1
        #driver.get(url+"/scheduleappointment")
        driver.get(url+"/applicanthome")
        driver.save_screenshot(screenshot)
        print (f"screenshot #{i}")
        if sys.argv[4] == "setup":
            frame = eval(input("frame="))
        Image.open(screenshot).crop(frame).save(screenshot)
        send(screenshot)
        #driver.get(url+"/applicanthome")
        sleep(refresh_interval)
    print(f"Closing Chrome...")
    driver.quit()

    # pic = takeScr(url,screenshot)
    # Image.open(pic).crop((775, 970, 1230, 1230)).save(pic)
    # send(pic)
    #getElement(find_element_2, "xpath").click()
    #sleep(refresh_interval+30)
    #print("Closing Chrome")
    #driver.quit()

if __name__ == '__main__':
    main()
