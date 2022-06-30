import os
import time
import asyncio
from webbrowser import Chrome

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()


async def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("enable-automation")
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


async def hh(username, password):

    driver = await get_driver('https://kazan.hh.ru/account/login?backurl=%2F')

    psw_btn = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/form/div[4]/button[2]')
    psw_btn.click()
    await asyncio.sleep(5)

    inp_username = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[1]/input')
    inp_username.send_keys(username)

    inp_psw = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[2]/span/input')
    inp_psw.send_keys(password)

    come_in_btn = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[4]/div/button[1]')
    come_in_btn.click()
    await asyncio.sleep(5)

    my_resume_btn = driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div/div[1]/div[1]/a')
    my_resume_btn.click()
    await asyncio.sleep(5)
    print('сайт hh сделаль')
    up_resume1 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume2 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[4]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume3 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[6]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume4 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[8]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume5 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[10]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume6 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[12]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume7 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[14]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume8 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[16]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume9 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[18]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume10 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[20]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume11 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[22]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume12 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[24]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume13 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[26]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume14 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[28]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume15 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[30]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume16 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[32]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume17 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[34]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume18 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[36]/div/div[6]/div/div/div/div[1]/span/button').click()
    await asyncio.sleep(0.5)
    up_resume19 = driver.find_element(By.XPATH, value='//*[@id="HH-React-Root"]/div/div/div[1]/div/div/div[1]/div[3]/div[38]/div/div[6]/div/div/div/div[1]/span/button').click()
    driver.close()


async def planfix(username, password, url):

    driver = await get_driver('https://dobrodel.planfix.ru/task/318')

    inp_username1 = driver.find_element(By.XPATH, value='//*[@id="tbUserName"]')
    inp_username1.send_keys(username)

    inp_psw1 = driver.find_element(By.XPATH, value='//*[@id="tbUserPassword"]')
    inp_psw1.send_keys(password)

    come_in_btn1 = driver.find_element(By.XPATH, value='//*[@id="fform"]/div/a').click()
    await asyncio.sleep(5)

    driver.get(url)
    await asyncio.sleep(5)

    reduct_btn = driver.find_element(By.XPATH,
                                     value='/html/body/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div/div[2]/div/input[3]').click()
    await asyncio.sleep(3)

    driver.switch_to.frame(driver.find_element(By.XPATH, value='//*[@id="cke_1_contents"]/iframe'))

    p = driver.find_element(By.XPATH, value='/html/body/p')
    p.send_keys('lol')

    driver.switch_to.default_content()

    save_btn = driver.find_element(By.XPATH, value='//*[@id="TaskSubmitBtn"]').click()
    print('насяльника, сайт planfix сделаль')
    driver.close()

print('Конфигурация HH.RU')
print('')
print('')

usernamehh = os.getenv('USERNAME_HH')
passwordhh = os.getenv('PASSWORD_HH')
pihh = float(os.getenv('PERIOD_HH'))

print('')
print('')
print('')
print('Конфигурация PLANFIX.RU')
print('')
print('')
usernameplanfix = os.getenv('USERNAME_PLANFIX')
passwordplanfix = os.getenv('PASSWORD_PLANFIX')
piplanfix = float(os.getenv('PERIOD_PLANFIX'))
url = os.getenv('URL')

async def hhtime(pihh):
    for i in range(10000):
        timehh = int(pihh * 86400)
        await asyncio.sleep(timehh)
        await hh(usernamehh, passwordhh)

async def planfixtime(piplanfix):
    for i in range(600):
        timeplanfix = int(piplanfix * 86000)
        await asyncio.sleep(timeplanfix)
        await planfix(usernameplanfix, passwordplanfix, url)


async def main():
    task2 = asyncio.create_task(planfixtime(piplanfix))
    task1 = asyncio.create_task(hhtime(pihh))

    await asyncio.gather(task2, task1)

if __name__ == '__main__':
    asyncio.run(main())
