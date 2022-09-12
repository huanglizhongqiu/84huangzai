"""
============================
Project: Python-class
Author:柠檬班-dd
Time:2022/9/12 17:51
E-mail:1161340814@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://erp.lemfix.com/login.html")
driver.find_element(By.ID,"username").send_keys("test123")
driver.find_element(By.ID,"password").send_keys("123456")
driver.find_element(By.ID,"btnSubmit").click()
driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
time.sleep(2)
id=driver.find_element(By.XPATH,"//div[text()='零售出库']/..").get_attribute("id")
iframe_id=id+"-frame"
# driver.switch_to.frame(iframe_id)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='{}']".format(iframe_id)))
driver.find_element(By.ID,"searchNumber").send_keys("308")
driver.find_element(By.XPATH,"//span[text()='查询']").click()
time.sleep(2)
num=driver.find_element(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
print(num)
if "308" in num:
    print("搜索结果正确")