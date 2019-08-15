from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def headless_browser():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    return browser