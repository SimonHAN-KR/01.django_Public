from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote_plus

import time

file = open('gitafinance.txt', 'r')
code_list = file.read()
code_list = code_list.split('\n')
juga_data = []
sichong_data = []

for item in code_list:
    url = 'https://finance.naver.com/item/main.nhn?code=' + item
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    titleLists1 = soup.select('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    titleLists2 = soup.select('#content > div.section.trade_compare > table > tbody > tr:nth-child(4) > td:nth-child(2)')

    for title in titleLists1:
        juga_data.append(title.get_text())

    for title in titleLists2:
        sichong_data.append(title.get_text())

print(sichong_data)
print(juga_data)


# for title in titleLists:
#     print(title.get('title') + " : " +title.get('href'))
#     print('----------------------------------------------')

# time.sleep(10)
# driver.close()