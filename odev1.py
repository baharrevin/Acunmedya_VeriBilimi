# ödev 1

# Bölüm 1: Operatörler ile İşlemler

a = float(input("Birinci tam sayı/ondalıklı sayı girin: "))
b = float(input("İkinci tam sayı/ondalıklı sayı girin: "))

addition = a+b
print("Girdiğiniz değerlerin toplamı: ", addition)

subtraction = a-b
print("Girdiğiniz değerlerin farkı: ", subtraction)

multiplication = a*b
print("Girdiğiniz değerlerin çarpımı: ", multiplication)

dividing = a/b
print("Girdiğiniz değerlerin bölümü: ", dividing)

mode = a%b
print("Girdiğiniz değerlerin modu: ", mode)

exponentiation = a**b
print("Girdiğiniz değerlerin üs alınması: ", exponentiation)



# Bölüm 2: Döngüler ile Uygulamalar

## Görev 2: Kullanıcıdan bir sayı alarak 1’den o sayıya kadar olan sayıların toplamını hesaplayan bir Python programı yazın. (For veya While döngüsü kullanın.)

number = int(input("bir tam sayı girin: "))
total = 0

for i in range(1, number):
    total += i

print("1'den itibaren girdiğiniz tam sayıya kadar olan tüm tam sayıların toplamı: ", total)

### yönergede "o sayıya kadar" yazdığı için kullanıcı tarafından verilen sayı toplama işlemine dahil edilmedi 


## Görev 3: 1 ile 100 arasındaki çift sayıları ekrana yazdıran bir Python programı yazın.


for i in range (1,100):
    if i % 2 == 0:
        print(i)
    else:
        continue


## Görev 4: Kullanıcıdan alınan bir metni ters çeviren ve ekrana yazdıran bir Python programı yazın. (Döngü kullanarak yapın.)

sentence = input("Bir cümle giriniz: ")
reverse = ""

for i in sentence:
    reverse = i + reverse

print("Girdiğiniz metnin ters çevrilmiş hali: ", reverse)
