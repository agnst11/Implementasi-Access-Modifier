class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk, __alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.alamat__rumah = __alamat


m1 = Mahasiswa('Udin', '10120371', 'Sistem Informasi', 2020, "Wonosari")
m2 = Mahasiswa('Agnesta Linda sari', '5210411167', 'Informatika', 2021, "Ponjong")
m3 = Mahasiswa('Bella Triana', '5210411175', 'Informatika', 2021, "Seleman")
m4 = Mahasiswa('Eusebia Nawang Ari', '5210411195', 'Informatika', 2021, "Yogyakarta")
m5 = Mahasiswa('Veratina Fridayanti', '5210411174', 'Informatika', 2021, "Kulonprogo")




data_mahasiswa = [m1, m2, m3, m4, m5]

print('Daftar Mahasiswa')
for i in data_mahasiswa:
        print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim} alamat rumah {i.alamat__rumah}')