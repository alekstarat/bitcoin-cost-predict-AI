import requests
from bs4 import BeautifulSoup
import pandas as pd


links = ['https://ria.ru/services/keyword_bitkoin/more.html?id=1560185063&date=20191024T175435',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1589599661&date=20201217T010159',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1591898120&date=20210103T152508',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1596536612&date=20210208T161033',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1598784610&date=20210225T080000',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1728805437&date=20210418T132242',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1736315030&date=20210609T153506',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1746291542&date=20210819T011600',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1758985906&date=20211114T130647',
         'https://ria.ru/services/keyword_bitkoin/more.html?id=1775499710&date=20220228T103257']
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0 (Edition Yx GX)',
           'cookie' : '_sp_ses.cf1a=*; cookiePrivacyPreferenceBannerProduction=notApplicable; _ga=GA1.1.1219922994.1685514364; cookiesSettings={"analytics":true,"advertising":true}; _ga_YVVRYGL0E0=GS1.1.1685514363.1.0.1685514374.49.0.0; g_state={"i_p":1685521595146,"i_l":1}; _sp_id.cf1a=fd5809e5-b461-4a94-9108-66554a1621a7.1685514364.1.1685514426.1685514364.17dcd1e1-3c7a-4791-af58-3d94d8d7a0e9'
           }

all_href = []
all_data = []

for link in links:

    a = requests.get(url=link, headers=headers).text
    soup = BeautifulSoup(a, 'lxml')
    temp = soup.find_all('a', class_='list-item__title color-font-hover-only')
    for i in temp:
        all_href.append(i.get('href'))
        all_data.append(i.text)
df = pd.DataFrame(columns=['href', 'data'])
df['href'] = all_href
df['data'] = all_data
print(df)
df.to_excel('output.xlsx')