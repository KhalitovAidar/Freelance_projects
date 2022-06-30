import time

from selenium import webdriver

def get_driver(PROXY):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(PROXY)

    driver = webdriver.Chrome(executable_path=r'C:\Users\khali\PycharmProjects\forFreelance\pseudo-human\chromedriver.exe',
                              chrome_options=chrome_options)
    driver.set_window_size(300, 500)
    return driver

driver = get_driver('proxy1.zip')

driver.get('https://whatismyipaddress.com/')
time.sleep(100)