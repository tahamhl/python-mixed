class HanoiKuleleri:
    def __init__(self):
        self.hamle_sayisi = 0
        self.hamleler = []
    
    def coz(self, n, kaynak="A", hedef="C", yardimci="B"):
        """
        Hanoi Kuleleri problemini çözen özyinelemeli fonksiyon
        
        Parametreler:
        n: disk sayısı
        kaynak: başlangıç çubuğu (varsayılan "A")
        hedef: hedef çubuk (varsayılan "C")
        yardimci: yardımcı çubuk (varsayılan "B")
        """
        if n == 1:
            self.hamle_yap(1, kaynak, hedef)
            return
        
        # n-1 diski kaynaktan yardımcıya taşı
        self.coz(n-1, kaynak, yardimci, hedef)
        
        # n. diski kaynaktan hedefe taşı
        self.hamle_yap(n, kaynak, hedef)
        
        # n-1 diski yardımcıdan hedefe taşı
        self.coz(n-1, yardimci, hedef, kaynak)
    
    def hamle_yap(self, disk, kaynak, hedef):
        """Disk hareketini kaydet ve hamle sayısını güncelle"""
        self.hamle_sayisi += 1
        self.hamleler.append(f"Hamle {self.hamle_sayisi}: Disk {disk} → {kaynak}'dan {hedef}'ye taşındı")
    
    def sonuclari_goster(self):
        """Çözüm sonuçlarını görüntüle"""
        print(f"Toplam hamle sayısı: {self.hamle_sayisi}")
        print("Hamleler:")
        for hamle in self.hamleler:
            print(hamle)
        print(f"Teori ile uyumlu: {self.hamle_sayisi == (2**len(self.hamleler)//self.hamle_sayisi) - 1}")

# Test edelim
def main():
    hanoi = HanoiKuleleri()
    disk_sayisi = 3
    
    print(f"{disk_sayisi} diskli Hanoi Kuleleri problemi çözülüyor...")
    hanoi.coz(disk_sayisi)
    hanoi.sonuclari_goster()

if __name__ == "__main__":
    main()