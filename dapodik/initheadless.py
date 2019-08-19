from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def headless_browser():
    options = Options()
    options.headless = False
    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Firefox(options=options, executable_path="/home/pedro/Documents/selenium/geckodriver")
    return browser