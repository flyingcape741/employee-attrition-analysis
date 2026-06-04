from os.path import curdir

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas
import os

from sympy.physics.units import length

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
links= []
url = 'https://www.emlakjet.com/satilik-daire/bursa?filtreler=max-fiyat=5000000&min-fiyat=0'
for sayfa in range(2,51):
   driver.get(url+f'&sayfa={sayfa}')
   ilanlar = driver.find_elements(By.CLASS_NAME, "styles_wrapper__587DT")
   for ilan in ilanlar:
      links.append(ilan.get_attribute('href'))

print(links)
print(len(links))

Fiyatlar = []
Adresler = []

NetMk = []
BrutMk = []
Oda = []
Yas = []
BulKat = []
KatSayı = []
Isıtma = []
KulDurum = []
TapuDurum = []
Sitedemi = []
BanyoSay = []


a=0
for link in links[0:50]:
   try:
      driver.get(link)

      a=a+1
      print(a)
      Fiyatlar.append(driver.find_element(By.CLASS_NAME, 'styles_price__6wmxk').text)
      Adresler.append(driver.find_element(By.CLASS_NAME, 'styles_location__HguIg').text)
      board = driver.find_element(By.CLASS_NAME,'styles_inner__qKPCB')
      keylist = board.find_elements(By.TAG_NAME, "li")
      for key in keylist:
         driver.execute_script("arguments[0].scrollIntoView(true);", key)
         templist = key.find_elements(By.TAG_NAME,"span")
         for j in templist:
            if j.text == "Net Metrekare":
               NetMk.append(templist[1].text)
            elif j.text == "Brüt Metrekare":
               BrutMk.append(templist[1].text)
            elif j.text == "Oda Sayısı":
               Oda.append(templist[1].text)
            elif j.text == "Binanın Yaşı":
               Yas.append(templist[1].text)
            elif j.text == "Bulunduğu Kat":
               BulKat.append(templist[1].text)
            elif j.text == "Binanın Kat Sayısı":
               KatSayı.append(templist[1].text)
            elif j.text == "Isıtma Tipi":
               Isıtma.append(templist[1].text)
            elif j.text == "Kullanım Durumu":
               KulDurum.append(templist[1].text)
            elif j.text == "Tapu Durumu":
               TapuDurum.append(templist[1].text)
            elif j.text == "Site İçerisinde":
               Sitedemi.append(templist[1].text)
            elif j.text == "Banyo Sayısı":
               BanyoSay.append(templist[1].text)
   except:
      pass
print(BanyoSay)
print(Fiyatlar)
print(Adresler)

current = os.path.dirname(os.path.realpath(__file__))
os.chdir(current + '\\csvler')

pandas.concat([
pandas.DataFrame(Fiyatlar),
pandas.DataFrame(Adresler),
pandas.DataFrame(NetMk),
pandas.DataFrame(BrutMk),
pandas.DataFrame(Oda),
pandas.DataFrame(Yas),
pandas.DataFrame(BulKat),
pandas.DataFrame(KatSayı),
pandas.DataFrame(Isıtma),
pandas.DataFrame(KulDurum),
pandas.DataFrame(TapuDurum),
pandas.DataFrame(Sitedemi),
pandas.DataFrame(BanyoSay)],axis=1
).to_csv("TestHal50.csv")




"""
FiyatlarDF = pandas.DataFrame(Fiyatlar).to_csv('Fiyatlar.csv')
AdreslerDF = pandas.DataFrame(Adresler).to_csv('Adresler.csv')

NetMkDF = pandas.DataFrame(NetMk).to_csv('NetMK.csv')
BrutMkDF = pandas.DataFrame(BrutMk).to_csv('BrutMK.csv')
OdaDF = pandas.DataFrame(Oda).to_csv('Oda.csv')
YasDF = pandas.DataFrame(Yas).to_csv('Yas.csv')
BulKatDF = pandas.DataFrame(BulKat).to_csv('BulKat.csv')
KatSayıDF = pandas.DataFrame(KatSayı).to_csv('KatSayı.csv')
IsıtmaDF = pandas.DataFrame(Isıtma).to_csv('Isıtma.csv')
KulDurumDF = pandas.DataFrame(KulDurum).to_csv('KulDurum.csv')
TapuDurumDF = pandas.DataFrame(TapuDurum).to_csv('TapuDurum.csv')
SitedemiDF = pandas.DataFrame(Sitedemi).to_csv('Sitedemi.csv')
BanyoSayDF = pandas.DataFrame(BanyoSay).to_csv('BanyoSay.csv')
"""


os.chdir(current)



"""DaireDataset = pandas.DataFrame({'index': [range(1,1501)],
                       'Fiyat': [Fiyatlar],
                       'Adres': [Adresler],
                       'Net Metrekare': [NetMk],
                       'Brüt Metrekare': [BrutMk],
                       'Oda': [Oda],
                       'Bina Yaşı': [Yas],
                       'Bulunduğu Kat': [BulKat],
                       'Kat Sayısı': [KatSayı],
                       'Isıtma': [Isıtma],
                       'Kullanım Durumu': [KulDurum],
                       'Tapu Durumu': [TapuDurum],
                       'Site İçindemi': [Sitedemi],
                       'Banyo Sayısı': [BanyoSay],
                       })


DaireDataset.to_excel("DaireDataset.xlsx")
"""
















