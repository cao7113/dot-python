#encoding:utf-8

'''屏幕截图函数
创建日期：2018/9/12
'''

from selenium import webdriver
import os

def snapshot(driver):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    file_path = base_dir + "/common/image/" + "bug.png"
    print(file_path)
    driver.get_screenshot_as_file(file_path)

def verify(driver,result,expectedresult):
    #driver = webdriver.Chrome()
    try:
        if(result == expectedresult):
            return True
        else:
            snapshot(driver)
            return False
    except Exception as e:
        print(e.message)

if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    verify(driver, "1","2")
    driver.quit()

