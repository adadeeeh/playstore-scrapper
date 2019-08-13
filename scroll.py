import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import pymysql

browser = webdriver.Firefox()
names = []
ratings = []
dates = []
comments = []

browser.get("https://play.google.com/store/apps/details?id=com.akupintar.mobile.siswa&showAllReviews=true")

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            showMore = browser.find_element_by_xpath("//div[1]/div[4]/c-wiz/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div").click()
            match=True

reviews = browser.find_elements_by_xpath("//div[1]/div[4]/c-wiz/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[@jscontroller='H6eOGe']")
for review in reviews:
    soup = BeautifulSoup(review.get_attribute("innerHTML"),"lxml")
    name = soup.find(class_="X43Kjb").text
    rating = soup.find('div',role='img').get('aria-label').strip("Rated ")[0]
    date = soup.find(class_="p2TkOb").text
    comment = soup.find(class_="UD7Dzf").text
    comment = comment.lstrip()
    names.append(name)
    ratings.append(rating)
    dates.append(date)
    comments.append(comment)
    print(name)
    print(rating)
    print(date)
    print(comment)

dict = {'nama': names, 'rating': ratings, 'date': dates, 'comment': comments}
df = pd.DataFrame(dict)
df.to_csv('output.csv')

