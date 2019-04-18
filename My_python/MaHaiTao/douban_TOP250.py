#-*-coding:utf-8-*-

import requests
import bs4

def url_parser(url):
    print (url)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    response = requests.get(url,headers)
    soup = bs4.BeautifulSoup(response.text.replace('<br>','').strip(),'html.parser')
    return soup
    
def parser_content(soups):
    soups_rangking = soups.find_all('em',class_='')
    soups_name = soups.find_all('div',class_='hd')
    soups_source = soups.find_all('span',class_='rating_num')
    soups_actor = soups.find_all('p',class_='')
    return soups_rangking,soups_name,soups_source,soups_actor

def text_parser(result):
    rangking = []
    name = []
    source = []
    actor = []
    lists = ''
    for each in result[0]:
        rangking.append(each.text)
    for each in result[1]:
        name.append(each.a.span.text)
    for each in result[2]:
        source.append(each.text)
    for each in result[3]:
        actor.append(each.text)
    
    for i in range(0,25):
        add = rangking[i]+name[i]+source[i]+actor[i]
        lists += add
    write_content_file(lists)

def write_content_file(content):
    with open('top250.txt','a',encoding="utf-8") as f:
        f.write(content)
        f.close()
def main():
    for i in range(0,10):
        url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
        soups = url_parser(url)
        parser_content_result = parser_content(soups)
        text_parser(parser_content_result)
if __name__=='__main__':
    main()
