"""
Project: 86python
Author:柠檬班-Tricy
Time:2021/12/6 21:32
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
"""
import time
from selenium.webdriver.common.by import By
def exec_search(driver,url,name,passwd,key):
    driver.get(url)
    driver.find_element(By.ID,"username").send_keys(name)
    driver.find_element(By.ID,'password').send_keys(passwd)
    driver.find_element(By.ID,"btnSubmit").click()
    username = driver.find_element(By.XPATH,'//p').text  # 获取文本
    driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
    id = driver.find_element(By.XPATH,'//div[text()="零售出库"]/..').get_attribute("id") # 获取ID属性
    frame_id = id + '-frame'  # 得到iframe id
    driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="{}"]'.format(frame_id)))  # 通过id进行 iframe的子页面的切换
    driver.find_element(By.ID,"searchNumber").send_keys(key)  # 对子页面的元素进行操作了
    driver.find_element(By.ID,'searchBtn').click()
    time.sleep(0.1) # 强制等待辅助
    text = driver.find_element(By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text # 获取值
    return  text  # 返回文本