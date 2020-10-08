#encoding:utf-8

'''
REQ_01需求对应测试用例
创建日期：2018/9/12
'''

import unittest
from time import sleep
from findmethod import findmethod
import testutil
import verify
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class baidu(testutil.MyTest):
    '''百度搜索测试'''
    def test_baidu_search(self):
        '''百度搜索设置'''
        self.driver.get("https://www.baidu.com")  #打开百度主页
        setUp = findmethod(self,"link_text",u"设置")
        ActionChains(self.driver).move_to_element(setUp).perform()  #鼠标悬浮设置
        search = findmethod(self,"link_text",u"搜索设置")
        search.click()  #点击搜索设置
        sleep(1)
        select = findmethod(self,"id","nr")
        select.click()
        sleep(1)
        Select(select).select_by_visible_text("每页显示20条")  #选择每页显示20条
        save = findmethod(self,"link_text",u"保存设置")
        save.click()  #点击保存设置
        alert = self.driver.switch_to_alert().text
        a = verify.verify(self.driver,alert,u"已经记录下您的使用偏")
        sleep(5)
        print(a)
        # self.assertEqual(u"已经记录下您的使用偏好",alert)
        self.driver.switch_to_alert().accept()
        sleep(3)

        # findmethod(self,"id","kw").send_keys(u"中油瑞飞")
        # sleep(3)
        #
        # u = self.driver.find_element_by_id('20')
        # print(u)
        #
        # count = findmethod(self,"id","20")
        # print(count)
        # count1 = findmethod(self,"id","21")
        # print(count1)
        # if count!='False' and count1=='False':
        #     print(u"搜索结果为20条！")
        # else:
        #     print(u"搜索结果不为20条！")









if __name__ == '__main__':
    unittest.main()



