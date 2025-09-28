# Program Manajemen Data Penerima Bantuan Sosial Kelurahan Sempaja Selatan

# Data Penerima Diisi Dengan 5 Contoh Data
data_penerima = [
    {
        "nama": "Naruto",
        "nik": 1,
        "alamat": "Konoha",
        "jenis bantuan": "Chakra"
    },
    {
        "nama": "Boruto",
        "nik": 2,
        "alamat": "Konoha",
        "jenis bantuan": "Karma"
    },
    {
        "nama": "Saruto",
        "nik": 3,
        "alamat": "Konoha",
        "jenis bantuan": "Chakra"
    },
    {
        "nama": "Ashuto",
        "nik": 4,
        "alamat": "Konoha",
        "jenis bantuan": "Chakra"
    },
    {
        "nama": "Saburo",
        "nik": 5,
        "alamat": "Konoha",
        "jenis bantuan": "Chakra"
    }
]
def login():
    print("--- Selamat Datang di Program Manajemen Bansos ---")
    print("---        Kelurahan Sempaja Selatan           ---")
    print("--------------------------------------------------")
    maksimal_percobaan = 3
    for percobaan in range(maksimal_percobaan):
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        
        if username == "lurah" and password == "admin":
            print("Login berhasil! Selamat datang, Lurah.")
            return "lurah"
        elif username == "warga" and password == "123":
            print("Login berhasil! Selamat datang, Warga.")
            return "warga"
        else:
            print(f"Username atau password salah. Percobaan {percobaan + 1}/{maksimal_percobaan}")
    
    print("Terlalu banyak percobaan gagal (Penyusup ya???).")
    return None

# Menambahkan Data Penerima Bantuan Sosial (Create) 
def tambah_penerima():
    print("--- Tambah Data Penerima ---")
    try:
        nama = input("Masukkan Nama lengkap: ")
        if not nama:
            raise ValueError("Nama tidak boleh kosong!")
        
        nik_input = input("Masukkan NIK (Nomor Induk Kependudukan): ")
        nik = int(nik_input)
        for penerima in data_penerima:
            if penerima["nik"] == nik:
                raise ValueError("NIK sudah terdaftar! Gunakan NIK lain.")
        
        alamat = input("Masukkan Alamat lengkap: ")
        if not alamat:
            raise ValueError("Alamat tidak boleh kosong!")
        
        jenis_bantuan = input("Masukkan Jenis Bantuan (Contoh: Sembako, Uang Tunai, dll): ")
        if not jenis_bantuan:
            raise ValueError("Jenis bantuan tidak boleh kosong!")
        
        penerima_baru = {
            "nama": nama,
            "nik": nik,
            "alamat": alamat,
            "jenis bantuan": jenis_bantuan
        }
        data_penerima.append(penerima_baru)
        print("Data penerima baru telah ditambahkan.")
    except ValueError:
        print(f"Error:Input harus angka")
    except KeyboardInterrupt:
        print(f"\nTerjadi kesalahan:tidak boleh seperti ctrl+c dll")

# Melihat Data Penerima Bantuan Sosial (Read) 
def lihat_penerima():
    print("--- Daftar Penerima Bantuan Sosial ---")
    if not data_penerima:
        print("Belum ada data penerima.")
        return
    
    for x, penerima in enumerate(data_penerima):
        print("=====================")
        print(f"No. {x+1}")
        print(f"Nama: {penerima['nama']}")
        print(f"NIK: {penerima['nik']}")
        print(f"Alamat: {penerima['alamat']}")
        print(f"Jenis Bantuan: {penerima['jenis bantuan']}")
    print("=====================")

# Mengubah Data Penerima Bantuan Sosial (Update) 
def ubah_penerima():
    print("--- Ubah Data Penerima ---")
    try:
        nik_input = input("Masukkan NIK penerima yang ingin diubah: ")
        nik = int(nik_input)
        
        ditemukan = False
        for penerima in data_penerima:
            if penerima["nik"] == nik:
                print(f"Data ditemukan! Nama saat ini: {penerima['nama']}")
                penerima["alamat"] = input("Masukkan Alamat baru: ")
                penerima["jenis bantuan"] = input("Masukkan Jenis Bantuan baru: ")
                print("Data berhasil diperbarui!")
                ditemukan = True
                break
        
        if not ditemukan:
            print("NIK yang Anda masukkan tidak ditemukan!")
    except ValueError:
        print("Error: NIK harus berupa angka!")
    except KeyboardInterrupt:
        print(f"\nTerjadi kesalahan:tidak boleh seperti ctrl+c dll")

# Menghapus Data Penerima Bantuan Sosial (Delete)
def hapus_penerima():
    print("--- Hapus Data Penerima ---")
    try:
        nik_input = input("Masukkan NIK penerima yang ingin dihapus: ")
        nik = int(nik_input)
        ditemukan = False
        for i, penerima in enumerate(data_penerima):
            if penerima["nik"] == nik:
                konfirmasi = input(f"Yakin hapus data {penerima['nama']} (ya/tidak)? ")
                if konfirmasi == "ya":
                    data_yang_dihapus = data_penerima.pop(i)
                    print(f"Nama: {data_yang_dihapus['nama']}")
                    print(f"NIK: {data_yang_dihapus['nik']}")
                    print("Data di atas telah berhasil dihapus!")
                elif konfirmasi == "tidak":
                    print("Pembatalan Hapus Data.")
                else:
                    print("Input tidak valid")
                ditemukan = True
                break
        
        if not ditemukan:
            print("NIK yang Anda masukkan tidak ditemukan!")
    except ValueError:
        print("Error: NIK harus berupa angka!")
    except KeyboardInterrupt:
        print(f"\nTerjadi kesalahan:tidak boleh seperti ctrl+c dll")

# Menu untuk Role Lurah
def menu_lurah():
    while True:
        print("\n--------------------------")
        print("Menu Lurah - Manajemen Bansos")
        print("Kelurahan Sempaja Selatan")
        print("--------------------------")
        print("Silakan pilih opsi di bawah ini:")
        print("1. Tambah Penerima")
        print("2. Lihat Semua Penerima")
        print("3. Ubah Data Penerima")
        print("4. Hapus Penerima")
        print("5. Keluar")
        try:
            pilihan = input("Pilihan Anda (1-5): ")
            if pilihan == "1":
                tambah_penerima()
            elif pilihan == "2":
                lihat_penerima()
            elif pilihan == "3":
                ubah_penerima()
            elif pilihan == "4":
                hapus_penerima()
            elif pilihan == "5":
                print("Sampai Jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka 1-5.")
        except KeyboardInterrupt:
            print(f"\nTerjadi kesalahan:tidak boleh seperti ctrl+c dll")

# Menu untuk Role Warga
def menu_warga():
    while True:
        print("\n--------------------------")
        print("Menu Warga - Manajemen Bansos")
        print("Kelurahan Sempaja Selatan")
        print("--------------------------")
        print("Silakan pilih opsi di bawah ini:")
        print("1. Tambah Penerima")
        print("2. Lihat Semua Penerima")
        print("3. Keluar")
        
        try:
            pilihan = input("Pilihan Anda (1-3): ")
            if pilihan == "1":
                tambah_penerima()
            elif pilihan == "2":
                lihat_penerima()
            elif pilihan == "3":
                print("Sampai Jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka 1-3.")
        except KeyboardInterrupt:
            print(f"\nTerjadi kesalahan:tidak boleh seperti ctrl+c dll")

# Fungsi Utama Program
def main():
    role = login()
    if role == "lurah":
        menu_lurah()
    elif role == "warga":
        menu_warga()

#Jalankan Program
if __name__ == "__main__":
    main()