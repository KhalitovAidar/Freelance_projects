import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://dobrodel.planfix.ru/task/318')

inp_username1 = driver.find_element(By.XPATH, value='//*[@id="tbUserName"]')
inp_username1.send_keys('advokaty')

inp_psw1 = driver.find_element(By.XPATH, value='//*[@id="tbUserPassword"]')
inp_psw1.send_keys('Legis55511')


come_in_btn1 = driver.find_element(By.XPATH, value='//*[@id="fform"]/div/a').click()
time.sleep(5)

driver.get('https://dobrodel.planfix.ru/task/318')
time.sleep(5)

reduct_btn = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div/div[2]/div/input[3]').click()
time.sleep(3)

driver.switch_to.frame(driver.find_element(By.XPATH, value='//*[@id="cke_1_contents"]/iframe'))

p = driver.find_element(By.XPATH, value='/html/body/p')
p.send_keys('lol')

driver.switch_to.default_content()

save_btn = driver.find_element(By.XPATH, value='//*[@id="TaskSubmitBtn"]').click()

driver.close()

