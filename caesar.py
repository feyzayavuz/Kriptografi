anahtar = raw_input("anahtari giriniz: ")
mesaj = raw_input("mesaji giriniz: ")
alfabe = "abcdefghijklmnopqrstuvwxyz"
def mesajiTemizle(mesaj):
    mesaj = mesaj.lower()
    mesaj = mesaj.replace(" ","")
    mesaj = mesaj.replace(".","")
    mesaj = mesaj.replace(",","")
    
    return mesaj 
    
mesaj = mesajiTemizle(mesaj)
mesaj = list(mesaj)

def konumBul(harf, alfabe):
    for i in range(0,len(alfabe)):
        if alfabe[i] == harf:
            return str(i)

liste=[]
def sifrele(alfabe,konum,anahtar):
    for i in range(0,len(mesaj)):
        konum = (int(konumBul(mesaj[i],alfabe))+int(anahtar))%len(alfabe)
        liste.append(alfabe[konum])
    
    return liste

x=0
for i in range(0,len(mesaj)):
    x =  konumBul(mesaj[i],alfabe)
sifrele(alfabe,x,anahtar)


def diziYazdir(dizi, info):
    dizi_str = ""
    for char in dizi:
        dizi_str += char
    
    print info + " " + dizi_str
    
    
diziYazdir(mesaj,"gonderilmis mesaj: ")
diziYazdir(liste,"sifrelenmis mesaj: ")

print mesaj
print liste

