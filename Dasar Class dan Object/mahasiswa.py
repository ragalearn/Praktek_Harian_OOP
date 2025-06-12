import csv
from datetime import datetime

class Mahasiswa:
    def __init__(self, nim, nama, prodi, tahun_lahir, status='Aktif'):
        if not nim.isdigit():
            raise ValueError("NIM harus berupa angka!")
        if not nama.strip() or not prodi.strip():
            raise ValueError("Nama dan Prodi tidak boleh kosong!")
        if len(str(tahun_lahir)) != 4 or not str(tahun_lahir).isdigit():
            raise ValueError("Tahun lahir harus 4 digit angka (contoh: 2000).")
        
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.tahun_lahir = int(tahun_lahir)
        self.status = status

    def hitung_usia(self):
        return datetime.now().year - self.tahun_lahir

    def cek_status(self):
        return "Aktif" if self.status == 'Aktif' else "Tidak Aktif"

    def tampilkan_info(self):
        print(f"\n[NIM: {self.nim}]")
        print(f"Nama: {self.nama}")
        print(f"Prodi: {self.prodi}")
        print(f"Usia: {self.hitung_usia()} tahun")
        print(f"Status: {self.cek_status()}")

class MahasiswaInternasional(Mahasiswa):
    def __init__(self, nim, nama, prodi, tahun_lahir, negara_asal, status='Aktif'):
        super().__init__(nim, nama, prodi, tahun_lahir, status)
        self.negara_asal = negara_asal

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Negara Asal: {self.negara_asal}")

# Fungsi untuk menyimpan data ke file
def simpan_ke_file(daftar_mahasiswa, format_file='txt'):
    if format_file == 'txt':
        with open('mahasiswa.txt', 'w') as file:
            for mhs in daftar_mahasiswa:
                file.write(f"{mhs.nim},{mhs.nama},{mhs.prodi},{mhs.tahun_lahir},{mhs.status}\n")
    elif format_file == 'csv':
        with open('mahasiswa.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["NIM", "Nama", "Prodi", "Tahun Lahir", "Status"])
            for mhs in daftar_mahasiswa:
                writer.writerow([mhs.nim, mhs.nama, mhs.prodi, mhs.tahun_lahir, mhs.status])

# Fungsi untuk memuat data dari file
def muat_dari_file(format_file='txt'):
    daftar_mahasiswa = []
    try:
        if format_file == 'txt':
            with open('mahasiswa.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 5:
                        mhs = Mahasiswa(data[0], data[1], data[2], data[3], data[4])
                        daftar_mahasiswa.append(mhs)
        elif format_file == 'csv':
            with open('mahasiswa.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Lewati header
                for row in reader:
                    if len(row) == 5:
                        mhs = Mahasiswa(row[0], row[1], row[2], row[3], row[4])
                        daftar_mahasiswa.append(mhs)
    except FileNotFoundError:
        print("File belum ada. Akan dibuat baru saat menyimpan.")
    return daftar_mahasiswa

# Fungsi untuk update data mahasiswa
def update_mahasiswa(daftar_mahasiswa, nim, nama_baru, prodi_baru, tahun_lahir_baru, status_baru):
    for mhs in daftar_mahasiswa:
        if mhs.nim == nim:
            mhs.nama = nama_baru
            mhs.prodi = prodi_baru
            mhs.tahun_lahir = tahun_lahir_baru
            mhs.status = status_baru
            return True
    return False

# Fungsi untuk hapus mahasiswa
def hapus_mahasiswa(daftar_mahasiswa, nim):
    for mhs in daftar_mahasiswa:
        if mhs.nim == nim:
            daftar_mahasiswa.remove(mhs)
            return True
    return False

# Fungsi untuk menampilkan semua mahasiswa
def tampilkan_semua_mahasiswa(daftar_mahasiswa):
    if not daftar_mahasiswa:
        print("\nTidak ada data mahasiswa.")
    else:
        print("\n=== DAFTAR MAHASISWA ===")
        for idx, mhs in enumerate(daftar_mahasiswa, 1):
            print(f"\n{idx}. [NIM: {mhs.nim}]")
            print(f"Nama: {mhs.nama}")
            print(f"Prodi: {mhs.prodi}")
            print(f"Usia: {mhs.hitung_usia()} tahun")
            print(f"Status: {mhs.cek_status()}")
            if isinstance(mhs, MahasiswaInternasional):
                print(f"Negara Asal: {mhs.negara_asal}")

# Program Utama
def main():
    daftar_mahasiswa = muat_dari_file('txt')  # Muat data dari file (jika ada)

    while True:
        print("\n=== MENU ===")
        print("1. Tambah Mahasiswa")
        print("2. Tambah Mahasiswa Internasional")
        print("3. Tampilkan Semua Mahasiswa")
        print("4. Update Data Mahasiswa")
        print("5. Hapus Mahasiswa")
        print("6. Simpan Data ke File")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            try:
                nim = input("NIM: ")
                nama = input("Nama: ")
                prodi = input("Prodi: ")
                tahun_lahir = input("Tahun Lahir (YYYY): ")
                status = input("Status (Aktif/Tidak Aktif): ").capitalize()
                
                mhs = Mahasiswa(nim, nama, prodi, tahun_lahir, status)
                daftar_mahasiswa.append(mhs)
                print(f"\nMahasiswa {nama} berhasil ditambahkan!")
            except ValueError as e:
                print(f"Error: {e}")

        elif pilihan == '2':
            try:
                nim = input("NIM: ")
                nama = input("Nama: ")
                prodi = input("Prodi: ")
                tahun_lahir = input("Tahun Lahir (YYYY): ")
                negara_asal = input("Negara Asal: ")
                status = input("Status (Aktif/Tidak Aktif): ").capitalize()
                
                mhs = MahasiswaInternasional(nim, nama, prodi, tahun_lahir, negara_asal, status)
                daftar_mahasiswa.append(mhs)
                print(f"\nMahasiswa Internasional {nama} berhasil ditambahkan!")
            except ValueError as e:
                print(f"Error: {e}")

        elif pilihan == '3':
            tampilkan_semua_mahasiswa(daftar_mahasiswa)

        elif pilihan == '4':
            nim = input("Masukkan NIM mahasiswa yang akan diupdate: ")
            nama_baru = input("Nama Baru: ")
            prodi_baru = input("Prodi Baru: ")
            tahun_lahir_baru = input("Tahun Lahir Baru (YYYY): ")
            status_baru = input("Status Baru (Aktif/Tidak Aktif): ").capitalize()
            
            if update_mahasiswa(daftar_mahasiswa, nim, nama_baru, prodi_baru, tahun_lahir_baru, status_baru):
                print("\nData berhasil diupdate!")
            else:
                print("\nMahasiswa dengan NIM tersebut tidak ditemukan.")

        elif pilihan == '5':
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            if hapus_mahasiswa(daftar_mahasiswa, nim):
                print("\nMahasiswa berhasil dihapus!")
            else:
                print("\nMahasiswa dengan NIM tersebut tidak ditemukan.")

        elif pilihan == '6':
            simpan_ke_file(daftar_mahasiswa, 'txt')
            simpan_ke_file(daftar_mahasiswa, 'csv')
            print("\nData berhasil disimpan ke mahasiswa.txt dan mahasiswa.csv!")

        elif pilihan == '7':
            simpan_ke_file(daftar_mahasiswa, 'txt')  # Auto-save sebelum keluar
            print("\nData disimpan. Program selesai.")
            break

        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()