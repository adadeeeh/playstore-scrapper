import pymysql
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

db = pymysql.connect('localhost', 'pedro', '1', 'python')

cursor = db.cursor()

drop = """DROP TABLE IF EXISTS REVIEW"""
create = """CREATE TABLE REVIEW (
    id int,
    name char(40),
    rating int,
    date varchar(255),
    comment text ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin;"""

try:
    cursor.execute(create)
except:
    cursor.execute(drop)
    cursor.execute(create)

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
ids = []
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

id_review = 1
for review in reviews:
    soup = BeautifulSoup(review.get_attribute("innerHTML"),"lxml")
    name = soup.find(class_="X43Kjb").text
    rating = soup.find('div',role='img').get('aria-label').strip("Rated ")[0]
    date = soup.find(class_="p2TkOb").text
    comment = soup.find(class_="UD7Dzf").text
    comment = comment.lstrip()
    # names.append(name)
    # ratings.append(rating)
    dates.append(date)
    # comments.append(comment)
    # ids.append(id_review)
    insert_query = """INSERT INTO REVIEW(id, name, rating, date, comment) values (%s, %s, %s, %s, %s)"""
    insert_tuple = (id_review, name, rating, date, comment)
    result = cursor.execute(insert_query, insert_tuple)
    db.commit()
    id_review += 1

db.close()
browser.quit()