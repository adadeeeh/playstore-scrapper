import time
from bs4 import BeautifulSoup
import initheadless
import initdb

def scroll():
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    return lenOfPage

browser = initheadless.headless_browser()

db = initdb.create_db()
cursor = initdb.get_cursor(db)

browser.get("https://play.google.com/store/apps/details?id=com.akupintar.mobile.siswa&showAllReviews=true")

match = False
print("Loading page...")
while(match==False):
        lastCount = scroll()
        time.sleep(3)
        scroll()
        if lastCount == scroll():
            time.sleep(2)
            showMore = browser.find_element_by_xpath("//div[1]/div[4]/c-wiz/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div")
            browser.execute_script("arguments[0].click();", showMore)
            time.sleep(4)
            match=True

reviews = browser.find_elements_by_xpath("//div[1]/div[4]/c-wiz/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[@jscontroller='H6eOGe']")

print("Inserting " + str(len(reviews)) + " items to database")
id_review = 1
for review in reviews:
   soup = BeautifulSoup(review.get_attribute("innerHTML"), "lxml")
   name = soup.find(class_="X43Kjb").text
   rating = soup.find('div',role='img').get('aria-label').strip("Rated ")[0]
   date = soup.find(class_="p2TkOb").text
   comment = soup.find(class_="UD7Dzf").text
   comment = comment.lstrip()
   insert_query = """INSERT INTO REVIEW(id, name, rating, date, comment) values (%s, %s, %s, %s, %s)"""
   insert_data = (id_review, name, rating, date, comment)
   result = cursor.execute(insert_query, insert_data)
   db.commit()
   id_review += 1

db.close()
browser.quit() 