# -*- coding: utf8 -*-
# import csv
import os
# import pickle
import sys
import time
# import multiprocessing
from selenium import webdriver
from tqdm import tqdm
# import sqlite3


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def info_collect(browser, url):
    browser.get(url)
    time.sleep(1)
    category = ""
    categorys = browser.find_elements_by_xpath("//div[@class='breadcrumbs  mb-20']/ul/li/a")
    for position in range(1, len(categorys)):
        category += categorys[position].text
        if position + 1 != len(categorys):
            category += " > "

    # print(category)
    name = browser.find_element_by_xpath("//div[@class='container']//h1").text
    # print(name)
    # time.sleep(1000)
    description = browser.find_element_by_xpath("//div[@itemprop='description']").text
    description = str(description).replace(";", " ")

    articul = browser.find_element_by_xpath("//span[@data-action='article']").text
    price = browser.find_element_by_xpath("//span[@class='offer-tools__price_num-strong']").text

    barcode = browser.find_element_by_xpath("//div[@class='offer-instruction__row']").text
    if "Штрих" in barcode:
        barcode = str(barcode).replace("Штрих-код: ", "")
        barcode = barcode.replace(", -", "")
        barcode = barcode.replace("-, *", "")
        description = description.replace("Штрих-код и вес", "").replace("Штрих-код:", "").replace(barcode, "").replace("-, *", "")


    else:
        barcode = ""

    # description = (browser.find_element_by_xpath("//div[@itemprop='description']").get_attribute('innerHTML'))
    brand = "-"
    try:
        all_a_href = browser.find_elements_by_xpath("//div[@class='description__item mb-4']//a[@href]")
        for a_href in all_a_href:
            href = a_href.get_attribute("href")

            if "brand" in href:
                # print(href)
                brand = a_href.text
    except:
        brand = "-"
    # print(brand)


    photos_text = ""
    photots = browser.find_elements_by_xpath("//div[@class='gallery__main']//img[@class='img-fluid']")
    for photo in photots:
        src = (photo.get_attribute("src"))
        photos_text += src + ", "
    photos_text = photos_text[:-2]

    try:
        srok_godnosti = browser.find_element_by_xpath("//p[@data-show-offer]/span").text
    except:
        srok_godnosti = "-"
    # print(srok_godnosti)


    try:
        ulovia_hranenia = browser.find_element_by_xpath("//div[@id='instruction_CONDITIONS']/div").text
        # print(ulovia_hranenia)
        description = description.replace(ulovia_hranenia, "").replace("Условия хранения", "")
        ulovia_hranenia = ulovia_hranenia.replace("\n", "<br>").replace("\r", "\\r").replace(";", " ")
        # print("\n\n\n")
        # print(description)
    except:
        ulovia_hranenia = "-"
    # ulovia_hranenia = ""
    # print(ulovia_hranenia)

    try:
        sostav = str(browser.find_element_by_xpath("//div[@id='instruction_COMPOSITION']/div").text).replace(";", " ")
        # print(sostav)
        test_sostav = str(sostav).split("\n")
        for line in test_sostav:

            if len(line) > 0:
                # print((line))
                # print("____________________")
                description = description.replace(line, "")
        description = description.replace(sostav, "").replace("Состав", "")
        # description = description.replace("\n\n\n\n", "\n\n")
        sostav = sostav.replace("\n", "<br>").replace("\r", "\\r").replace(";", " ")

        # print("\n\n\n")
        # print(description)
    except:
        sostav = "-"

    try:
        proisvoditel = browser.find_element_by_xpath("//div[@id='instruction_MANUFACTURER']/div").text
        # print(proisvoditel)
        description = description.replace(proisvoditel, "").replace("Производитель", "")
        proisvoditel = proisvoditel.replace("\n", "<br>").replace("\r", "\\r").replace(";", " ")
        # print("\n\n\n")
        # print(description)
    except:
        proisvoditel = "-"

    try:
        lek_forma = browser.find_element_by_xpath("//div[@id='instruction_drug_form']/div").text
        # print(lek_forma)
        description = description.replace(lek_forma, "").replace("Лекарственная форма", "")
        lek_forma = lek_forma.replace("\n", "<br>").replace("\r", "\\r").replace(";", " ")
        # print("\n\n\n")
        # print(description)
    except:
        lek_forma = "-"

    try:
        ulovia_otpuska = browser.find_element_by_xpath("//div[@id='instruction_IS_RECIPE']/div").text
        # print(ulovia_otpuska)
        description = description.replace(ulovia_otpuska, "").replace("Условия отпуска из аптек", "")
        ulovia_otpuska = ulovia_otpuska.replace("\n", "<br>").replace("\r", "\\r").replace(";", " ")
        # print("\n\n\n")
        # print(description)
    except:
        ulovia_otpuska = "-"

    # with open("test.txt", 'a', encoding='utf-8') as fl:
    #     fl.write(category)
    #     fl.write("\n")
    #

    description = (description.replace("\n", "<br>").replace("\r", "\\r"))
    while True:
        try:
            with open("test.csv", 'a', encoding='utf-8') as csv_fl:
                csv_fl.write(
                    f""";;{articul};{name};1;0;visible;;{description};;;taxable;;1;;;0;0;;;;;0;;;{price};{category};;;{photos_text};;;;;;;;;0;Производитель;{proisvoditel};1;0;Бренд;{brand};1;0;Срок годности;{srok_godnosti};1;0;Состав;{sostav};1;0;Условия хранения;{ulovia_hranenia};1;0;Лекарственная форма;{lek_forma};1;0;Условия отпуска из аптек;{ulovia_otpuska};1;0;Штрих-код:;{barcode};1;0\n""")
                break
        except:
            pass


def main(urls_list):
    try:
        option = webdriver.ChromeOptions()
        #
        # option.add_argument("user-agent=" + fake_useragent.UserAgent().random)
        option.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.579 Yowser/2.5 Safari/537.36")

        directery = os.getcwd()
        option.add_argument("--log-level=OFF")
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
        option.add_argument("--log-level=3")
        browser = webdriver.Chrome(
            executable_path=resource_path('chromedriver.exe'),  # C:\\Users\\Ivan\\PycharmProjects\\1688Parser\\
            options=option
        )

        for url in tqdm(urls_list, desc=f"Сбор данных"):
            url = (str(url).replace("('", "").replace("',)", ""))
            info_collect(browser, url)


        #     csv_fl.write("""ID,Тип,Артикул,Имя,Опубликован,рекомендуемый?,"Видимость в каталоге","Краткое описание",Описание,"Дата начала действия продажной цены","Дата окончания действия продажной цены","Статус налога","Налоговый класс","В наличии?",Запасы,"Величина малых запасов","Возможен ли предзаказ?","Продано индивидуально?","Вес (kg)","Длина (cm)","Ширина (cm)","Высота (cm)","Разрешить отзывы от клиентов?","Примечание к покупке","Цена распродажи","Базовая цена",Категории,Метки,"Класс доставки",Изображения,"Лимит загрузок","Число дней до просроченной загрузки",Родительский,"Сгруппированные товары",Апсейл,Кросселы,"Внешний URL","Текст кнопки",Позиция,"Имя атрибута 1","Значение(-я) аттрибута(-ов) 1","Видимость атрибута 1","Глобальный атрибут 1","Имя атрибута 2","Значение(-я) аттрибута(-ов) 2","Видимость атрибута 2","Глобальный атрибут 2","Имя атрибута 3","Значение(-я) аттрибута(-ов) 3","Видимость атрибута 3","Глобальный атрибут 3","Имя атрибута 4","Значение(-я) аттрибута(-ов) 4","Видимость атрибута 4","Глобальный атрибут 4","Имя атрибута 5","Значение(-я) аттрибута(-ов) 5","Видимость атрибута 5","Глобальный атрибут 5","Имя атрибута 6","Значение(-я) аттрибута(-ов) 6","Видимость атрибута 6","Глобальный атрибут 6"
        # """)
    except Exception as ex:
        print(ex)
        print(url)
        pass

    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':
    url_list = ["https://www.eapteka.ru/goods/id506784/", "https://www.eapteka.ru/goods/id350729/", "https://www.eapteka.ru/goods/id272583/"]
    main(url_list)

