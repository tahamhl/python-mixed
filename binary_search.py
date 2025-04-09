import tkinter as tk
import time

class TahminOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Yapay Zeka Tahmin Oyunu")

        self.low = 1
        self.high = 100
        self.tahmin_sayisi = 0
        self.tahmin = (self.low + self.high) // 2

        # Başlık
        self.label = tk.Label(root, text="Bir sayı tutun ve AI'nin tahmin etmesini sağlayın!", font=("Arial", 12))
        self.label.pack(pady=10)

        # Tahmin metni
        self.tahmin_label = tk.Label(root, text=f"Benim tahminim: {self.tahmin}", font=("Arial", 16, "bold"))
        self.tahmin_label.pack(pady=10)

        # Çubuk grafik (Tahmin yüzdesi)
        self.canvas = tk.Canvas(root, width=200, height=20, bg="white", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.progress_bar = self.canvas.create_rectangle(0, 0, 2, 20, fill="blue")

        # Butonlar
        self.btn_yukari = tk.Button(root, text="Daha Büyük", font=("Arial", 12), bg="lightblue", command=self.daha_buyuk)
        self.btn_yukari.pack(pady=5)
        self.btn_yukari.bind("<Enter>", lambda e: self.btn_yukari.config(bg="blue"))
        self.btn_yukari.bind("<Leave>", lambda e: self.btn_yukari.config(bg="lightblue"))

        self.btn_asagi = tk.Button(root, text="Daha Küçük", font=("Arial", 12), bg="lightcoral", command=self.daha_kucuk)
        self.btn_asagi.pack(pady=5)
        self.btn_asagi.bind("<Enter>", lambda e: self.btn_asagi.config(bg="red"))
        self.btn_asagi.bind("<Leave>", lambda e: self.btn_asagi.config(bg="lightcoral"))

        self.btn_dogru = tk.Button(root, text="Doğru", font=("Arial", 12), bg="lightgreen", command=self.dogru)
        self.btn_dogru.pack(pady=10)
        self.btn_dogru.bind("<Enter>", lambda e: self.btn_dogru.config(bg="green"))
        self.btn_dogru.bind("<Leave>", lambda e: self.btn_dogru.config(bg="lightgreen"))

        # Sonuç etiketi
        self.sonuc_label = tk.Label(root, text="", font=("Arial", 14, "italic"))
        self.sonuc_label.pack(pady=10)

    def guncelle_tahmin(self):
        self.tahmin = (self.low + self.high) // 2
        self.tahmin_label.config(text=f"Benim tahminim: {self.tahmin}")

        # Çubuk grafiği güncelle
        progress = (self.tahmin - 1) / 100 * 200
        self.canvas.coords(self.progress_bar, 0, 0, progress, 20)

    def daha_buyuk(self):
        self.low = self.tahmin + 1
        self.tahmin_sayisi += 1
        self.guncelle_tahmin()

    def daha_kucuk(self):
        self.high = self.tahmin - 1
        self.tahmin_sayisi += 1
        self.guncelle_tahmin()

    def dogru(self):
        self.tahmin_sayisi += 1
        self.sonuc_label.config(text=f"🎉 AI {self.tahmin_sayisi} denemede bildi!", fg="green")
        self.btn_yukari.config(state="disabled")
        self.btn_asagi.config(state="disabled")
        self.btn_dogru.config(state="disabled")

        # Kazanma efektini başlat
        self.kazanma_efekti()

    def kazanma_efekti(self):
        for _ in range(10):
            self.sonuc_label.config(fg="red")
            self.root.update()
            time.sleep(0.2)
            self.sonuc_label.config(fg="blue")
            self.root.update()
            time.sleep(0.2)

if __name__ == "__main__":
    root = tk.Tk()
    app = TahminOyunu(root)
    root.mainloop()
