from collections import OrderedDict


def matrisOlustur(liste):
    alfabe_matris = [[0 for x in range(5)] for x in range(5)]
    index = 0
    for i in range(0,5):
        for j in range(0,5):
            alfabe_matris[i][j] = liste[index]
            index += 1
    return alfabe_matris
    

def anahtariTemizle(anahtar):
    
    anahtar = anahtar.lower()
    anahtar = anahtar.replace(" ", "")
    anahtar = anahtar.replace("j", "")

    return anahtar

def mesajiTemizle(mesaj):
    
    mesaj = mesaj.lower()
    mesaj = mesaj.replace(".", "")
    mesaj = mesaj.replace(" ", "")
    mesaj = mesaj.replace("j", "i")
   
    
    mesaj_dizi = [mesaj[i:i+2] for i in range(0,len(mesaj),2)]
    
    
    for i in range(0,len(mesaj_dizi)):
        char = mesaj_dizi[i]
        if len(char) == 2:
          if char[0] == char[1]:
            mesaj_dizi[i] = char[0] + "x" + char[1]
        
    mesaj_str = ""    
    
    for char in mesaj_dizi:
        mesaj_str += char
    
    mesaj_dizi = [mesaj_str[i:i+2] for i in range(0,len(mesaj_str),2)]
    
    if len(mesaj_dizi[-1]) == 1:
        mesaj_dizi[-1] += "x"
    
    return mesaj_dizi


def konumBul(harf, alfabe_matris):
    for i in range(0,5):
        for j in range(0,5):
            if alfabe_matris[i][j] == harf:
                return str(i) + str(j)
          
          
def diziYazdir(dizi, info):
    dizi_str = ""
    for char in dizi:
        dizi_str += char
    
    print info + " " + dizi_str
        
    
mesaj_input = raw_input("mesaji giriniz: ")
anahtar_input = raw_input("anahtari giriniz: ")
    
anahtar = anahtariTemizle(anahtar_input)

alfabe  = "abcdefghiklmnopqrstuvwxyz"
alfabe_matris = matrisOlustur(''.join(OrderedDict.fromkeys(anahtar+alfabe).keys()))
mesaj = mesajiTemizle(mesaj_input)


diziYazdir(mesaj, "gonderilmis mesaj: ")


sifrelenmis_dizi = []

for char in mesaj:
    ilk = konumBul(char[0], alfabe_matris)
    iki = konumBul(char[1], alfabe_matris)
    
    ilk_i = int(ilk[0])
    ilk_j = int(ilk[1])
    
    iki_i = int(iki[0])
    iki_j = int(iki[1])

    if ilk_i == iki_i:
        sec1_i = ilk_i
        sec1_j = (ilk_j+1)%5
        sec2_i = iki_i
        sec2_j = (iki_j+1)%5
        
    elif ilk_j == iki_j:
        sec1_j = ilk_j
        sec1_i = (ilk_i+1)%5
        sec2_j = iki_j
        sec2_i = (iki_i+1)%5
        
    else:
        sec1_i = ilk_i
        sec1_j = iki_j
        sec2_i = iki_i
        sec2_j = ilk_j
        
    sec1 = alfabe_matris[sec1_i][sec1_j]
    sec2 = alfabe_matris[sec2_i][sec2_j]
        
    sifrelenmis_dizi.append(sec1+sec2)
    
diziYazdir(sifrelenmis_dizi, "sifrelenmis mesaj: ")
