class Pegawai:
    def __init__(self, id_pegawai, nama, jabatan):
        if not str(id_pegawai).isdigit():
            raise ValueError("ID Pegawai harus angka!")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong!")
        
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
    
    def gaji(self):
        return "Gaji pegawai standar"
    
    def tunjangan(self):
        return 0
    
    def hitung_bonus(self, performa):
        if not (0 <= performa <= 100):
            raise ValueError("Performa harus antara 0-100!")
        return performa * 100
    
    def __str__(self):
        return (
            f"\n=== Informasi Pegawai ===\n"
            f"ID: {self.id_pegawai}\n"
            f"Nama: {self.nama}\n"
            f"Jabatan: {self.jabatan}\n"
            f"Gaji: {self.gaji()}\n"
            f"Tunjangan: Rp {self.tunjangan():,}\n"
        )

class Manager(Pegawai):
    def gaji(self):
        return "Gaji manajer lebih tinggi"
    
    def tunjangan(self):
        return 5_000_000
    
    def hitung_bonus(self, performa):
        return super().hitung_bonus(performa) * 1.5

class Direktur(Manager):
    def gaji(self):
        return "Gaji direktur paling tinggi"
    
    def tunjangan(self):
        return 10_000_000
    
    def hitung_bonus(self, performa):
        return super().hitung_bonus(performa) * 2

# Database sederhana
daftar_pegawai = []

def input_pegawai():
    while True:
        try:
            print("\n=== Tambah Pegawai ===")
            id_pegawai = input("ID Pegawai (angka): ").strip()
            nama = input("Nama: ").strip()
            jabatan = input("Jabatan (Pegawai/Manager/Direktur): ").strip().capitalize()
            
            if jabatan == "Pegawai":
                pegawai = Pegawai(id_pegawai, nama, jabatan)
            elif jabatan == "Manager":
                pegawai = Manager(id_pegawai, nama, jabatan)
            elif jabatan == "Direktur":
                pegawai = Direktur(id_pegawai, nama, jabatan)
            else:
                print("Error: Jabatan tidak valid!")
                continue
            
            daftar_pegawai.append(pegawai)
            print(f"\nBerhasil menambahkan {nama}!")
            return pegawai
            
        except ValueError as e:
            print(f"Error: {e}")

def hitung_bonus_pegawai():
    if not daftar_pegawai:
        print("\nBelum ada data pegawai!")
        return
    
    print("\n=== Hitung Bonus ===")
    tampilkan_semua_pegawai()
    
    try:
        id_pegawai = input("\nMasukkan ID Pegawai: ").strip()
        pegawai = next((p for p in daftar_pegawai if p.id_pegawai == id_pegawai), None)
        
        if not pegawai:
            print("Pegawai tidak ditemukan!")
            return
        
        performa = int(input("Nilai performa (0-100): "))
        bonus = pegawai.hitung_bonus(performa)
        print(f"\nBonus untuk {pegawai.nama}: Rp {bonus:,}")
        
    except ValueError as e:
        print(f"Error: {e}")

def tampilkan_semua_pegawai():
    if not daftar_pegawai:
        print("\nBelum ada data pegawai!")
        return
    
    print("\n=== Daftar Pegawai ===")
    for idx, pegawai in enumerate(daftar_pegawai, 1):
        print(f"\n{idx}. ID: {pegawai.id_pegawai}")
        print(f"Nama: {pegawai.nama}")
        print(f"Jabatan: {pegawai.jabatan}")

def tampilkan_detail_pegawai():
    if not daftar_pegawai:
        print("\nBelum ada data pegawai!")
        return
    
    tampilkan_semua_pegawai()
    id_pegawai = input("\nMasukkan ID Pegawai untuk detail: ").strip()
    
    pegawai = next((p for p in daftar_pegawai if p.id_pegawai == id_pegawai), None)
    if pegawai:
        print(pegawai)  # Memanggil __str__
    else:
        print("Pegawai tidak ditemukan!")

def main_menu():
    while True:
        print("\n=== Sistem Manajemen Pegawai ===")
        print("1. Tambah Pegawai")
        print("2. Hitung Bonus Pegawai")
        print("3. Tampilkan Semua Pegawai")
        print("4. Tampilkan Detail Pegawai")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            input_pegawai()
        elif pilihan == "2":
            hitung_bonus_pegawai()
        elif pilihan == "3":
            tampilkan_semua_pegawai()
        elif pilihan == "4":
            tampilkan_detail_pegawai()
        elif pilihan == "5":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main_menu()