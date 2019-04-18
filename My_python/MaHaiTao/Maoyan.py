import requests
import re
import json
from multiprocessing import Pool

def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else :
        return None

def write_to_file(content):
    with open('猫眼电影.txt','a') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def parse_page(html):
    pattern = re.compile('.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
                'index':item[0],
                'image':item[1],
                'title':item[2],
                'actor':item[3].strip()[3:],
                'time':item[4].strip()[5:],
                'source':item[5]+item[6]
                }
    return item

def main():
    for offset in range(10):
        url = 'https://maoyan.com/board/4?offset='+str(offset*10)
        html = get_page(url)
        items = parse_page(html)
        for item in parse_page(html):
            print (item)
            write_to_file(item)

if __name__ == '__main__':
    main()
