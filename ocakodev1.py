""" Değişkenler ve Kullanıcı Girişi
Soru: Kullanıcıdan adını, soyadını ve yaşını alan bir Python programı yazın. Alınan bilgileri şu formatta ekrana yazdırın:
"Merhaba [Ad Soyad], [Yaş] yaşındasınız. Hoş geldiniz!
"""

name = input("adınız : ")
surname = input("soyadınız : ")
age = input("yaşınız : ")

print(f"Merhaba {name} {surname}, {age} yaşındasınız. Hoş geldiniz!")