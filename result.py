import csv

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

file = open('gitafinance.txt', 'r')
code_list = file.read()
code_list = code_list.split('\n')

first_bunki = []
second_bunki = []
third_bunki = []
fourth_bunki = []


def getDataOfParam(param):
    sub_tbody = soup.find("table", attrs={"class": "tb_type1 tb_num tb_type1_ifrs"}).find("tbody")
    sub_title = sub_tbody.find("th", attrs={"class": param}).get_text().strip()

    # param 에 매핑되는 row 검색 => 상위 이동 => 해당 row의 모든 td 컬럼 가져오기
    dataOfParam = sub_tbody.find("th", attrs={"class": param}).parent.find_all("td")
    value_param = [i.get_text().strip() for i in dataOfParam]
    #print(sub_title, " : ", value_param)

    return value_param

for item in code_list:

    first_bunki.append(item)
    second_bunki.append(item)
    third_bunki.append(item)
    fourth_bunki.append(item)

    url = 'https://finance.naver.com/item/main.nhn?code=' + item
    driver = webdriver.Chrome()
    driver.get(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    ParamList = ['매출액', '영업이익', '당기순이익', '영업이익률', '순이익률', 'ROE(지배주주)', '부채비율', '당좌비율', '유보율', 'EPS(원)', 'PER(배)','PBR(배)', 'BPS(원)']

    information = []

    titleLists = soup.select('#middle > div.h_company > div.wrap_company > h2 > a')

    for title in titleLists: #이름
        first_bunki.append(title.get_text())
        second_bunki.append(title.get_text())
        third_bunki.append(title.get_text())
        fourth_bunki.append(title.get_text())

    for idx, pText in enumerate(ParamList):
        param = " ".join(soup.find('strong', text=pText).parent['class'])
        information.append(getDataOfParam(param))

    sub_thead = soup.find("table", attrs={"class":"tb_type1 tb_num tb_type1_ifrs"})
    sub_thead = sub_thead.find("thead").find_all("th", attrs={"scope":"col", "class":""})

    for i in range(len(information)):
        first_bunki.append(information[i][4])

    for i in range(len(information)):
        second_bunki.append(information[i][5])

    for i in range(len(information)):
        third_bunki.append(information[i][6])

    for i in range(len(information)):
        fourth_bunki.append(information[i][7])

    titleLists1 = soup.select('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    titleLists2 = soup.select('#content > div.section.trade_compare > table > tbody > tr:nth-child(4) > td:nth-child(2)')

    for title in titleLists1: #주가
        first_bunki.append(title.get_text())
        second_bunki.append(title.get_text())
        third_bunki.append(title.get_text())
        fourth_bunki.append(title.get_text())

    for title in titleLists2: #시총
        first_bunki.append(title.get_text())
        second_bunki.append(title.get_text())
        third_bunki.append(title.get_text())
        fourth_bunki.append(title.get_text())

first_bunki = [first_bunki[i:i + 17] for i in range(0, len(first_bunki), 17)]
second_bunki = [second_bunki[i:i + 17] for i in range(0, len(second_bunki), 17)]
third_bunki = [third_bunki[i:i + 17] for i in range(0, len(third_bunki), 17)]
fourth_bunki = [fourth_bunki[i:i + 17] for i in range(0, len(fourth_bunki), 17)]

#
# print(first_bunki)
# print(second_bunki)
# print(third_bunki)
# print(fourth_bunki)

with open('01_firstquarter.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(first_bunki)

with open('01_secondquarter.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(second_bunki)

with open('01_thirdquarter.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(third_bunki)

with open('01_fourthquarter.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fourth_bunki)
