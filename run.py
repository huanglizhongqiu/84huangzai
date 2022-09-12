"""
Project: 86python
Author:柠檬班-Tricy
Time:2021/12/6 21:33
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
"""
from selenium import webdriver
from common import method  # 导入公共方法
from testdata import data   # 导入测试数据

driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = data.testdate.get("url")
name = data.testdate.get("name")
passwd = data.testdate.get("passwd")
key = data.testdate.get("key")

result = method.exec_search(driver=driver,url=url,name=name,passwd=passwd,key=key)  # 调用函数 接受返回值
# print(result)
if key in result:
    print("搜索结果正确！")
else:
    print("搜索错误")