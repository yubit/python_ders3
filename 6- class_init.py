"""class Insan:
    isim = 'Yok'
    yas = 0

    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def ismini_soyle(self):
        print('İsmim:', self.isim)


insan = Insan('Ali', yas=3)
print(insan.isim)
insan.ismini_soyle()"""


class Sayi:
    def __init__(self, deger):
        self.deger = deger

    def __add__(self, other):
        return self.deger - other


sayi1 = Sayi(3)
sayi2 = Sayi(5)
sayi3 = 4

# print(sayi1 + sayi2)
print(sayi1 + sayi3)