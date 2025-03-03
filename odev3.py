#### ödev 3


## BÖLÜM 1: Teorik Sorular

# Dosya açma modları (r, w, a, x, b, t) nedir ve hangi durumlarda kullanılır?
"""
r : read , dosyadaki bilgileri okumak için kullanılır
w : write , yeni bir dosya açar (eğer yoksa), dosyaya bilgi eklemek için kullanılır fakat önceki bilgileri siler
a : append , yeni bir dosya açar (eğer yoksa), var olan bilgiler üzerine bilgi eklemye yardımcı olur
x : dosya oluşturur
b : binary , diğer dosyalar için diğer harflerin yanına eklenir
t : text , metin dosyaları için diğer harflerin yanına eklenir 
"""

# Bir dosyayı okurken read(), readline() ve readlines() arasındaki farklar nelerdir?
"""
read : bütün dosyayı okur
readline : satır okur
readlines : satırlar okur liste gibi yazar
"""

# Dosya işlemlerinde with open(...) kullanmanın avantajları nelerdir?
"""
open dosyayı açarsak close yazmamıza gerek kalmaz kendiliğinden kapanır ve fazla kod karmaşası ya da dosya kapamayı unutma gibi durumları engeller
"""

# JSON formatı nedir ve hangi durumlarda kullanılır?
"""
anahtar - değer kullanılır (dictionary) yani daha düzenlidir veri depolamak veri çekmek için
""" 

# Bir dosyanın var olup olmadığını kontrol etmek için hangi Python modülü kullanılır? Örnek kod ile açıklayınız.
"""
dosya var mı yok mu kontrolü için os modülü kullanılır 

import os 
if os.path.exists("ornek.txt"):
    print("dosya mevcut")
else:
    print("dosya bulunamadı")
"""



## BÖLÜM 2: Uygulamalı Çalışmalar


"""
1. Metin Dosyası İşleme
📌 Görev:

"ogrenciler.txt" adlı bir dosya oluşturun.
Kullanıcıdan öğrenci isimleri alarak bu dosyaya ekleyin.
Kullanıcı "bitti" yazdığında giriş işlemini sonlandırın.
Dosyadaki öğrenci isimlerini ekrana yazdıran bir fonksiyon yazın.
💡 İpucu: open("ogrenciler.txt", "a") kullanabilirsiniz.
"""


def ogrenci_ekleme():
        ogrenciler =[] 
        while True:
            numara = str(input("kullanıcının okul numarası: "))
            ad = input("kullanıcı adı: ")
            soyad = input("kullanıcı soyadı: ")
            ogrenci = f"{numara},{ad},{soyad}\n"            
            ogrenciler.append(ogrenci)

            secim = input("öğrenci eklemeye devam etmek için 'devam', İşlemi sonlandırmak için 'bitti' yazınız : ")
            if secim == "devam":
                continue
            elif secim == "bitti":
                break
            else:
                print("hatalı tuşlama")
        
        with open ("ogrenci_bilgileri.txt" , "a" , encoding="utf-8") as dosya:
            dosya.writelines(ogrenciler)
            
        print("öğrenci-öğrenciler başarıyla eklendi")


def ogrencileri_goruntule():
    print("**** Tüm öğrenciler:")

    with open ("ogrenci_bilgileri.txt", "r" , encoding="utf-8") as dosya:
        print(dosya.read())


def ogrenci_sistemi():
    while True:
        print("1 - öğrenci ekleme")
        print("2 - tüm öğrencileri görüntüleme")
        print("3 - çıkış")
        secim = input("yapmak istediğiniz işlemi seçiniz : ")

        if secim == "1":
            print("****** yeni öğrenci ekleme ******")
            ogrenci_ekleme()
        elif secim == "2":
            print("****** tüm öğrencileri görüntüleme ******")
            ogrencileri_goruntule()
        elif secim == "3" :
            print("çıkış yapıldı...")
            break
        else:
            print("HATALI TUŞLAMA YAPTINIZ")
            ogrenci_sistemi() 
    
ogrenci_sistemi()


"""
2. Günlük Kayıt Defteri
📌 Görev:

Kullanıcıdan aldığı notları "gunluk.txt" dosyasına ekleyen bir program yazın.
Kullanıcı "goruntule" komutunu girerse, dosyada kayıtlı tüm notları ekrana yazdırın.
Kullanıcı "sil" yazarsa "gunluk.txt" dosyasını silin.
💡 İpucu: os.remove("gunluk.txt") komutunu kullanabilirsiniz.
"""

def gunluk_yaz():
    print("Günlük yazma kısmına hoşgeldiniz")
    txt = input("günlüğünüze yazmak istediğiniz metni giriniz: ")
    with open("gunluk.txt", "a", encoding="utf-8" ) as dosya:
        dosya.write(txt + "\n")
    print("günlük yazınız kaydedildi")


def gunluk_goruntule():
    print("Günlük görüntüleme kısmına hoşgeldiniz, metniniz : ")
    with open("gunluk.txt","r",encoding="utf-8") as dosya:
        print(dosya.read())
    

import os 

def gunluk_sil():
    os.remove("gunluk.txt")
    print("Günlüğünüz başarıyla temizlendi")


def gunluk_sistemi():
    print("hoşgeldiniz")

    while True: 
        print("1- Günlüğe ekleme yapma")
        print("2- Günlüğü görüntüleme")
        print("3- Günlüğü temizleme")
        print("4- Sistemden çıkış")

        secim = input("yapmak istediğiniz işlem numarasını giriniz : ")

        
        if secim == "1":
            print("***** Günlüğe ekleme yapma *****")
            gunluk_yaz()
        elif secim == "2":
            print("***** Günlüğü görüntüleme *****")
            gunluk_goruntule()
        elif secim == "3":
            print("***** Günlüğü temizleme *****")
            gunluk_sil()
        elif secim == "4":
            print("***** Sistemden çıkılıyor... *****")
            break
        else:
            print("*******  hatalı tuşlama, Tekrar tuşlama yapınız *******")
        
gunluk_sistemi()




"""
3. JSON Kullanarak Kullanıcı Bilgileri Saklama
📌 Görev:

"kullanicilar.json" adlı bir dosya oluşturun.
Kullanıcıdan ad, soyad ve yaş bilgilerini alıp JSON formatında kaydedin.
Kullanıcının "listele" komutunu girdiğinde JSON dosyasındaki tüm kullanıcıları ekrana yazdırın.
💡 İpucu: json.dump() ve json.load() fonksiyonlarını kullanabilirsiniz.
"""

import json

def kullanıcı_ekle():
    print("HOŞGELDİNİZ!")
    ad = input("adınız: ")
    soyad = input("soyadınız: ")
    yas = input("yaşınız: ")

    kullanıcı = {
        "kullanıcı adı" : ad,
        "kullanıcı soyadı" : soyad,
        "kullanıcı yaşı" : yas
    }

    with open("kullanıcılar.json", "w", encoding="utf-8") as dosya:
        json.dump(kullanıcı, dosya, ensure_ascii=False, indent=4)

# "a" ile açamıyorum hata veriyor ama bu şekilde de yeni kullanıcı ekleyince öncekiler siliniyo  ????????????????????

def kullanıcı_listesi():
    print("kullanıcılar listeleniyor...")
    with open("kullanıcılar.json","r",encoding="utf-8") as dosya:
        kullanıcılar = json.load(dosya)
    print(kullanıcılar)

def sistem():
    while True:
        print("sisteme hoşgeldiniz ! ")
        print("1 - kullanıcı ekleme")
        print("2 - kullanıcıları görüntüleme")
        print("3 - sistemden çıkış")
    
        secim = input("yapmak istediğiniz işlem numarasını giriniz : ")
        
        if secim == "1":
            kullanıcı_ekle()

        elif secim == "2":
            kullanıcı_listesi()

        elif secim == "3":
            print("\nsistemden çıkış yapıldı!")
            break

sistem()



"""
4. Telefon Rehberi Uygulaması
📌 Görev:

"rehber.txt" adlı bir dosyada telefon numaralarını saklayan bir program yazın.
Kullanıcı "ekle" komutu girerse, ad ve telefon numarası alıp dosyaya ekleyin.
Kullanıcı "ara" komutunu girerse, adı girilen kişinin telefon numarasını gösterin.
Kullanıcı "listele" komutunu girerse, tüm rehberi ekrana yazdırın.
💡 İpucu: Dosyayı satır satır okuyarak ad-soyad eşleştirmesi yapabilirsiniz.
"""


def kullanıcı_ekle():
    print("*** KULLANICI EKLE ***")
    ad = input("kullanıcı adı : ")
    tel = input("kullanıcı telefon numarası : ")
    
    with open("rehber.txt","a",encoding="utf-8")as dosya:
        dosya.write(f"kullanıcı adı: {ad}, kullanıcı telefon numarası: {tel} \n")
    print("\nkullanıcı başarıyla eklendi")

def kullanıcı_ara():
    print("*** KULLANICI ARA ***")
    secim = input("aramak istediğiniz kullanıcının adını giriniz : ")
    with open("rehber.txt","r",encoding="utf-8") as dosya:
        for line in dosya:
            if secim in line:
                print(line)

            else:
                print("kullanıcı bulunamadı")

def kullanıcı_listele():
    print("*** KULLANICI LİSTELE ***")
    with open("rehber.txt","r",encoding="utf-8") as dosya:
        print(dosya.read())

           

def sistem():
    while True:
        print("Kullanıcı eklemek için 'ekle'")
        print("Kullanıcı aramak için 'ara'")
        print("Kullanıcı listelemek için 'listele'")
        print("Sistemden çıkış yapmak için 'çıkış'")
        print("yapmak istediğiniz işlem için yukarıdaki komutları yazmanız gerekmektedir.")
        secim = input("\n***** yapmak istediğiniz işlem komutu : ")

        if secim == "ekle":
            kullanıcı_ekle()

        elif secim == "ara":
            kullanıcı_ara()
        
        elif secim == "listele":
            kullanıcı_listele()

        elif secim == "çıkış":
            print("çıkış yapılıyor...")
            break
        else:
            print("hatalı tuşlama...")

sistem()



"""
5. Otomatik Log Kayıt Sistemi
📌 Görev:

"log.txt" dosyasına her 10 saniyede bir sistemin çalıştığını kaydeden bir Python programı yazın.
Kayıtlara zaman damgası ekleyin ("%Y-%m-%d %H:%M:%S" formatında).
Kullanıcı "loglari_goruntule" yazarsa, dosyadaki tüm logları ekrana yazdırın.
💡 İpucu: time.sleep(10) fonksiyonunu kullanabilirsiniz.
"""

import datetime
import time

def log():
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  ### ????????????????????
    with open("log.txt","a",encoding="utf-8")as dosya:
        dosya.write(f"{zaman} - Sistem çalışıyor...\n")

def log_goruntule():
    with open("log.txt", "r", encoding="utf-8") as dosya:
        print("*** LOG KAYITLARI ***")
        print(dosya.read())

def sistem():
    while True:
        log()
        time.sleep(10)

        komut = input("Logları görüntülemek için 'loglari_goruntule' yazın ya da bitirmek için 'çıkış' yazın: ")
        if komut == "loglari_goruntule":
            log_goruntule()
        elif komut == "çıkış":
            print("çıkış yapıldı...")
            break
        else:
            print("hatalı tuşlama !!!")

sistem()