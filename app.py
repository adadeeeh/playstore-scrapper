import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/apps/details?id=com.akupintar.mobile.siswa&showAllReviews=true'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

script = soup.find_all('script')[31]
listScript = []
for x in script:
    listScript.append(str(x))

stringScript = ''.join(listScript)

def getAll(data):
    ss = data.replace("}});", "")
    sss = ss.split("(){return")
    pickData = sss.pop(1)
    rmEnter = pickData.replace("\n", "")
    rmBracket1 = rmEnter.replace("[", "")
    rmBracket2 = rmBracket1.replace("]", "")
    rmComma = rmBracket2.replace(",", "")
    rmNull = rmComma.replace("null", "")
    rmSlash = rmNull.replace("\\", "")
    listData = rmSlash.split("\"") 
    return listData

name = []
rating = []
comment = []

data = getAll(stringScript)
nextName = 3
jumlahIndex = (len(data))
for i in range(len(data)):
    if nextName <= len(data):
        if i == nextName:
            print(nextName)
            nextName = i + 28
            # print(listData[nextName])
            checkData = []
            if nextName < len(data):
                for x in data[nextName]:
                    checkData.append(str(x))
                if data[nextName] == '':
                    nextName = nextName + 1
                    # print(nextName)
            for j in range(len(checkData)):
                if j == 0:
                    if checkData[j] == 'h' and checkData[j+1] == 't' and checkData[j+2] == 't' and checkData[j+3] == 'p':
                        nextName = nextName - 2
                        # print(checkData[0])
                        break

            # print(listData[nextName])
            name.append(data[i])
            rating.append(data[i+3])
            comment.append(data[i+4])
            print(data[i], data[i+3], data[i+4])

dict = {'nama': name, 'rating': rating, 'comment': comment}
df = pd.DataFrame(dict)
df.to_csv('output.csv')