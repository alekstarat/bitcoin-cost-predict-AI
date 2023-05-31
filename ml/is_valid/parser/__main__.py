import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

URL = 'https://ria.ru/keyword_bitkoin/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0 (Edition Yx GX)',
           'cookie' : '_sp_ses.cf1a=*; cookiePrivacyPreferenceBannerProduction=notApplicable; _ga=GA1.1.1219922994.1685514364; cookiesSettings={"analytics":true,"advertising":true}; _ga_YVVRYGL0E0=GS1.1.1685514363.1.0.1685514374.49.0.0; g_state={"i_p":1685521595146,"i_l":1}; _sp_id.cf1a=fd5809e5-b461-4a94-9108-66554a1621a7.1685514364.1.1685514426.1685514364.17dcd1e1-3c7a-4791-af58-3d94d8d7a0e9'
           }
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get(URL)

links = []
values = []
#driver.find_element(By.LINK_TEXT, 'Еще 20 материалов')

pageSource = driver.execute_script("return document.body.innerHTML;")
print(pageSource)
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(pageSource)
    file.close()

driver.quit()