
#-*-coding:utf-8-*-

'''网址 http://music.163.com/api/v1/resource/comments/R_SO_4_1348568908?offset=1&total=true&limit=3 '''
import requests
import bs4
import json

def head():
    headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Referer": "https://music.163.com/song?id=4466775",
            "Origin" : "https://music.163.com",
            "Host" : "music.163.com",
            "Accept" : "*/*",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded"
            }
    params = "0gjgMFwkeBkPD/S7sxNcHLTppacTKEN2EjM3F10MzdokeW+4RD1DR0LtIkDcq85MT7rdat5DHEOcEOfueKPjZiDEGo2Kt4MIhiqWsACmRtciNeNMMU7gfx0YYAu00d/760QOmFzGyCw3gtR5wSLCgNb5p94PjFQ1oDraEFAEcGyrWMWn2Hga/e2WS1scJQea"
    encSecKey = "b07f346612fe908f11dedd66b2aa032ef86fdabc7533a4a3a602c9b42efb11fffb6e43f531338fdb9cc658a7ae2dac7789fd64e3b4b9c777eb6630d4c031f39c44ac636d9500e202b234f197ef1937b66e9f35d47951bf8bf9e0af0dcc539287a02e37eb03650dff7d11182c10ccc39e432a4193f738e1bacce7a16758124755"
    data = {
        "params": params,
        "encSecKey": encSecKey
        }
    return headers,data
def parser_url(url,headers,data):

    response = requests.post(url,headers=headers,data = data)
    soup =  bs4.BeautifulSoup(response.text,'html.parser')
    return soup

def parser_html(soup):
    dict_soup = json.loads(soup.text)
    hotComments = dict_soup['hotComments']
    comments = dict_soup['comments']
    return hotComments,comments


def to_file(name,hotComments,comments):
    with open(name+'_Comments.txt','w',encoding='utf-8') as f:
        f.write('hotComments:'+'\n')
        for each in hotComments:
            f.write(each['user']['nickname']+':'+each['content']+'\n')
        f.write('\n'+'comments'+'\n')
        for each in comments:
            f.write(each['user']['nickname']+':'+each['content']+'\n')
    f.close
    print ('歌曲评论下载成功！')
def main():
    print ('Please input name+URL;'+'\n'+'E.g:蜂鸟://music.163.com/#/song?id=1348568908')
    headers,data = head()
    name = input('Song_name:')
    Song_url = input('Song_URL:')
    offset = Song_url.split('=')[1]
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{0}?csrf_token='.format(offset)
    print ('*********************************************************')
    print ('A comment about this song will be generated in this directory, please wait a moment.')
    print ('*********************************************************')
    soup = parser_url(url,headers,data)
    hotComment,comments = parser_html(soup)
    to_file(name,hotComment,comments)

if __name__ == '__main__':
    main()
