import json
from datetime import datetime

class Matematika:
    RIWAYAT_FILE = "riwayat_matematika.txt"
    
    @staticmethod
    def kuadrat(x):
        return x ** 2
    
    @staticmethod
    def akar(x):
        return x ** 0.5
    
    @staticmethod
    def faktorial(x):
        if x == 0:
            return 1
        return x * Matematika.faktorial(x-1)
    
    @staticmethod
    def logaritma(x, basis=10):
        import math
        return math.log(x, basis)
    
    @classmethod
    def info(cls):
        info_text = f"""
=== INFORMASI CLASS {cls.__name__} ===
Static Methods:
1. kuadrat(x)   - Menghitung x pangkat 2
2. akar(x)      - Menghitung akar kuadrat
3. faktorial(x) - Menghitung factorial
4. logaritma(x, [basis]) - Menghitung logaritma

Class Methods:
1. info()       - Menampilkan informasi ini
"""
        print(info_text)

    @classmethod
    def simpan_riwayat(cls, operasi, hasil):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(cls.RIWAYAT_FILE, 'a') as f:
            f.write(f"[{timestamp}] {operasi} = {hasil}\n")

    @classmethod
    def tampilkan_riwayat(cls):
        try:
            with open(cls.RIWAYAT_FILE, 'r') as f:
                print("\n=== RIWAYAT PERHITUNGAN ===")
                print(f.read())
        except FileNotFoundError:
            print("\nBelum ada riwayat perhitungan")

def main():
    print("=== SUPER KALKULATOR MATEMATIKA ===")
    
    while True:
        print("\nMenu Operasi:")
        print("1. Kuadrat")
        print("2. Akar Kuadrat")
        print("3. Faktorial")
        print("4. Logaritma")
        print("5. Lihat Riwayat")
        print("6. Info Class")
        print("7. Keluar")
        
        pilihan = input("Pilih operasi (1-7): ")
        
        if pilihan == '7':
            print("Program selesai.")
            break
        
        try:
            if pilihan in ['1', '2', '3', '4']:
                x = float(input("Masukkan angka: "))
                
                if pilihan == '1':
                    hasil = Matematika.kuadrat(x)
                    operasi = f"Kuadrat({x})"
                elif pilihan == '2':
                    hasil = Matematika.akar(x)
                    operasi = f"Akar({x})"
                elif pilihan == '3':
                    hasil = Matematika.faktorial(int(x))
                    operasi = f"Faktorial({int(x)})"
                elif pilihan == '4':
                    basis = float(input("Masukkan basis logaritma (default 10): ") or "10")
                    hasil = Matematika.logaritma(x, basis)
                    operasi = f"Log_{basis}({x})"
                
                print(f"Hasil: {operasi} = {hasil}")
                Matematika.simpan_riwayat(operasi, hasil)
            
            elif pilihan == '5':
                Matematika.tampilkan_riwayat()
            elif pilihan == '6':
                Matematika.info()
            else:
                print("Pilihan tidak valid!")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()