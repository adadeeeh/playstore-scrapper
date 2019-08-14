from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
#driver.get("https://www.youtube.com/")
#element_text = driver.find_element_by_id("title").text
driver.get("https://play.google.com/store/apps/details?id=com.akupintar.mobile.siswa&showAllReviews=true")
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# action = webdriver.common.action_chains.ActionChains(driver)
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            time.sleep(2)
            showMore = driver.find_element_by_xpath("//div[1]/div[4]/c-wiz/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div")
            driver.execute_script("arguments[0].click();", showMore)
            # action.move_to_element_with_offset(showMore, 612, 18)
            # action.click()
            # action.perform()
            time.sleep(4)
            match=True

reviews = driver.find_elements_by_xpath("//div[1]/div[4]/c-wiz/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[@jscontroller='H6eOGe']")

id_review = 1
for review in reviews:
   soup = BeautifulSoup(review.get_attribute("innerHTML"), "lxml")
#    print (soup)
   name = soup.find(class_="X43Kjb").text
   rating = soup.find('div',role='img').get('aria-label').strip("Rated ")[0]
   date = soup.find(class_="p2TkOb").text
   comment = soup.find(class_="UD7Dzf").text
   comment = comment.lstrip()
   print (name)
#print(element_text)
