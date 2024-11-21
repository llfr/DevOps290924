from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.get("file:///Users/lewfaiman/Downloads/tip_calc/index.html")
d.find_element(by="id", value="billamt").send_keys(100)
d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
d.find_element(by="id", value="peopleamt").send_keys(5)

expected = "6.00"
actual = d.find_element(by="id", value="tip").text
is_visiable = d.find_element(by="id", value="tip").is_displayed()
assert actual == expected
assert is_visiable
sleep(10)
