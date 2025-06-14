import datetime
import json
from getpass import getpass  # Untuk input password tanpa echo

class RekeningBank:
    MAX_TARIK_HARIAN = 1000000  # Limit 1 juta/hari
    
    def __init__(self, nama_pemilik, password):
        self.__nama_pemilik = nama_pemilik
        self.__saldo = 0
        self.__password = password
        self.__riwayat = []
        self.__tarikan_hari_ini = 0
    
    # ===== CORE FUNCTIONALITY =====
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, jumlah):
        if not isinstance(jumlah, (int, float)):
            raise ValueError("Input harus angka")
        if jumlah < 0:
            raise ValueError("Saldo tidak boleh negatif")
        self.__saldo = jumlah
        self.catat_transaksi("SETOR" if jumlah > self.__saldo else "PENYESUAIAN", abs(jumlah - self.__saldo))
    
    # ===== PASSWORD PROTECTION =====
    def verifikasi_password(self, password):
        return self.__password == password
    
    # ===== TRANSACTION FEATURES =====
    def setor_tunai(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah setor harus positif")
        self.__saldo += jumlah
        self.catat_transaksi("SETOR", jumlah)
    
    def tarik_tunai(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah tarik harus positif")
        if jumlah > self.__saldo:
            raise ValueError("Saldo tidak mencukupi")
        if jumlah + self.__tarikan_hari_ini > self.MAX_TARIK_HARIAN:
            raise ValueError(f"Melebihi limit harian (Rp {self.MAX_TARIK_HARIAN:,})")
        
        self.__saldo -= jumlah
        self.__tarikan_hari_ini += jumlah
        self.catat_transaksi("TARIK", jumlah)
    
    def transfer(self, rekening_tujuan, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah transfer harus positif")
        if jumlah > self.__saldo:
            raise ValueError("Saldo tidak mencukupi")
        
        self.__saldo -= jumlah
        rekening_tujuan.__saldo += jumlah
        self.catat_transaksi("TRANSFER KELUAR", jumlah)
        rekening_tujuan.catat_transaksi("TRANSFER MASUK", jumlah)
    
    # ===== TRANSACTION HISTORY =====
    def catat_transaksi(self, jenis, jumlah):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__riwayat.append({
            'waktu': timestamp,
            'jenis': jenis,
            'jumlah': jumlah,
            'saldo': self.__saldo
        })
    
    def tampilkan_riwayat(self):
        print("\n=== RIWAYAT TRANSAKSI ===")
        for trx in self.__riwayat[-10:]:  # Tampilkan 10 transaksi terakhir
            print(f"{trx['waktu']} | {trx['jenis']:15} | Rp {trx['jumlah']:>10,} | Saldo: Rp {trx['saldo']:,}")
    
    # ===== FILE OPERATIONS =====
    def simpan_ke_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Data Rekening {self.__nama_pemilik}\n")
            f.write(f"Saldo Terakhir: Rp {self.__saldo:,}\n")
            f.write("\nRiwayat Transaksi:\n")
            for trx in self.__riwayat:
                f.write(f"{trx['waktu']} | {trx['jenis']:15} | Rp {trx['jumlah']:>10,} | Saldo: Rp {trx['saldo']:,}\n")
    
    @classmethod
    def muat_dari_file(cls, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                nama = lines[0].split("Data Rekening ")[1].strip()
                saldo = float(lines[1].split("Rp ")[1].replace(",", ""))
                
                rekening = cls(nama, "temp_password")
                rekening.__saldo = saldo
                
                for line in lines[4:]:  # Skip header
                    if line.strip():
                        parts = line.split("|")
                        rekening.__riwayat.append({
                            'waktu': parts[0].strip(),
                            'jenis': parts[1].strip(),
                            'jumlah': float(parts[2].split("Rp")[1].replace(",", "")),
                            'saldo': float(parts[3].split("Rp")[1].replace(",", ""))
                        })
                return rekening
        except FileNotFoundError:
            return None

def main():
    print("=== APLIKASI BANK ===")
    
    # Coba muat data dari file
    rekening = RekeningBank.muat_dari_file("rekening.txt")
    if rekening:
        password = getpass("Masukkan password: ")
        if not rekening.verifikasi_password(password):
            print("Password salah! Membuat rekening baru...")
            rekening = None
    
    if not rekening:
        nama = input("Nama pemilik rekening: ")
        password = getpass("Buat password: ")
        rekening = RekeningBank(nama, password)
    
    while True:
        print("\nMENU:")
        print("1. Setor Tunai")
        print("2. Tarik Tunai")
        print("3. Transfer")
        print("4. Cek Saldo")
        print("5. Riwayat Transaksi")
        print("6. Simpan & Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        try:
            if pilihan == "1":
                jumlah = float(input("Jumlah setor: Rp "))
                rekening.setor_tunai(jumlah)
                print(f"Setor berhasil! Saldo: Rp {rekening.get_saldo():,}")
            
            elif pilihan == "2":
                jumlah = float(input("Jumlah tarik: Rp "))
                rekening.tarik_tunai(jumlah)
                print(f"Tarik berhasil! Saldo: Rp {rekening.get_saldo():,}")
            
            elif pilihan == "3":
                tujuan_nama = input("Nama penerima: ")
                tujuan = RekeningBank(tujuan_nama, "dummy_password")  # Asumsi rekening tujuan ada
                jumlah = float(input("Jumlah transfer: Rp "))
                rekening.transfer(tujuan, jumlah)
                print(f"Transfer berhasil! Saldo: Rp {rekening.get_saldo():,}")
            
            elif pilihan == "4":
                print(f"\nSaldo Anda: Rp {rekening.get_saldo():,}")
            
            elif pilihan == "5":
                rekening.tampilkan_riwayat()
            
            elif pilihan == "6":
                rekening.simpan_ke_file("rekening.txt")
                print("Data berhasil disimpan. Sampai jumpa!")
                break
            
            else:
                print("Pilihan tidak valid!")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()