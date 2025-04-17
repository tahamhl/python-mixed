import random

kelimeler = [
    "python", "programlama", "bilgisayar", "algoritma", "yazılım",
    "geliştirici", "internet", "teknoloji", "veritabanı", "uygulama"
]

def kelime_karistir(kelime):
    kelime_liste = list(kelime)
    random.shuffle(kelime_liste)
    return "".join(kelime_liste)

def ipucu_ver(kelime, gosterilen_harfler):
    ipucu = ""
    for i, harf in enumerate(kelime):
        if i < gosterilen_harfler:
            ipucu += harf
        else:
            ipucu += "_"
    return ipucu

print("🎯 Kelime Karıştırma Oyununa Hoş Geldiniz! 🎯")
print("Karışık harflerden doğru kelimeyi bulun.")

skor = 0
ipucu_hakki = 3

while kelimeler:
    secilen_kelime = random.choice(kelimeler)
    karisik_kelime = kelime_karistir(secilen_kelime)
    kelimeler.remove(secilen_kelime)
    
    print(f"\n🎲 Karışık kelime: {karisik_kelime}")
    
    tahmin_hakki = 3
    ipucu_sayisi = 0
    
    while tahmin_hakki > 0:
        tahmin = input(f"\nTahmininiz (Kalan hak: {tahmin_hakki}, İpucu hakkı: {ipucu_hakki}): ").lower()
        
        if tahmin == "ipucu" and ipucu_hakki > 0:
            ipucu_sayisi += 1
            ipucu_hakki -= 1
            print(f"💡 İpucu: {ipucu_ver(secilen_kelime, ipucu_sayisi)}")
            continue
            
        if tahmin == secilen_kelime:
            print("🎉 Tebrikler! Doğru bildiniz!")
            skor += tahmin_hakki
            break
        else:
            tahmin_hakki -= 1
            if tahmin_hakki > 0:
                print(f"❌ Yanlış tahmin. {tahmin_hakki} hakkınız kaldı.")
            else:
                print(f"😔 Üzgünüm, doğru kelime: {secilen_kelime}")
    
    if not kelimeler:
        print("\n🎮 Oyun bitti!")
        print(f"📊 Toplam skorunuz: {skor}")
        print("👋 Oynadığınız için teşekkürler!")
        break
        
    devam = input("\nDevam etmek istiyor musunuz? (e/h): ").lower()
    if devam != 'e':
        print(f"\n🎮 Oyun bitti!")
        print(f"📊 Toplam skorunuz: {skor}")
        print("👋 Oynadığınız için teşekkürler!")
        break 