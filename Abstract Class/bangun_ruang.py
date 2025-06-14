from abc import ABC, abstractmethod
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

# ===== ABSTRACT CLASS =====
class BangunRuang(ABC):
    @abstractmethod
    def volume(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    
    @staticmethod
    def _validate_input(*args):
        """Method validasi dasar untuk semua bangun ruang"""
        if any(not isinstance(x, (int, float)) or x <= 0 for x in args):
            raise ValueError("Input harus bilangan positif")

# ===== SUBCLASS IMPLEMENTATIONS =====
class Kubus(BangunRuang):
    def __init__(self, sisi):
        self._validate_input(sisi)  # Perhatikan nama method tanpa spasi
        self.sisi = sisi
    
    def volume(self):
        return self.sisi ** 3
    
    def __str__(self):
        return f"KUBUS | Sisi: {self.sisi:.2f} | Volume: {self.volume():.2f}"

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self._validate_input(panjang, lebar, tinggi)
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def volume(self):
        return self.panjang * self.lebar * self.tinggi
    
    def __str__(self):
        return f"BALOK\t| P×L×T: {self.panjang:.2f}×{self.lebar:.2f}×{self.tinggi:.2f}\t| Volume: {self.volume():.2f}"

class Lingkaran(BangunRuang):
    def __init__(self, jari_jari):
        self._validate_input(jari_jari)
        self.jari_jari = jari_jari
    
    def volume(self):
        return 3.14159 * (self.jari_jari ** 2)
    
    def __str__(self):
        return f"LINGKARAN\t| Jari-jari: {self.jari_jari:.2f}\t| Luas: {self.volume():.2f}"

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self._validate_input(jari_jari, tinggi)
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def volume(self):
        return 3.14159 * (self.jari_jari ** 2) * self.tinggi
    
    def __str__(self):
        return f"TABUNG\t| r×t: {self.jari_jari:.2f}×{self.tinggi:.2f}\t| Volume: {self.volume():.2f}"

    @staticmethod
    def _validate_input(*args):
        if any(not isinstance(x, (int, float)) or x <= 0 for x in args):
            raise ValueError("Input harus bilangan positif")

# ===== HISTORY MANAGEMENT (TXT FORMAT) =====
class HistoryManager:
    FILE_NAME = "riwayat_perhitungan.txt"
    
    @staticmethod
    def save_to_history(calculation):
        try:
            with open(HistoryManager.FILE_NAME, 'a') as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
                f.write(f"{str(calculation)}\n")
                f.write("-" * 50 + "\n")
        except Exception as e:
            print(f"{Fore.RED}Gagal menyimpan riwayat: {e}")

    @staticmethod
    def show_history():
        try:
            with open(HistoryManager.FILE_NAME, 'r') as f:
                print(f"\n{Fore.CYAN}=== RIWAYAT PERHITUNGAN ===\n")
                print(f.read())
        except FileNotFoundError:
            print(f"{Fore.YELLOW}Tidak ada riwayat perhitungan")

# ===== USER INTERFACE =====
def input_bangun_ruang():
    print(f"\n{Fore.YELLOW}=== PILIH BANGUN RUANG ===")
    print(f"{Fore.CYAN}1. Kubus")
    print(f"{Fore.CYAN}2. Balok")
    print(f"{Fore.CYAN}3. Lingkaran (2D)")
    print(f"{Fore.CYAN}4. Tabung")
    
    pilihan = input("Pilih bangun (1-4): ")
    
    try:
        if pilihan == "1":
            sisi = float(input("Masukkan panjang sisi: "))
            return Kubus(sisi)
        elif pilihan == "2":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            tinggi = float(input("Masukkan tinggi: "))
            return Balok(panjang, lebar, tinggi)
        elif pilihan == "3":
            jari_jari = float(input("Masukkan jari-jari: "))
            return Lingkaran(jari_jari)
        elif pilihan == "4":
            jari_jari = float(input("Masukkan jari-jari: "))
            tinggi = float(input("Masukkan tinggi: "))
            return Tabung(jari_jari, tinggi)
        else:
            print(f"{Fore.RED}Pilihan tidak valid!")
            return None
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}")
        return None

def main_menu():
    while True:
        print(f"\n{Fore.BLUE}=== APLIKASI PERHITUNGAN BANGUN RUANG ===")
        print(f"{Fore.WHITE}1. Hitung Volume/Luas")
        print(f"{Fore.WHITE}2. Lihat Riwayat")
        print(f"{Fore.WHITE}3. Keluar")
        
        choice = input(f"{Fore.YELLOW}Pilih menu (1-3): ")
        
        if choice == "1":
            bangun = input_bangun_ruang()
            if bangun:
                print(f"\n{Fore.GREEN}=== HASIL ===")
                print(bangun)
                HistoryManager.save_to_history(bangun)
        elif choice == "2":
            HistoryManager.show_history()
        elif choice == "3":
            print(f"{Fore.GREEN}Terima kasih! Program selesai.")
            break
        else:
            print(f"{Fore.RED}Pilihan tidak valid!")

if __name__ == "__main__":
    main_menu()