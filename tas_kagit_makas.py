import random
import time

def oyun_durumu(oyuncu_skor, bilgisayar_skor):
    print(f"\n📊 SKOR DURUMU:")
    print(f"Sizin skorunuz: {oyuncu_skor} 👤")
    print(f"Bilgisayarın skoru: {bilgisayar_skor} 🤖")

secenekler = ["taş", "kağıt", "makas"]
emoji_map = {"taş": "🪨", "kağıt": "📄", "makas": "✂️"}
oyuncu_skor = 0
bilgisayar_skor = 0

print("🎮 Taş-Kağıt-Makas Oyununa Hoş Geldiniz! 🎮")
print("Çıkmak için 'q' yazın")

while True:
    print("\nSeçenekler: taş, kağıt, makas")
    oyuncu_secim = input("Seçiminizi yapın: ").lower()
    
    if oyuncu_secim == 'q':
        print("\n🎯 Final Skoru:")
        oyun_durumu(oyuncu_skor, bilgisayar_skor)
        print("👋 Oynadığınız için teşekkürler!")
        break
        
    if oyuncu_secim not in secenekler:
        print("❌ Geçersiz seçim! Lütfen taş, kağıt veya makas seçin.")
        continue
        
    print("\n🎲 Bilgisayar seçim yapıyor", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()
    
    bilgisayar_secim = random.choice(secenekler)
    
    print(f"\nSizin seçiminiz: {oyuncu_secim} {emoji_map[oyuncu_secim]}")
    print(f"Bilgisayarın seçimi: {bilgisayar_secim} {emoji_map[bilgisayar_secim]}")
    
    if oyuncu_secim == bilgisayar_secim:
        print("🤝 Berabere!")
    elif (
        (oyuncu_secim == "taş" and bilgisayar_secim == "makas") or
        (oyuncu_secim == "kağıt" and bilgisayar_secim == "taş") or
        (oyuncu_secim == "makas" and bilgisayar_secim == "kağıt")
    ):
        print("🎉 Kazandınız!")
        oyuncu_skor += 1
    else:
        print("😔 Bilgisayar kazandı!")
        bilgisayar_skor += 1
    
    oyun_durumu(oyuncu_skor, bilgisayar_skor) 