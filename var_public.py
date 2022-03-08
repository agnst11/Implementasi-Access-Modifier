class Mobil:

    # public variabel
    def __init__(self, jendela, pintu, mesin):
        self.jendela = jendela
        self.pintu = pintu
        self.mesin = mesin
mobil1 = Mobil(2, 2, "ICE")

print(mobil1.jendela)
