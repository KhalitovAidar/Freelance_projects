import math
import os
# import pickle
import random
import sys
import time
import multiprocessing
from selenium import webdriver
from tqdm import tqdm
import sqlite3



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


option = webdriver.ChromeOptions()
#
# option.add_argument("user-agent=" + fake_useragent.UserAgent().random)
option.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.579 Yowser/2.5 Safari/537.36")

directery = os.getcwd()

option.add_experimental_option('prefs', {
    "download.default_directory": directery,
    # Change default directory for downloads
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
})
# option.add_argument("--log-level=OFF")
option.add_argument("--log-level=3")
# disable webdriver
option.add_argument("--disable-blink-features=AutomationControlled")

# headless mod
option.add_argument("--headless")

browser = webdriver.Chrome(
    executable_path=resource_path('chromedriver.exe'),  # C:\\Users\\Ivan\\PycharmProjects\\1688Parser\\
    options=option
)



# def create_cursor(conn):
#
#     cursor = conn.cursor()
#
#     # Создание таблицы
#     try:
#         cursor.execute("""CREATE TABLE all_urls
#                           (url text)
#                        """)
#         conn.commit()
#
#     except sqlite3.OperationalError:
#         pass
#
#     return cursor


def insert_url_in_db(url):
    while True:
        try:
            conn = sqlite3.connect(resource_path("urls.db"), timeout=10)

            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO all_urls VALUES ('{url}')")
            conn.commit()
            conn.close()
            break
        except sqlite3.Error as ex:
            # print("---------")
            # print(ex)
            # print("DB error")
            # print("_________")
            time.sleep(random.random())


def main_urls_collect():
    url = "https://www.eapteka.ru/"
    browser.get(url)
    time.sleep(1)
    browser.get(url)
    categories = browser.find_elements_by_xpath("//li[@class='header__nav-item ']/a")
    main_cat_urls = []
    for elem in categories:
        href = elem.get_attribute("href")
        main_cat_urls.append(href)
    return main_cat_urls


def sub_url_collect(url):
    browser.get(url)
    sub_categorys = browser.find_elements_by_xpath("//div[@class='filter__links']/ul/li/a")
    sub_cat_urls = []
    for elem in sub_categorys:
        href = elem.get_attribute("href")
        # print(href)
        sub_cat_urls.append(href)
    return sub_cat_urls


def item_urls_collect(url_list):
    # try:
        # print(spec_dict)
        # cursor = spec_dict["cursor"]
        # url = spec_dict["url"]
    # print(url_list)
    try:
        option = webdriver.ChromeOptions()
        #
        # option.add_argument("user-agent=" + fake_useragent.UserAgent().random)
        option.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.579 Yowser/2.5 Safari/537.36")

        directery = os.getcwd()

        option.add_experimental_option('prefs', {
            "download.default_directory": directery,
            # Change default directory for downloads
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
        })

        # disable webdriver
        option.add_argument("--disable-blink-features=AutomationControlled")

        # headless mod
        option.add_argument("--headless")

        browser = webdriver.Chrome(
            executable_path=resource_path('chromedriver.exe'),  # C:\\Users\\Ivan\\PycharmProjects\\1688Parser\\
            options=option
        )

        for url in tqdm(url_list, desc=f"{multiprocessing.current_process().name}"):
            url += "?PAGEN_1="
            urls_list = []
            for i in range(1, 100):
                new_url = url + str(i)

                while True:
                    try:
                        # print(new_url)
                        browser.get(new_url)
                        break
                    except Exception as ex:

                        pass
                elements = browser.find_elements_by_xpath(
                    "//div[@class='cc-item--group ']/section//a[@class='cc-item--img-link mb-2']")
                if len(elements) > 0:
                    for elem in elements:
                        item_href = (elem.get_attribute("href"))
                        insert_url_in_db(item_href)
                        # urls_list.append(item_href)
                else:
                    break

            conn = sqlite3.connect(resource_path("urls.db"), timeout=10)

            cursor = conn.cursor()

            sql = "SELECT * FROM all_urls"
            cursor.execute(sql)
            srt_list = (cursor.fetchall())  # or use fetchone()
            print(f"Длинна списка: {len(srt_list)}")

    except Exception as ex:
        print(ex)
        print(url)
        pass

    finally:
        browser.close()
        browser.quit()


def main():
    multiprocessing.freeze_support()
    try:

        conn = sqlite3.connect(resource_path("urls.db"), timeout=10)

        cursor = conn.cursor()

        cursor.execute("""DROP TABLE IF EXISTS all_urls;""")
        conn.commit()

        # Создание таблицы
        try:
            cursor.execute("""CREATE TABLE all_urls
                                 (url text)
                              """)
            conn.commit()

        except sqlite3.OperationalError:
            pass

        sql_qr = """DELETE from all_urls"""
        cursor.execute(sql_qr)
        conn.commit()

        sql = "SELECT * FROM all_urls"
        cursor.execute(sql)
        srt_list = (cursor.fetchall())  # or use fetchone()
        print(srt_list)

        conn.close()

        print("Собираю мейн-категории")
        main_cat_urls = main_urls_collect()
        print("Собрал мейн-категории")

        sub_cat_urls = []


        for main_cat_url in tqdm(main_cat_urls, desc='Собираю данные о sub-категориях'):

            for elem in sub_url_collect(main_cat_url):
                # print(elem)
                sub_cat_urls.append(elem)

        def func_chunks_generators(lst, c_num):
            n = math.ceil(len(lst) / c_num)

            for x in range(0, len(lst), n):
                e_c = lst[x: n + x]

                if len(e_c) < n:
                    e_c = e_c + [None for y in range(n - len(e_c))]
                yield e_c

        process_count = multiprocessing.cpu_count()
        process_count = int(process_count/1.5)

        big_sub_cat_urls = func_chunks_generators(sub_cat_urls, process_count)

        print(f"Будет запущено {process_count} процессов")
        with multiprocessing.Pool(process_count) as p1:  # в нескольких процессах собираю инфу о н товарах
            with tqdm(desc='Собираю ссылки на товары') as pbar1:
                for i, _ in enumerate(p1.imap_unordered(item_urls_collect, big_sub_cat_urls)):
                    pbar1.update()

        print("end")

    except Exception as ex:
        # print(ex)
        time.sleep(10)

    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()