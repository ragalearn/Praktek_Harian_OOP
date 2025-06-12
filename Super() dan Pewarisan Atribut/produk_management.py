import re
from colorama import Fore, Style, init
init(autoreset=True)

# ========== CLASS HIERARCHY ==========
class Produk:
    def __init__(self, nama, harga):
        if not self._validate_nama(nama):
            raise ValueError("Nama hanya boleh mengandung huruf, angka, dan spasi!")
        if not self._validate_harga(harga):
            raise ValueError("Harga harus antara 1.000 - 10.000.000.000")
        
        self.nama = nama.strip()
        self.harga = harga
    
    def _validate_nama(self, nama):
        return bool(re.match(r'^[\w\s]+$', nama.strip()))
    
    def _validate_harga(self, harga):
        return isinstance(harga, (int, float)) and 1000 <= harga <= 10_000_000_000
    
    def __str__(self):
        return (
            f"{Fore.CYAN}Nama:{Style.RESET_ALL} {self.nama}\n"
            f"{Fore.GREEN}Harga:{Style.RESET_ALL} Rp {self.harga:,}\n"
            f"{Fore.YELLOW}Jenis:{Style.RESET_ALL} Produk Umum"
        )

class Elektronik(Produk):
    def __init__(self, nama, harga, garansi):
        super().__init__(nama, harga)
        if not self._validate_garansi(garansi):
            raise ValueError("Garansi harus 1-36 bulan")
        self.garansi = garansi
    
    def _validate_garansi(self, garansi):
        return isinstance(garansi, int) and 1 <= garansi <= 36
    
    def __str__(self):
        base_str = super().__str__()
        return (
            f"{base_str.replace('Produk Umum', 'Elektronik')}\n"
            f"{Fore.MAGENTA}Garansi:{Style.RESET_ALL} {self.garansi} bulan"
        )

class ElektronikDigital(Elektronik):
    def __init__(self, nama, harga, garansi, lisensi):
        super().__init__(nama, harga, garansi)
        if not self._validate_lisensi(lisensi):
            raise ValueError("Lisensi harus format 'ABC-123'")
        self.lisensi = lisensi
    
    def _validate_lisensi(self, lisensi):
        return bool(re.match(r'^[A-Z]{3}-\d{3}$', lisensi))
    
    def __str__(self):
        base_str = super().__str__()
        return (
            f"{base_str}\n"
            f"{Fore.BLUE}Lisensi:{Style.RESET_ALL} {self.lisensi}"
        )

# ========== CRUD FUNCTIONS ==========
daftar_produk = []

def tambah_produk():
    print(f"\n{Fore.YELLOW}=== TAMBAH PRODUK ===")
    try:
        jenis = input("Jenis produk (1. Umum | 2. Elektronik | 3. Digital): ")
        
        nama = input("Nama produk: ")
        harga = float(input("Harga: Rp "))
        
        if jenis == "1":
            produk = Produk(nama, harga)
        elif jenis == "2":
            garansi = int(input("Garansi (bulan): "))
            produk = Elektronik(nama, harga, garansi)
        elif jenis == "3":
            garansi = int(input("Garansi (bulan): "))
            lisensi = input("Lisensi (format ABC-123): ").upper()
            produk = ElektronikDigital(nama, harga, garansi, lisensi)
        else:
            print(f"{Fore.RED}Jenis tidak valid!")
            return
            
        daftar_produk.append(produk)
        print(f"{Fore.GREEN}Produk berhasil ditambahkan!")
    
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}")

def lihat_produk():
    print(f"\n{Fore.YELLOW}=== DAFTAR PRODUK ===")
    if not daftar_produk:
        print(f"{Fore.RED}Tidak ada produk")
        return
    
    for idx, produk in enumerate(daftar_produk, 1):
        print(f"\n{Fore.CYAN}Produk #{idx}")
        print(produk)

def edit_produk():
    lihat_produk()
    if not daftar_produk:
        return
    
    try:
        pilihan = int(input("\nPilih nomor produk yang akan diedit: ")) - 1
        if 0 <= pilihan < len(daftar_produk):
            produk = daftar_produk[pilihan]
            print(f"\n{Fore.YELLOW}Edit Produk:")
            print(produk)
            
            nama_baru = input(f"\nNama baru [{produk.nama}]: ") or produk.nama
            harga_baru = float(input(f"Harga baru [Rp {produk.harga:,}]: ") or produk.harga)
            
            if isinstance(produk, Elektronik):
                garansi_baru = int(input(f"Garansi baru [{produk.garansi} bulan]: ") or produk.garansi)
                
                if isinstance(produk, ElektronikDigital):
                    lisensi_baru = input(f"Lisensi baru [{produk.lisensi}]: ").upper() or produk.lisensi
                    daftar_produk[pilihan] = ElektronikDigital(nama_baru, harga_baru, garansi_baru, lisensi_baru)
                else:
                    daftar_produk[pilihan] = Elektronik(nama_baru, harga_baru, garansi_baru)
            else:
                daftar_produk[pilihan] = Produk(nama_baru, harga_baru)
            
            print(f"{Fore.GREEN}Produk berhasil diupdate!")
        else:
            print(f"{Fore.RED}Nomor tidak valid!")
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}")

def hapus_produk():
    lihat_produk()
    if not daftar_produk:
        return
    
    try:
        pilihan = int(input("\nPilih nomor produk yang akan dihapus: ")) - 1
        if 0 <= pilihan < len(daftar_produk):
            deleted = daftar_produk.pop(pilihan)
            print(f"{Fore.GREEN}Produk '{deleted.nama}' dihapus!")
        else:
            print(f"{Fore.RED}Nomor tidak valid!")
    except ValueError:
        print(f"{Fore.RED}Input harus angka!")

# ========== MAIN MENU ==========
def main():
    while True:
        print(f"\n{Fore.BLUE}=== MENU UTAMA ===")
        print(f"{Fore.WHITE}1. Tambah Produk")
        print(f"{Fore.WHITE}2. Lihat Produk")
        print(f"{Fore.WHITE}3. Edit Produk")
        print(f"{Fore.WHITE}4. Hapus Produk")
        print(f"{Fore.WHITE}5. Keluar")
        
        pilihan = input(f"{Fore.YELLOW}Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            lihat_produk()
        elif pilihan == "3":
            edit_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            print(f"{Fore.GREEN}Program selesai.")
            break
        else:
            print(f"{Fore.RED}Pilihan tidak valid!")

if __name__ == "__main__":
    main()