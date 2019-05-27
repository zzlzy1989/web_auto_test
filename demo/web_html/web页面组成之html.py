'''

'''

"""
selenium代码库
77,68,56,59
版本匹配 chromedriver

<></>
元素，<起始标签，属性名=属性值>文本内容</结束标签名>

元素共同属性，id唯一标识 在当前整个html
    class 类别   给元素归类 有很多元素有同样的class值，不是唯一的
    style name  内联样式设置 position
    name
javascript DOM 对象，如何进行交互


selenium 环境搭建以及原理解释

selenium里面的webdriver会直接控制浏览器，通过不同的浏览器的驱动，然后对目标进行代码层的操作；

"""

from selenium import webdriver
from time import sleep




driver = webdriver.Chrome()
url = "https://test-w1.sancaijia.net/?fileName=#/login"
driver.get(url)
driver.find_element_by_xpath('//input[@name="username"]').send_keys("17792303803")
driver.find_element_by_xpath('//input[@name="password"]').send_keys("Qwe@1234")
driver.find_element_by_xpath('//button[@type="button"]').click()

sleep(3)
driver.find_element_by_xpath('//span[text()="房源"]/parent::li/parent::a').click()
driver.quit()
