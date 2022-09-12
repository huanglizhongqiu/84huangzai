"""
============================
Project: Python-class
Author:柠檬班-dd
Time:2022/9/9 20:36
E-mail:1161340814@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

# import selenium
# from selenium import webdriver
# import time
# diver=webdriver.Chrome()
# diver.get("https://baidu.com")
# diver.maximize_window()
# diver.get("https://taobao.com")
# time.sleep(2)
# diver.back()
# time.sleep(2)
# diver.forward()
# time.sleep(2)
# diver.refresh()
# diver.close()
# diver.quit()
# title=diver.title
# print(title)


import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
diver=webdriver.Chrome()
diver.implicitly_wait(10)
diver.get("http://erp.lemfix.com/login.html")
diver.find_element(By.ID,"username").send_keys("test123")
diver.find_element(By.ID,"password").send_keys("123456")
diver.find_element(By.ID,"btnSubmit").click()
# time.sleep(2)
# uname=diver.find_element(By.XPATH,"//p").text
# print(uname)
diver.find_element(By.XPATH,"//span[text()='零售出库']").click()
time.sleep(2)
id=diver.find_element(By.XPATH,"//div[text()='零售出库']/..").get_attribute("id")
iframe_id=id +"-frame"
diver.switch_to.frame(diver.find_element(By.XPATH,"//iframe[@id='{}']".format(iframe_id)))
# diver.switch_to.frame(iframe_id)
# diver.find_element(By.ID,"searchNumber").send_keys("308")
diver.find_element(By.XPATH,"//input[@id='searchNumber']").send_keys("308")
diver.find_element(By.XPATH,"//span[text()='查询']").click()
time.sleep(2)
num=diver.find_element(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
print(num)
if "308" in num:
    print("搜索结果正确")
else:
    print("搜索结果错误")

