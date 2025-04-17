import math

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"
    return x / y

def us_alma(x, y):
    return x ** y

def karekok(x):
    if x < 0:
        return "Negatif sayının karekökü alınamaz!"
    return math.sqrt(x)

def faktoriyel(x):
    if x < 0:
        return "Negatif sayının faktoriyeli hesaplanamaz!"
    if x == 0:
        return 1
    return math.factorial(int(x))

print("🧮 Gelişmiş Hesap Makinesine Hoş Geldiniz! 🧮")

while True:
    print("\nİşlemler:")
    print("1. Toplama ➕")
    print("2. Çıkarma ➖")
    print("3. Çarpma ✖️")
    print("4. Bölme ➗")
    print("5. Üs Alma 📈")
    print("6. Karekök 📊")
    print("7. Faktoriyel ‼️")
    print("8. Çıkış 🚪")
    
    secim = input("\nYapmak istediğiniz işlemin numarasını girin (1-8): ")
    
    if secim == '8':
        print("\n👋 Hesap makinesini kullandığınız için teşekkürler!")
        break
        
    try:
        if secim in ['6', '7']:
            sayi = float(input("Sayıyı girin: "))
            if secim == '6':
                sonuc = karekok(sayi)
            else:
                sonuc = faktoriyel(sayi)
        else:
            sayi1 = float(input("İlk sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
            
            if secim == '1':
                sonuc = toplama(sayi1, sayi2)
            elif secim == '2':
                sonuc = cikarma(sayi1, sayi2)
            elif secim == '3':
                sonuc = carpma(sayi1, sayi2)
            elif secim == '4':
                sonuc = bolme(sayi1, sayi2)
            elif secim == '5':
                sonuc = us_alma(sayi1, sayi2)
            else:
                print("❌ Geçersiz seçim!")
                continue
                
        if isinstance(sonuc, str):
            print(f"\n⚠️ Hata: {sonuc}")
        else:
            print(f"\n🎯 Sonuç: {sonuc}")
            
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin!")
    except Exception as e:
        print(f"❌ Bir hata oluştu: {str(e)}")
        
    devam = input("\nBaşka bir işlem yapmak ister misiniz? (e/h): ").lower()
    if devam != 'e':
        print("\n👋 Hesap makinesini kullandığınız için teşekkürler!")
        break 