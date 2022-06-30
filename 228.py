import time
from datetime import date, datetime

import os

from dotenv import load_dotenv

from selenium import webdriver

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from anticaptchaofficial.imagecaptcha import *
import requests

load_dotenv()

SEARCH_DEPTH = os.getenv('SEATCH_DEPTH')
REGION = os.getenv('REGION')
LANGUAGE = os.getenv('LANGUAGE')


def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path=r'H:\проги\1. Я.Парсер NEW\chromedriver.exe', options=chrome_options)
    return driver


def urll(key, k):
    url = 'https://yandex.ru/search/?text=' + str(key) + '&lr='+str(REGION)+'&rstr=' + '&lang=' + str(LANGUAGE) +'&p=' + str(k)
    return url


def parse_all(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')

    lis = []
    links = []

    all_lis = soup.find_all('li', class_='serp-item desktop-card')

    for i in all_lis:
        text = i.find('span', class_='organic__advLabel')
        if text == None:
            lis.append(i)
    for li in lis:
        try:
            links.append(li.find('a').get('href'))
        except:
            print('')
    return links


def part_parse(driver, count):
    soup = BeautifulSoup(driver.page_source, 'lxml')

    lis = []
    links = []

    all_lis = soup.find_all('li', class_='serp-item desktop-card')[:count]

    for i in all_lis:
        text = i.find('span', class_='organic__advLabel')
        if text == None:
            lis.append(i)
    for li in lis:
        try:
            a = li.find('a').get('href')
        except:
            a = ''
        links.append(a)
        print(links)

    return links


def info():
    with open('ban_sites.txt', 'r') as ban_sites_file:
        ban_sites = []
        for i in ban_sites_file:
            ban_sites.append(i.split('\n')[0])

    with open('ban_words.txt', 'r') as ban_words_file:
        ban_words = []
        for i in ban_words_file:
            ban_words.append(i.split('\n')[0])

    with open('keys.txt', 'r') as keys_file:
        keys = []
        for i in keys_file:
            keys.append(i.split('\n')[0])

    with open('../../../Downloads/duplicates.txt', 'r') as duplicate_file:
        duplicate_sites = []
        for i in duplicate_file:
            duplicate_sites.append(i.split('\n')[0])


    return ban_sites, ban_words, keys, duplicate_sites


def site_info(driver, link):
    driver.get(link)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    title = ''
    text = ''
    description = ''

    try:
        title = soup.find('title').get_text()
    except:
        print('')

    try:
        descriptions = soup.find_all('meta')
    except:
        print('')

    for i in descriptions:
        if i.get('name') == 'description':
            description = i.get('content')
    try:
        text = soup.get_text()
    except:
        print('')
    if title == None:
        title = ''
    if text == None:
        text = ''
    if description == None:
        description = ''

    text.split()
    new_text = ' '.join(text.split())

    return title, description, new_text


def captcha():
    driver.find_element(by=By.CLASS_NAME, value='CheckboxCaptcha-Button').click()
    time.sleep(3)
    img = driver.find_element(by=By.CLASS_NAME, value='AdvancedCaptcha-Image').get_attribute('src')

    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("72b28b4d1de32e12747282dd17324864")

    p = requests.get(img)
    out = open("img.png", "wb")
    out.write(p.content)
    out.close()

    for i in range(1000):
        captcha_text = solver.solve_and_return_solution("img.png")
        if captcha_text != 0:
            print(captcha_text)
            break

    driver.find_element(by=By.CLASS_NAME, value='Textinput-Control').send_keys(captcha_text)
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[2]/form/div[2]/button[3]').click()


my_file = open("../../../Downloads/duplicates.txt", "a", encoding="utf-8")
my_file.write('\n')
my_file.write(str(date.today()) + '.' + str(datetime.now().time())[:2] + '_' + str(LANGUAGE) + '_' + str(REGION))
my_file.write('\n')
my_file.close()

file = 'result_' + str(date.today()) + '.' + str(datetime.now().time())[:2] + '_' + str(LANGUAGE) + '_' + str(REGION)

driver = get_driver()
ban_sites, ban_words, keys, duplicate_sites = info()

with open(file, 'w+', encoding="utf-8") as f:
    for key in keys:
        max = int(SEARCH_DEPTH)
        div_count_pages = int(SEARCH_DEPTH) // 10
        mod_count_pages = int(SEARCH_DEPTH) % 10

        links1 = []
        titles = []
        descriptions = []
        texts = []
        links = []

        for i in range(div_count_pages):
            url = urll(key, i)
            driver.get(url)
            if 'https://yandex.ru/showcaptcha' in driver.current_url:
                captcha()
            time.sleep(2)
            links1 += parse_all(driver)

        if div_count_pages == 0:
            url = urll(key, 0)
            driver.get(url)
            if 'https://yandex.ru/showcaptcha' in driver.current_url:
                captcha()
            links1 += part_parse(driver, mod_count_pages)

        if div_count_pages > 0:
            url = urll(key, div_count_pages + 1)
            driver.get(url)
            if 'https://yandex.ru/showcaptcha' in driver.current_url:
                captcha()
            links1 += part_parse(driver, mod_count_pages)

        for i in range(len(links1)):
            if (not (links1[i] in ban_sites)) and (not (links1[i] in duplicate_sites)):
                links.append(links1[i])

        for link in range(len(links)):
            title, description, text = site_info(driver, links[link])
            banned_links = []
            k = 0
            for word in ban_words:
                if word in text:
                    k += 1
            if k == 0:
                with open('../../../Downloads/duplicates.txt', 'a', encoding="utf-8") as l:
                    l.write(links[link] + '\n')
                    print(1)
                    f.write(title + '\n')
                    f.write(description + '\n')
                    f.write(text + '\n')
                    f.write('\n')
                    print(2)
            else:
                continue
