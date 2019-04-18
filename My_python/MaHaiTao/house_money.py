#-*-coding:utf-8-*-

import requests
import bs4
import openpyxl

def parser_url(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    response = requests.get(url,headers=headers)
    soup = bs4.BeautifulSoup(response.text.replace('[','').replace(']',''),'html.parser')
    return soup

def parser_soup(soup):
    target  = soup.find_all('p',style='TEXT-INDENT: 2em')
    city = []
    house_price = []
    money = []
    proportion = []
    result = []
    a = []

    for i in range(0,37*5,5):
        city.append(target[9+i].text)
    for i in range(0,37*5,5):
        house_price.append(target[10+i].text)
    for i in range(0,37*5,5):
        money.append(target[11+i].text)
    for i in range(0,37*5,5):
        proportion.append(target[12+i].text)

    for i in range(0,36):
        result.append(city[i])
        result.append(house_price[i])
        result.append(money[i])
        result.append(proportion[i])
        a.append(result)
        result = []
    return a
def write_file(content):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['city','house_price','acerage_salary','proportion'])
    for each in content:
        ws.append(each)
    wb.save('房价比.xlsx')
    print ('生成文件成功！')

def main():
    url = 'http://news.house.qq.com/a/20170702/003985.htm'
    soup = parser_url(url)
    content = parser_soup(soup)
    write_file(content)

if __name__ == '__main__':
    main()
