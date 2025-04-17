import random
import string

def sifre_olustur(uzunluk=12, ozel_karakterler=True, sayilar=True, buyuk_harfler=True):
    karakterler = string.ascii_lowercase
    if buyuk_harfler:
        karakterler += string.ascii_uppercase
    if sayilar:
        karakterler += string.digits
    if ozel_karakterler:
        karakterler += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    sifre = ""
    for _ in range(uzunluk):
        sifre += random.choice(karakterler)
    return sifre

print("🔐 Güçlü Şifre Oluşturucuya Hoş Geldiniz! 🔐")

while True:
    try:
        uzunluk = int(input("\nŞifre uzunluğunu girin (minimum 8): "))
        if uzunluk < 8:
            print("❌ Şifre uzunluğu en az 8 karakter olmalıdır!")
            continue
            
        ozel = input("Özel karakterler eklensin mi? (e/h): ").lower() == 'e'
        sayilar = input("Sayılar eklensin mi? (e/h): ").lower() == 'e'
        buyuk = input("Büyük harfler eklensin mi? (e/h): ").lower() == 'e'
        
        yeni_sifre = sifre_olustur(uzunluk, ozel, sayilar, buyuk)
        print(f"\n🎉 İşte yeni şifreniz: {yeni_sifre}")
        
        devam = input("\nBaşka bir şifre oluşturmak ister misiniz? (e/h): ").lower()
        if devam != 'e':
            print("\n👋 Güle güle!")
            break
            
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin!") 