print("""********************* 
ATM PROGRAMI V1.0'a Hoşgeldiniz!
1.Bakiye Sorgula
2.Para Yatır
3.Para Çek
Çıkmak için "q" Enter'layın
*********************""")
bakiye = 1000
while True:
    islemSec = input("İşlem seçiniz: ")
    if islemSec == "q":
        break
    elif islemSec == "1":
        print(f"Bakiyeniz {bakiye} TL")
    elif islemSec == "2":
        yatir = int(input("Miktar Giriniz: "))
        bakiye += yatir
    elif islemSec == "3":
        cek = int(input("Miktar Giriniz: "))
        if bakiye - cek < 0:
            print("Bakiyenizden yüksek miktar çekemezsiniz")
            continue
        bakiye -= cek
    else:
        print("Yanlış işlem yapıyorsunuz")