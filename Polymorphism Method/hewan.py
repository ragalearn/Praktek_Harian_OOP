import json

class Hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def bergerak(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nama}"

class Burung(Hewan):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis
    
    def bergerak(self):
        return f"{self.nama} ({self.jenis}) terbang di udara."
    
    def terbang(self, ketinggian):
        return f"{self.nama} terbang setinggi {ketinggian} meter!"
    
    def __str__(self):
        return f"{super().__str__()} | Jenis: {self.jenis}"

class Ikan(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama)
        self.habitat = habitat
    
    def bergerak(self):
        return f"{self.nama} berenang di {self.habitat}."
    
    def menyelam(self, kedalaman):
        return f"{self.nama} menyelam {kedalaman} meter di {self.habitat}."
    
    def __str__(self):
        return f"{super().__str__()} | Habitat: {self.habitat}"

class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna
    
    def bergerak(self):
        return f"{self.nama} ({self.warna}) berjalan di darat."
    
    def __str__(self):
        return f"{super().__str__()} | Warna: {self.warna}"

# Validasi Input
def input_non_kosong(pesan):
    while True:
        data = input(pesan).strip()
        if data:
            return data
        print("Error: Input tidak boleh kosong!")

def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Error: Harap masukkan angka!")

# Input Data Hewan
def input_data_hewan():
    print("\nPilih jenis hewan:")
    print("1. Burung")
    print("2. Ikan")
    print("3. Kucing")
    
    pilihan = input("Pilihan (1/2/3): ")
    nama = input_non_kosong("Nama hewan: ")
    
    if pilihan == "1":
        jenis = input_non_kosong("Jenis burung: ")
        return Burung(nama, jenis)
    elif pilihan == "2":
        habitat = input_non_kosong("Habitat ikan: ")
        return Ikan(nama, habitat)
    elif pilihan == "3":
        warna = input_non_kosong("Warna kucing: ")
        return Kucing(nama, warna)
    else:
        print("Pilihan tidak valid!")
        return None

# Program Utama
def main():
    daftar_hewan = []
    
    while True:
        print("\n=== MENU ===")
        print("1. Tambah Hewan")
        print("2. Lihat Info Hewan")
        print("3. Aksi Khusus (Terbang/Menyelam)")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            hewan = input_data_hewan()
            if hewan:
                daftar_hewan.append(hewan)
                print(f"Sukses: {hewan} ditambahkan!")
        
        elif pilihan == "2":
            if not daftar_hewan:
                print("Daftar hewan kosong.")
            else:
                print("\nDaftar Hewan:")
                for i, hewan in enumerate(daftar_hewan, 1):
                    print(f"{i}. {hewan}")  # Memanggil __str__
        
        elif pilihan == "3":
            if not daftar_hewan:
                print("Daftar hewan kosong.")
            else:
                print("\nPilih hewan:")
                for i, hewan in enumerate(daftar_hewan, 1):
                    print(f"{i}. {hewan.nama} ({hewan.__class__.__name__})")
                
                nomor = input_angka("Nomor hewan: ") - 1
                if 0 <= nomor < len(daftar_hewan):
                    hewan = daftar_hewan[nomor]
                    if isinstance(hewan, Burung):
                        ketinggian = input_angka("Ketinggian (meter): ")
                        print(hewan.terbang(ketinggian))
                    elif isinstance(hewan, Ikan):
                        kedalaman = input_angka("Kedalaman (meter): ")
                        print(hewan.menyelam(kedalaman))
                    else:
                        print(f"{hewan.nama} tidak memiliki aksi khusus.")
                else:
                    print("Nomor tidak valid!")
        
        elif pilihan == "4":
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()