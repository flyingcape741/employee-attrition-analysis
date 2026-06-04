import pandas
import os, glob
import re



#EvData için

#Fiyat değer kontrolü
"""
data = pandas.read_csv("SonHal.csv")
b= 0
for index,row in data.iterrows():
    if row['Fiyatlar'] >=6000000:
        b = b+1
print(f"fazla değer= {b}")
"""




"""
data = pandas.read_csv("SonHal.csv")
data = data.rename(columns={"Isıtma": "Isitma", "KatSayı": "KatSayi", "İlçe": "Ilce"})

data.to_csv('SonHal.csv')
"""

"""
data = pandas.read_csv("SonHal.csv")
index = 0
for i in data['Yas']:
    if i == '21 Ve Üzeri':
        data.at[index,'Yas'] = 21
    elif i == '0 (Yeni)':
        data.at[index,'Yas'] = 0
    elif i == '5-10':
        data.at[index,'Yas'] = 7.5
    elif i == '11-15':
        data.at[index,'Yas'] = 13
    elif i == '16-20':
        data.at[index,'Yas'] = 18
    index = index+1
data.to_csv('SonHal.csv')
"""







#csvler için
"""
Adres = pandas.read_csv('C:\\Users\\enesc\\PycharmProjects\\SatılıkDaire\\csvler\\Adresler.csv')
Adres = Adres.loc[:, ~Adres.columns.str.contains('^Unnamed')]
Mahalle = []
İlçe = []

for index,row in Adres.iterrows():
    templist = row['0'].split(' - ')
    İlçe.append(templist[1])
    Mahalle.append(templist[2])
MahalleDF = pandas.DataFrame(Mahalle).to_csv('Mahalle.csv')
İlçeDF = pandas.DataFrame(İlçe).to_csv('İlçe.csv')
"""





#csvler için
"""
df = pandas.DataFrame()
if os.path.exists("C:\\Users\\enesc\\PycharmProjects\\SatılıkDaire\\csvler\\SonHal.csv"):
    os.remove("C:\\Users\\enesc\\PycharmProjects\\SatılıkDaire\\csvler\\SonHal.csv")
files = glob.glob(os.path.join(os.getcwd(),'*.csv'))
for i in files:
    a = pandas.read_csv(i)
    a = a.loc[:, ~a.columns.str.contains('^Unnamed')]
    name = i.split("\\")[-1].split(".")[0]
    a.columns = [name]
    if name == "BrutMK" or name == "NetMK":
        for index, value in enumerate(a[name]):
            a.at[index,name] = value.split(' ')[0]
    elif name == "BulKat":
        for index, value in enumerate(a[name]):
            a.at[index,name] = value.split('.')[0]
    elif name == "Fiyatlar":
        for index, value in enumerate(a[name]):
            templist2 = re.split(r"[. ]", value)
            templist2.pop(-1)
            last = ""
            for t in templist2:
                last = last + t
            a.at[index,name] = last
            


    df = pandas.concat([df, a],axis =1)
df.to_csv('SonHal.csv')


"""
os.chdir(current)
