import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import re
from mongodb import mongodb

'''parsing
Request and parse HTML.

@author: FeilyZhang
@date: 2020-11-29 21:10:39
@version: alpha 0.1
@mail: fei@feily.tech
'''
class parsing:

    __headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0'
    }

    __html = ''
    __ele = None

    def get_html(self, ele):
        self.__ele = ele
        session = requests.Session()
        retry = Retry(connect = 3, backoff_factor = 0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('https://', adapter)
        self.__html = session.get(url = ele['href'], headers = self.__headers).text
        return self

    def get_json(self, mongo, db, col):
        #dept = re.findall(r'<strong>发布部门：</strong>.*?<span title="(.*?)">', self.__html, re.S|re.M)word_num = re.findall(r'<li  title="(.*?)"><strong>发文字号：</strong>', self.__html, re.S|re.M)
        #pub_date = re.findall(r'<strong>发文字号：</strong>.*?<li  title="(.*?)"><strong>发布日期：</strong>', self.__html, re.S|re.M)
        #exe_date = re.findall(r'<strong>发布日期：</strong>.*?<li  title="(.*?)"><strong>实施日期：</strong>', self.__html, re.S|re.M)
        title = re.findall(r'<li  title="(.*?)">', self.__html, re.S|re.M)
        timeliness = re.findall(r'<strong>时效性：</strong>.*?<span title="(.*?)">', self.__html, re.S|re.M)
        level = re.findall(r'<strong>效力级别：</strong>.*?<span title="(.*?)">', self.__html, re.S|re.M)
        type = re.findall(r'<span title="(.*?)">', self.__html, re.S|re.M)
        content = re.findall(r'<div class="zhang" id="div_fulltext_start">(.*?)<div class="fb-info fb-info-code">', self.__html, re.S|re.M)
        dept = type[0 : type.index(timeliness[0])]
        type = type[type.index(level[0]) + 1 : ]
        dic = {
            'title' : self.__ele['title'],
            'dept' : dept,
            'word_num' : title[0] if len(title) == 3 else '',
            'pub_date' : title[1] if len(title) == 3 else '',
            'exe_date' : title[2] if len(title) == 3 else '',
            'timeliness' : timeliness,
            'level' : level,
            'type' : type,
            'content' : content
        }
        mongo.insert_one(db, col, dic)
        return dic
