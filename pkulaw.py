from browser import browser
from mongodb import mongodb

'''pkulaw
Get pkulaw related data.

@author: FeilyZhang
@date: 2020-11-29 20:26:47
@version: alpha 0.1
@mail: fei@feily.tech
'''
class pkulaw:

    __url = 'https://www.pkulaw.com/'
    __exe_path = 'E:\chromedriver\chromedriver.exe'
    __service_log_path = 'E:\chromedriver\watchlog.log'
    __browser_instance = None
    __SELLP_TIME_SEC = 7
    __rule = '//div[@class="list-title"]/h4/a[starts-with(@href,"/chl/")]'
    __keys = ['title', 'href', 'related-info']
    __mongo = None

    def __init__(self):
        self.__browser_instance = browser(self.__url, self.__exe_path, self.__service_log_path)
        self.__mongo = mongodb()

    def get_laws(self):
        self.execute_common(500, 'XA01')
        return self.__browser_instance.click_and_get(self.__rule, self.__keys, 1, 1, self.__mongo, 'pkulaw', 'law').get_texts_and_attrs()

    def get_rules(self):
        self.execute_common(500, 'XC02')
        return self.__browser_instance.click_and_get(self.__rule, self.__keys, 1, 2, self.__mongo, 'pkulaw', 'rule').get_texts_and_attrs()

    def get_justices(self):
        self.execute_common(500, 'XG04')
        return self.__browser_instance.click_and_get(self.__rule, self.__keys, 1, 3, self.__mongo, 'pkulaw', 'justice').get_texts_and_attrs()

    def get_depts(self):
        self.execute_common(500, 'XE03')
        return self.__browser_instance.click_and_get(self.__rule, self.__keys, 1, 4, self.__mongo, 'pkulaw', 'dept').get_texts_and_attrs()

    def get_parties(self):
        self.execute_common(500, 'XR12')
        return self.__browser_instance.click_and_get(self.__rule, self.__keys, 1, 1, self.__mongo, 'pkulaw', 'party').get_texts_and_attrs()

    def get_groups(self):
        self.execute_common(500, 'XI05')
        return self.__browser_instance.click_and_get(self.__rule, self.__keys, 1, 1, self.__mongo, 'pkulaw', 'group').get_texts_and_attrs()

    def get_industries(self):
        self.execute_common(500, 'XK06')
        return self.__browser_instance.click_and_get(self.__rule, self.__keys, 1, 1, self.__mongo, 'pkulaw', 'industry').get_texts_and_attrs()

    def execute_common(self, scroll_val, group_val):
        self.__browser_instance.clear_texts_and_attrs().refresh()
        self.__browser_instance.find_element('id', 'txtSearch')\
            .send_keys('新冠肺炎').find_element('id', 'btnSearch').click()
        self.__browser_instance.scroll(scroll_val)
        self.__browser_instance.sleep(self.__SELLP_TIME_SEC).find_element(
            'xpath', '//li[@class=" inner level-1"]/a[@cluster_code="' + group_val + '"]'
        ).click()
        self.__browser_instance.sleep(self.__SELLP_TIME_SEC).find_elements(
            'xpath', '//ul[@class="pagination pagination-sm"]/li/a[@style="padding-left:5px;padding-right:5px;font-size: 13px"]'
        )
