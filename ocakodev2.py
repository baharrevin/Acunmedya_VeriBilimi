"""
Koşullu İfadeler (if-else)
Soru: Kullanıcıdan bir sayı alarak, bu sayının çift mi tek mi olduğunu ekrana yazdıran bir Python programı yazın. 
Eğer sayı negatifse, ekrana "Negatif sayı girdiniz!" mesajı versin.
"""

number = int(input("bir tam sayı giriniz : "))

if number >= 0:
    if number%2 == 0:
        print(f"girdiğiniz sayı : {number} -- ÇİFT")
    elif not number%2 == 0:
        print(f"girdiğiniz sayı : {number} -- TEK")
elif number < 0:
    print("Negatif sayı girdiniz!")
else:
    print("hatalı tuşlama")