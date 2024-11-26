from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?reff=menu_main")
source_data = driver.page_source
soup = bs(source_data, features="html.parser")
time.sleep(4)
driver.close()