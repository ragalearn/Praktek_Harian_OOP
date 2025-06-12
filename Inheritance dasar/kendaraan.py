class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def tampilkan_info(self):
        print(f"Merek: {self.merek}")
        print(f"Tahun: {self.tahun}")


class Mobil(Kendaraan):
    def __init__(self, merek, tahun, jenis_bbm):
        super().__init__(merek, tahun)
        self.jenis_bbm = jenis_bbm
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenis BBM: {self.jenis_bbm}")


class Motor(Kendaraan):
    def __init__(self, merek, tahun, cc):
        super().__init__(merek, tahun)
        self.cc = cc
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"CC: {self.cc}")


class Truk(Kendaraan):
    def __init__(self, merek, tahun, kapasitas_muatan):
        super().__init__(merek, tahun)
        self.kapasitas_muatan = kapasitas_muatan
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kapasitas Muatan: {self.kapasitas_muatan} ton")


class Pesawat(Kendaraan):
    def __init__(self, merek, tahun, maskapai):
        super().__init__(merek, tahun)
        self.maskapai = maskapai
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Maskapai: {self.maskapai}")


# Fungsi validasi input angka
def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Error: Harap masukkan angka!")


# Fungsi input data kendaraan
def input_data_kendaraan():
    print("\nPilih jenis kendaraan:")
    print("1. Mobil")
    print("2. Motor")
    print("3. Truk")
    print("4. Pesawat")
    
    pilihan = input("Pilihan (1-4): ")
    
    merek = input("Merek: ")
    tahun = input_angka("Tahun: ")
    
    if pilihan == "1":
        jenis_bbm = input("Jenis BBM: ")
        return Mobil(merek, tahun, jenis_bbm)
    elif pilihan == "2":
        cc = input_angka("CC: ")
        return Motor(merek, tahun, cc)
    elif pilihan == "3":
        kapasitas = input_angka("Kapasitas Muatan (ton): ")
        return Truk(merek, tahun, kapasitas)
    elif pilihan == "4":
        maskapai = input("Maskapai: ")
        return Pesawat(merek, tahun, maskapai)
    else:
        print("Pilihan tidak valid!")
        return None


# Program utama
def main():
    daftar_kendaraan = []
    
    while True:
        print("\nMenu:")
        print("1. Tambah Kendaraan")
        print("2. Lihat Daftar Kendaraan")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            kendaraan = input_data_kendaraan()
            if kendaraan:
                daftar_kendaraan.append(kendaraan)
                print("Data berhasil ditambahkan!")
        elif pilihan == "2":
            if not daftar_kendaraan:
                print("Daftar kendaraan kosong.")
            else:
                print("\nDaftar Kendaraan:")
                for i, kendaraan in enumerate(daftar_kendaraan, 1):
                    print(f"\nKendaraan {i}:")
                    kendaraan.tampilkan_info()
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()