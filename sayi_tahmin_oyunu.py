import random

print("🎮 Sayı Tahmin Oyununa Hoş Geldiniz! 🎮")
print("1 ile 100 arasında bir sayı tuttum.")

tutulan_sayi = random.randint(1, 100)
tahmin_sayisi = 0
max_tahmin = 10

while tahmin_sayisi < max_tahmin:
    try:
        tahmin = int(input(f"\nTahmininizi girin (Kalan hak: {max_tahmin - tahmin_sayisi}): "))
        tahmin_sayisi += 1
        
        if tahmin < tutulan_sayi:
            print("📈 Daha YÜKSEK bir sayı söyleyin!")
        elif tahmin > tutulan_sayi:
            print("📉 Daha DÜŞÜK bir sayı söyleyin!")
        else:
            print(f"\n🎉 TEBRİKLER! {tahmin_sayisi}. denemede bildiniz!")
            break
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin!")
        tahmin_sayisi -= 1

if tahmin_sayisi == max_tahmin and tahmin != tutulan_sayi:
    print(f"\n😔 Üzgünüm, hakkınız bitti. Tutulan sayı: {tutulan_sayi}") 