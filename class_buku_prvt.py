class Buku:
    def __init__(self, judul, pengarang, tahun_terbit,__harga):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.harga__buku = __harga   


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938, 40000)
buku2 = Buku('Psychology Of Money', 'Morgan Housel', 2022, 40000)
buku3 = Buku('Harry Potter', 'Mahabarata', 1997, 40000)


data_buku = [buku1, buku2, buku3]

print('Daftar Buku')
for b in data_buku:
    print(
        f'Buku {b.judul} karangan {b.pengarang} pertama kali diterbitkan tahun {b.tahun_terbit} harga buku {b.harga__buku}')