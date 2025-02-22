## öğrenci bilgi sistemi


ogrenci_listesi = []

def ogrenci_ekle():
    ad = input("öğrencinin adı: ")
    soyad = input("öğrencinin soyadı: ")
    numara = input("öğrencinin numarası: ")
    bolum = input("öğrencinin bölümü: ")
    ortalama = input("öğrencinin not ortalaması: ")

    for ogrenciler in ogrenci_listesi:
        if ad == ogrenciler["öğrencinin adı"]:
            print("Bu öğrenci daha önce kaydedilmiş, menüye yönlendiriliyorsunuz...")
            ogrenci_sistemi()
            return

    
    ogrenciler = {
        "öğrencinin adı" : ad,
        "öğrencinin soyadı" : soyad,
        "öğrencinin numarası" : numara,
        "öğrencinin bölümü" : bolum,
        "öğrencinin not ortalaması" : ortalama
    }
    ogrenci_listesi.append(ogrenciler)
    print(f"{numara} numaralı öğrenci sisteme başarıyla yüklenmiştir..")


def ogrenci_sorgula():
    
    if len(ogrenci_listesi) == 0:
            print("Kaydedilmiş herhangi bir öğrenci bulunmamaktadır!")
            ogrenci_sistemi()
    else:
        print("KAYITLI ÖĞRENCİ LİSTESİ") 
        print(ogrenci_listesi)
        ogr_num = input("Bilgilerini görüntülemek istediğiniz öğrencinin öğrenci numarasını giriniz: ")
        
        for ogrenciler in ogrenci_listesi:
            if ogrenciler["öğrencinin numarası"] == ogr_num: 
                print(f"\n{ogr_num} numaralı öğrencinin bilgileri: ")
                print("öğrencinin adı: " + ogrenciler["öğrencinin adı"])
                print("öğrencinin soyadı: " + ogrenciler["öğrencinin soyadı"])
                print("öğrencinin numarası: " + ogrenciler["öğrencinin numarası"])
                print("öğrencinin bölümü: " + ogrenciler["öğrencinin bölümü"])
                print("öğrencinin not ortalaması: " + ogrenciler["öğrencinin not ortalaması"])

            
            elif ogrenciler["öğrencinin numarası"] != ogr_num:
                print(f"{ogr_num} numaralı kayıtlı öğrenci bulunamadı...")
            
                while True: 
                    secim = input("1 - Öğrenci sorgula\n2 - Menü\nSEÇİMİNİZ: ")
                    if secim == "1" : 
                        ogrenci_sorgula()
                    elif secim == "2" : 
                        ogrenci_sistemi()
                    else:
                        print("***** HATALI TUŞLAMA *****")

        



def ogrenci_guncelle():
    ogr_num = input("Bilgilerini güncellemek istediğiniz öğrencinin öğrenci numarasını giriniz: ")
    
    for ogrenciler in ogrenci_listesi:
        if ogr_num == ogrenciler["öğrencinin numarası"]:
            print("1 - öğrencinin adı\n2 - öğrencinin soyadı\n3 - öğrencinin numarası\n4 - öğrencinin bölümü\n5 - öğrencinin not ortalaması")
            secim = input(f"{ogr_num} numaralı öğrencinin güncellemek istediğiniz bilgisinin numarasını giriniz: ")
            if secim == "1":
                guncel = input("güncel isim bilgisi giriniz: ")
                ogrenciler["öğrencinin adı"] = guncel
            elif secim == "2":
                guncel = input("güncel soyisim bilgisi giriniz: ")
                ogrenciler["öğrencinin soyadı"] = guncel
            elif secim == "3":
                guncel = input("güncel öğrenci numara bilgisi giriniz: ")
                ogrenciler["öğrencinin numarası"] = guncel
            elif secim == "4":
                guncel = input("güncel bölüm bilgisi giriniz: ")
                ogrenciler["öğrencinin bölümü"] = guncel
            elif secim == "5":
                guncel = input("güncel not ortalaması bilgisi giriniz: ")
                ogrenciler["öğrencinin not ortalaması"] = guncel
            else:
                print("***** HATALI TUŞLAMA *****")
                while True: 
                    secim = input("1 - Öğrenci bilgisi güncelleme\n2 - Menü")
                    if secim == "1" : 
                        ogrenci_guncelle()
                    elif secim == "2" : 
                        ogrenci_sistemi()
                    else:
                        print("***** HATALI TUŞLAMA *****")
                        


def ogrenci_silme():
    ogr_num = input("Silmek istediğiniz öğrencinin öğrenci numarasını giriniz: ")
    for ogrenciler in ogrenci_listesi:
        if ogr_num == ogrenciler["öğrencinin numarası"]:
            ogrenci_listesi.remove(ogrenciler)
            print(f"\n{ogr_num} numaralı öğrenci silme işlemi gerçeleşti! ")



def ogrenci_sistemi():
    while True:
        print("ÖĞRENCİ BİLGİ SİSTEMİ")
        print("1 - Öğrenci Ekleme\n2 - Öğrenci Bilgilerini Görüntüleme\n3 - Öğrenci Bilgilerini Güncelleme\n4 - Öğrenci Silme\n5 - SİSTEMDEN ÇIKIŞ")
        secim = input("\n Yapmak istediğiniz işlemin numarasını giriniz: ")

        if secim == "1":
            print("*** ÖĞRENCİ EKLEME ***")
            ogrenci_ekle()

        elif secim == "2":
            print("*** ÖĞRENCİ BİLGİLERİNİ GÖRÜNTÜLEME ***")
            ogrenci_sorgula()

        elif secim == "3":
            print("*** ÖĞRENCİ BİLGİLERİNİ GÜNCELLEME ***")
            ogrenci_guncelle()
        
        elif secim == "4":
            print("*** ÖĞRENCİ SİLME ***")
            ogrenci_silme()

        elif secim == "5":
            print("********** SİSTEMDEN ÇIKIŞ YAPILDI **********")
            break


ogrenci_sistemi()