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

browser.get("http://dapo.dikdasmen.kemdikbud.go.id/progres")
time.sleep(4)
datas_provinsi = browser.find_elements_by_xpath("//div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody/tr[@role='row']")
ganjil = True
for data_provinsi in datas_provinsi:
   provinsi = []
   soup_provinsi = BeautifulSoup(data_provinsi.get_attribute("innerHTML"), "lxml")
   provinsiid = soup_provinsi.find(class_ = "sorting_1").text
   nama_provinsi = soup_provinsi.find("a").text
   for data in soup_provinsi.find_all("td"):
      provinsi.append(data.text)
   provinsi.pop(2)
   for x in range(2, 20):
      f = float(provinsi[x])
      provinsi[x] = f
   insert_query = """INSERT INTO Provinsi(provinsiid, nama_provinsi, total_sekolah, total_kirim, total_sisa, total_sd, total_kirim_sd,
        total_sisa_sd, total_smp, total_kirim_smp, total_sisa_smp, total_sma, total_kirim_sma, total_sisa_sma,
        total_slb, total_kirim_slb, total_sisa_slb, total_smk, total_kirim_smk,
        total_sisa_smk) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
   insert_data = provinsi
   cursor.execute(insert_query, insert_data)
   db.commit()
   print (provinsi)

# match = False
# print("Loading page...")
# while(match==False):
#         lastCount = scroll()
#         time.sleep(3)
#         scroll()
#         if lastCount == scroll():
#             time.sleep(2)
#             showMore = browser.find_element_by_xpath("//div[1]/div[4]/c-wiz/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div")
#             browser.execute_script("arguments[0].click();", showMore)
#             time.sleep(4)
#             match=True

# reviews = browser.find_elements_by_xpath("//div[1]/div[4]/c-wiz/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[@jscontroller='H6eOGe']")

# print("Inserting " + str(len(reviews)) + " items to database")
# id_review = 1
# for review in reviews:
#    soup = BeautifulSoup(review.get_attribute("innerHTML"), "lxml")
#    name = soup.find(class_="X43Kjb").text
#    rating = soup.find('div',role='img').get('aria-label').strip("Rated ")[0]
#    date = soup.find(class_="p2TkOb").text
#    comment = soup.find(class_="UD7Dzf").text
#    comment = comment.lstrip()
#    insert_query = """INSERT INTO REVIEW(id, name, rating, date, comment) values (%s, %s, %s, %s, %s)"""
#    insert_data = (id_review, name, rating, date, comment)
#    result = cursor.execute(insert_query, insert_data)
#    db.commit()
#    id_review += 1

db.close()
browser.quit() 