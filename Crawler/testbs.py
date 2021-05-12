import requests
import time
from bs4 import BeautifulSoup

URL_PATH = 'E:/vs/URLN_T.txt'
TITLE_PATH = 'E:/vs/TITLE_T.txt'
FILE_PATH = 'E:/vs/TTBT_new_T.txt'

# 首先我们写好抓取网页的函数


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "


def get_content(url):
    '''
    分析贴吧的网页文件，整理信息，保存在列表变量中
    '''
    print('getting content')
    # 初始化一个列表来保存所有的帖子信息：
    comments = []
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)
    # 我们来做一锅汤
    soup = BeautifulSoup(html, 'lxml')

    # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    divTags = soup.find_all('div', attrs={'class': 'd_post_content_main'})
    #(divTags)
    for li in divTags:
        # 初始化一个字典来存储文章信息
        #print(li)
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        try:
            # 开始筛选信息，并保存到字典中
            comment['lou'] = li.find('div', attrs={'class': 'd_post_content j_d_post_content clearfix'}).text
            comments.append(comment)
            print(comment['lou'])
        except:
            print('小问题')

        # try:
        #     comment['lzl_w'] = li.find('span', attrs={'class': 'lzl_content_main'}).text
        #
        #     print(comment['lzl_w'])
        # except:
        #     print('没有楼中楼')

    return comments


def get_url(url):
    '''
    分析贴吧的网页文件，整理信息，保存在列表变量中
    '''

    # 初始化一个列表来保存所有的帖子信息：
    comments = []
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)
    # 我们来做一锅汤
    soup = BeautifulSoup(html, 'lxml')

    # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    liTags = soup.find_all('li', attrs={'class': 'j_thread_list clearfix thread_item_box'})

    # 通过循环找到每个帖子里的我们需要的信息：
    for li in liTags:
        # 初始化一个字典来存储文章信息
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        try:
            # 开始筛选信息，并保存到字典中
            comment['title'] = li.find(
                'a', attrs={'class': 'j_th_tit'}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + \
                              li.find('a', attrs={'class': 'j_th_tit'})['href']
            comments.append(comment)
            #print(comment)
        except:
            print('出了点小问题')


    return comments


def replace_utf8mb4(v):
        """Replace 4-byte unicode characters by REPLACEMENT CHARACTER"""
        import re
        INVALID_UTF8_RE = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
        INVALID_UTF8_RE.sub(u'\uFFFD', v)


def Out2URL(dict, url_list_2, title):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。

    '''
    with open(URL_PATH, 'a+', encoding='utf-8') as f:
        for comment in dict:
            f.write('{}\n'.format(
                comment['link'],
                encoding='utf-8'))
            url_list_2.append(comment['link'])
            title.append(comment['title'])
        print('当前页面爬取完成')
    with open(TITLE_PATH, 'a+', encoding='utf-8') as f:
        for comment in dict:
            f.write('{}\n'.format(
                comment['title'], encoding='utf-8'))


def Out2File(dict, t):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。

    '''
    with open(FILE_PATH, 'a+', encoding='utf-8') as f:
        for comment in dict:
            f.write('{}  | {}\n'.format(
                 t, comment['lou'],
                encoding='utf-8'))
        print('当前页面爬取完成')


def main(base_url, deep):
    url_list = []
    url_list_2 = []
    title = []
    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    # for url in url_list:
    #     content = get_url(url)
    #     Out2URL(content, url_list_2, title)
    # print('链接获取完成！')
    for line in open(URL_PATH):
        line2 = line[0:-1]
        url_list_2.append(line2)

    for line in open(TITLE_PATH, encoding='utf-8'):
        line2 = line[0:-1]
        title.append(line2)

    print(title)
    print(url_list_2)
    for url, t in zip(url_list_2, title):
        print(url)
        print(t)
        content = get_content(url)
        Out2File(content, t)
        time.sleep(1)
    print('所有的信息都已经保存完毕！')


base_url = 'https://tieba.baidu.com/f?kw=清华大学&ie=utf-8'
# 设置需要爬取的页码数量
deep = 3

if __name__ == '__main__':
    main(base_url, deep)