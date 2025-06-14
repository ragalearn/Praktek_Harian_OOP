import re
from colorama import Fore, Style, init
init(autoreset=True)

# ========== CLASS HIERARCHY ==========
class MakhlukHidup:
    def __init__(self, nama, jenis_habitat):
        if not self._validasi_nama(nama):
            raise ValueError("Nama harus berupa huruf dan spasi (min 3 karakter)")
        if not jenis_habitat.strip():
            raise ValueError("Habitat tidak boleh kosong")
        
        self.nama = nama.strip()
        self.jenis_habitat = jenis_habitat.strip()
    
    def _validasi_nama(self, nama):
        return bool(re.match(r'^[a-zA-Z\s]{3,}$', nama.strip()))
    
    def info(self):
        return f"{Fore.CYAN}Nama:{Style.RESET_ALL} {self.nama} | {Fore.GREEN}Habitat:{Style.RESET_ALL} {self.jenis_habitat}"

class Hewan(MakhlukHidup):
    def __init__(self, nama, jenis_habitat, jumlah_kaki):
        super().__init__(nama, jenis_habitat)
        if not self._validasi_kaki(jumlah_kaki):
            raise ValueError("Jumlah kaki harus 0-8 (angka bulat)")
        
        self.jumlah_kaki = jumlah_kaki
    
    def _validasi_kaki(self, jumlah_kaki):
        return isinstance(jumlah_kaki, int) and 0 <= jumlah_kaki <= 8
    
    def info(self):
        return super().info() + f" | {Fore.YELLOW}Kaki:{Style.RESET_ALL} {self.jumlah_kaki}"

class Kucing(Hewan):
    def __init__(self, nama, jenis_habitat, jumlah_kaki, ras, warna_bulu):
        super().__init__(nama, jenis_habitat, jumlah_kaki)
        if not self._validasi_ras(ras):
            raise ValueError("Ras harus berupa huruf (contoh: Persia)")
        if not warna_bulu.strip():
            raise ValueError("Warna bulu tidak boleh kosong")
        
        self.ras = ras.strip()
        self.warna_bulu = warna_bulu.strip()
    
    def _validasi_ras(self, ras):
        return bool(re.match(r'^[a-zA-Z\s]+$', ras.strip()))
    
    def info(self):
        return super().info() + f" | {Fore.MAGENTA}Ras:{Style.RESET_ALL} {self.ras} | {Fore.BLUE}Warna:{Style.RESET_ALL} {self.warna_bulu}"

class KucingLiarkucing(Kucing):
    def __init__(self, nama, jenis_habitat, jumlah_kaki, ras, warna_bulu, mangsa_favorit):
        super().__init__(nama, jenis_habitat, jumlah_kaki, ras, warna_bulu)
        if not self._validasi_mangsa(mangsa_favorit):
            raise ValueError("Mangsa favorit harus berupa huruf (contoh: Tikus)")
        
        self.mangsa_favorit = mangsa_favorit.strip()
    
    def _validasi_mangsa(self, mangsa):
        return bool(re.match(r'^[a-zA-Z\s]+$', mangsa.strip()))
    
    def info(self):
        return super().info() + f" | {Fore.RED}Mangsa:{Style.RESET_ALL} {self.mangsa_favorit}"

# ========== CRUD OPERATIONS ==========
daftar_kucing = []

def tambah_kucing():
    print(f"\n{Fore.YELLOW}=== TAMBAH DATA KUCING ===")
    try:
        jenis = input("Jenis kucing (1. Domestik / 2. Liarkucing): ").strip()
        
        nama = input("Nama kucing: ")
        habitat = input("Habitat: ")
        kaki = int(input("Jumlah kaki (0-8): "))
        ras = input("Ras: ")
        warna = input("Warna bulu: ")
        
        if jenis == "2":
            mangsa = input("Mangsa favorit: ")
            kucing = KucingLiarkucing(nama, habitat, kaki, ras, warna, mangsa)
        else:
            kucing = Kucing(nama, habitat, kaki, ras, warna)
        
        daftar_kucing.append(kucing)
        print(f"{Fore.GREEN}Data kucing berhasil ditambahkan!")
    
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}")

def lihat_kucing():
    print(f"\n{Fore.YELLOW}=== DAFTAR KUCING ===")
    if not daftar_kucing:
        print(f"{Fore.RED}Tidak ada data kucing")
        return
    
    for idx, kucing in enumerate(daftar_kucing, 1):
        print(f"\n{Fore.CYAN}[{idx}] {kucing.nama}")
        print(kucing.info())

def edit_kucing():
    lihat_kucing()
    if not daftar_kucing:
        return
    
    try:
        nomor = int(input("\nPilih nomor kucing yang akan diedit: ")) - 1
        if 0 <= nomor < len(daftar_kucing):
            kucing = daftar_kucing[nomor]
            
            print(f"\n{Fore.YELLOW}Edit Data Kucing:")
            print(kucing.info())
            
            # Input data baru (jika kosong gunakan nilai lama)
            nama_baru = input(f"\nNama baru [{kucing.nama}]: ") or kucing.nama
            habitat_baru = input(f"Habitat baru [{kucing.jenis_habitat}]: ") or kucing.jenis_habitat
            kaki_baru = input(f"Jumlah kaki baru [{kucing.jumlah_kaki}]: ") or kucing.jumlah_kaki
            ras_baru = input(f"Ras baru [{kucing.ras}]: ") or kucing.ras
            warna_baru = input(f"Warna bulu baru [{kucing.warna_bulu}]: ") or kucing.warna_bulu
            
            if isinstance(kucing, KucingLiarkucing):
                mangsa_baru = input(f"Mangsa favorit baru [{kucing.mangsa_favorit}]: ") or kucing.mangsa_favorit
                daftar_kucing[nomor] = KucingLiarkucing(nama_baru, habitat_baru, int(kaki_baru), ras_baru, warna_baru, mangsa_baru)
            else:
                daftar_kucing[nomor] = Kucing(nama_baru, habitat_baru, int(kaki_baru), ras_baru, warna_baru)
            
            print(f"{Fore.GREEN}Data berhasil diupdate!")
        else:
            print(f"{Fore.RED}Nomor tidak valid!")
    except ValueError:
        print(f"{Fore.RED}Input harus angka!")

def hapus_kucing():
    lihat_kucing()
    if not daftar_kucing:
        return
    
    try:
        nomor = int(input("\nPilih nomor kucing yang akan dihapus: ")) - 1
        if 0 <= nomor < len(daftar_kucing):
            deleted = daftar_kucing.pop(nomor)
            print(f"{Fore.GREEN}Kucing {deleted.nama} berhasil dihapus!")
        else:
            print(f"{Fore.RED}Nomor tidak valid!")
    except ValueError:
        print(f"{Fore.RED}Input harus angka!")

# ========== MAIN MENU ==========
def main():
    while True:
        print(f"\n{Fore.BLUE}=== MENU MANAJEMEN KUCING ===")
        print(f"{Fore.WHITE}1. Tambah Kucing")
        print(f"{Fore.WHITE}2. Lihat Semua Kucing")
        print(f"{Fore.WHITE}3. Edit Data Kucing")
        print(f"{Fore.WHITE}4. Hapus Kucing")
        print(f"{Fore.WHITE}5. Keluar")
        
        pilihan = input(f"{Fore.YELLOW}Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_kucing()
        elif pilihan == "2":
            lihat_kucing()
        elif pilihan == "3":
            edit_kucing()
        elif pilihan == "4":
            hapus_kucing()
        elif pilihan == "5":
            print(f"{Fore.GREEN}Program selesai. Data tersimpan!")
            break
        else:
            print(f"{Fore.RED}Pilihan tidak valid!")

if __name__ == "__main__":
    main()