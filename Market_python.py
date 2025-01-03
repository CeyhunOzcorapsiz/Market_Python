import os

class Market:
    def __init__(self):
       
        self.dosya_adi = "urunler.txt"
        if not os.path.exists(self.dosya_adi):
            with open(self.dosya_adi, 'w') as dosya:
                pass  

    def __del__(self):
      
        print("Market sınıfı sonlandı.")

    def urunleri_listele(self):
  
        try:
            with open(self.dosya_adi, 'r') as dosya:
                satirlar = dosya.read().splitlines()
                if not satirlar:
                    print("Ürün listesi boş.")
                else:
                    print("\n*** Ürün Listesi ***")
                    for i, satir in enumerate(satirlar, 1):
                        ad, kategori, fiyat, stok = satir.split(',')
                        print(f"{i}. Ürün: {ad}, Kategori: {kategori}, Fiyat: {fiyat} TL, Stok: {stok}")
        except Exception as hata:
            print(f"Bir hata oluştu: {hata}")

    def urun_ekle(self):
        
        try:
            ad = input("Ürün adı: ")
            kategori = input("Kategori: ")
            fiyat = input("Fiyat: ")
            stok = input("Stok miktarı: ")

            with open(self.dosya_adi, 'a') as dosya:
                dosya.write(f"{ad},{kategori},{fiyat},{stok}\n")
            print("Ürün başarıyla eklendi!")
        except Exception as hata:
            print(f"Bir hata oluştu: {hata}")

    def urun_sil(self):
       
        try:
            with open(self.dosya_adi, 'r') as dosya:
                satirlar = dosya.read().splitlines()

            if not satirlar:
                print("Ürün listesi boş, silinecek ürün yok.")
                return

            self.urunleri_listele()
            secim = int(input("Silmek istediğiniz ürün numarasını girin: "))

            if 1 <= secim <= len(satirlar):
                del satirlar[secim - 1]
                with open(self.dosya_adi, 'w') as dosya:
                    for satir in satirlar:
                        dosya.write(satir + '\n')
                print("Ürün başarıyla silindi!")
            else:
                print("Geçersiz ürün numarası.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
        except Exception as hata:
            print(f"Bir hata oluştu: {hata}")


def menu():
    
    market = Market()

    while True:
        print("\n*** MENÜ ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            market.urunleri_listele()
        elif secim == "2":
            market.urun_ekle()
        elif secim == "3":
            market.urun_sil()
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
