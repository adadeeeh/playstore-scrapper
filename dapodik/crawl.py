import time
from bs4 import BeautifulSoup
import initheadless
import initdb

browser = initheadless.headless_browser()

db = initdb.create_db()
cursor = initdb.get_cursor(db)

browser.get("http://dapo.dikdasmen.kemdikbud.go.id/progres")
time.sleep(4)
link_provinsi = browser.find_elements_by_xpath("//div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody/tr[@role='row']")
# get provinsi
daftar_link_kabupaten = []
for data_provinsi in link_provinsi:
   provinsi = []
   soup_provinsi = BeautifulSoup(data_provinsi.get_attribute("innerHTML"), "lxml")
   for data in soup_provinsi.find_all("td"):
      provinsi.append(data.text)
   provinsi.pop(2)
   for x in range(1, len(provinsi)):
      if x == 1:
         daftar_link_kabupaten.append(provinsi[x])
      else:
         f = float(provinsi[x])
         provinsi[x] = f

   # insert_query = """INSERT INTO Provinsi(provinsiid, nama_provinsi, total_sekolah, total_kirim, total_sisa, total_sd, total_kirim_sd,
   #      total_sisa_sd, total_smp, total_kirim_smp, total_sisa_smp, total_sma, total_kirim_sma, total_sisa_sma,
   #      total_slb, total_kirim_slb, total_sisa_slb, total_smk, total_kirim_smk,
   #      total_sisa_smk) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
   # insert_data = provinsi
   # cursor.execute(insert_query, insert_data)
   # db.commit()

# get kabupaten
dict_provinsi = {}
daftar_link_kecamatan = []
counter_provinsi = 1
for link in daftar_link_kabupaten:
   browser.find_element_by_link_text(link).click()
   time.sleep(4)
   nama_provinsi = BeautifulSoup(browser.find_element_by_xpath("//div[2]/div[1]/div[1]/ul/li[3]").get_attribute("innerHTML"), "lxml").get_text()
   dict_provinsi[nama_provinsi] = counter_provinsi
   id_provinsi = dict_provinsi[nama_provinsi]
   counter_provinsi += 1
   link_kabupaten = browser.find_elements_by_xpath("//div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody/tr[@role='row']")
   for data_kabupaten in link_kabupaten:
      kabupaten = []
      soup_kabupaten = BeautifulSoup(data_kabupaten.get_attribute("innerHTML"), "lxml")
      for i in soup_kabupaten.find_all("td"):
         kabupaten.append(i.text)
      kabupaten.pop(2)
      for x in range(1, len(kabupaten)):
         if x == 1:
            daftar_link_kecamatan.append(kabupaten[x])
         else:
            f = float(kabupaten[x])
            kabupaten[x] = f
      kabupaten.insert(1, id_provinsi)
      # insert_query = """INSERT INTO Kabupaten(kabupatenid, provinsiid, nama_kabupaten, total_sekolah, total_kirim, total_sisa, total_sd, total_kirim_sd,
      #   total_sisa_sd, total_smp, total_kirim_smp, total_sisa_smp, total_sma, total_kirim_sma, total_sisa_sma,
      #   total_slb, total_kirim_slb, total_sisa_slb, total_smk, total_kirim_smk,
      #   total_sisa_smk) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
      # insert_data = kabupaten
      # cursor.execute(insert_query, insert_data)
      # db.commit()
      print (daftar_link_kecamatan)
      print (kabupaten)
   browser.back()
   time.sleep(4)

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