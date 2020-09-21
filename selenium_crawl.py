from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

op=Options()
# 不打开浏览器
op.add_argument("--headless")
# 不使用沙箱机制，docker 中使用需要配置该项目，docker 本身就运行大沙箱中
op.add_argument("--no-sandbox")
with webdriver.Chrome(options=op) as driver:
    driver.get('https://bbs.51credit.com/search.html?q=花呗&source=pc_bbs')
    el=WebDriverWait(driver,100).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'res-list')))
    print(driver.page_source)

