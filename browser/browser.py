from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from time import sleep

'''browser
Automatic browser instance, simulate the real browser request process.

@author: FeilyZhang
@date: 2020-11-29 02:26:35
@version: alpha 0.1
@mail: fei@feily.tech
'''
class browser:

    __url = ''
    __exe_path = ''
    __log_path = ''
    __browser_element = None
    __browser_elements = None
    __browser_instance = None
    __texts_and_attrs = []
    __instance = None

    def __init__(self, url, exe_path, log_path):
        self.__url = url
        self.__exe_path = exe_path
        self.__log_path = log_path
        self.__browser_instance = self.__get_instance()

    def __get_instance(self):
        instance = webdriver.Chrome(
            executable_path = self.__exe_path, service_log_path = self.__log_path
        )
        self.__instance = instance
        instance.get(self.__url)
        return instance

    def find_element(self, by, id_cls_xpath_name):
        if by == 'id':
            self.__browser_element = self.__browser_instance.find_element_by_id(id_cls_xpath_name)
        elif by == 'cls':
            self.__browser_element = self.__browser_instance.find_element_by_class_name(id_cls_xpath_name)
        elif by == 'xpath':
            self.__browser_element = self.__browser_instance.find_element_by_xpath(id_cls_xpath_name)
        elif by == 'name':
            self.__browser_element = self.__browser_instance.find_element_by_name(id_cls_xpath_name)
        return self

    def find_elements(self, by, id_cls_xpath_name):
        if by == 'id':
            self.__browser_elements = self.__browser_instance.find_elements_by_id(id_cls_xpath_name)
        elif by == 'cls':
            self.__browser_elements = self.__browser_instance.find_elements_by_class_name(id_cls_xpath_name)
        elif by == 'xpath':
            self.__browser_elements = self.__browser_instance.find_elements_by_xpath(id_cls_xpath_name)
        elif by == 'name':
            self.__browser_elements = self.__browser_instance.find_elements_by_name(id_cls_xpath_name)
        return self

    def click(self):
        self.__browser_element.click()
        return self

    def clickAll(self):
        for ele in self.__browser_elements:
            ele.click()
        return

    def click_and_get(self, rule, key: list, start, page_num, mongo, db, col):
        self.__texts_and_attrs.clear()
        if col == 'dept':
            rul = ['//div[@style="width:45px;margin-right:10px"]', '//dl[@prop="TokenNum"]/dd[@filter_value="100"]']
            self.action('xpath', rul).sleep(3)
        for i in range(start, page_num + 1):
            print(i)
            self.find_element('name', 'jumpToNum').clear().sleep(3)
            self.find_element('name', 'jumpToNum').send_keys(i).sleep(3)
            if (col == 'dept'):
                self.find_element('cls', 'jumpBtn').click().sleep(5)
            else:
                self.find_element('cls', 'jumpBtn').click().sleep(5)
            self.find_elements('xpath', rule)
            for ele in self.__browser_elements:
                dic = {
                    key[0] : ele.text,
                    key[1] : ele.get_attribute(key[1])
                }
                #if mongo.is_exist(db, col, dic) == False:
                # mongo.insert_one(db, col, dic)
                self.__texts_and_attrs.append(dic)
        mongo.insert_all(db, col, self.get_texts_and_attrs())
        #self.__texts_and_attrs = self.__texts_and_attrs[10 : len(self.__texts_and_attrs)]
        #self.find_element('id', 'btnhulue').click()
        return self

    def get_elements(self):
        return self.__browser_elements

    def send_keys(self, keyword):
        self.__browser_element.send_keys(keyword)
        return self

    def sleep(self, sleep_time):
        sleep(sleep_time)
        return self

    def refresh(self):
        self.__browser_instance.refresh()
        return self

    def scroll(self, val):
        self.__browser_instance.execute_script('document.documentElement.scrollTop=' + str(val))
        return self

    def get_text_all(self, key):
        if len(self.__texts_and_attrs) == 0:
            for ele in self.__browser_elements:
                self.__texts_and_attrs.append({
                    key : ele.text
                })
        else:
            for i in range(0, len(self.__texts_and_attrs)):
                self.__texts_and_attrs[i][key] = self.__browser_elements[i].text
        return self

    def get_attribute_all(self, attr, key):
        if len(self.__texts_and_attrs) == 0:
            for ele in self.__browser_elements:
                self.__texts_and_attrs.append({
                    key : ele.get_attribute(attr)
                })
        else:
            for i in range(0, len(self.__texts_and_attrs)):
                self.__texts_and_attrs[i][key] = self.__browser_elements[i].get_attribute(attr)
        return self

    def clear_texts_and_attrs(self):
        self.__texts_and_attrs.clear()
        return self

    def get_texts_and_attrs(self):
        return self.__texts_and_attrs

    def get_browser(self):
        return self

    def clear(self):
        self.__browser_element.clear()
        return self

    def get_pg_source(self):
        return self.__browser_instance.page_source

    def action(self, xpath, rule):
        ActionChains(self.__instance).move_to_element(self.__instance.find_element_by_xpath(rule[0])).perform()
        self.sleep(2)
        dat_click = WebDriverWait(self.__instance, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, rule[1]))
        )
        self.sleep(2)
        dat_click.click()
        return self