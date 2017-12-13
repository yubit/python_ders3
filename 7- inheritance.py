class Canli:
    tur = 'Canlı'

    def __init__(self, isim):
        self.isim = isim

    def konus(self):
        print('...')

    def turunu_goster(self):
        print(self.tur)


class Kedi(Canli):
    tur = 'Kedi'

    def konus(self):
        print('Miyav')


class Kopek(Canli):
    tur = 'Köpek'

    def konus(self):
        print('Hav')


canli = Canli('U.F.O')
canli.konus()
canli.turunu_goster()

kedi = Kedi(isim='Mırmır')
kedi.konus()
kedi.turunu_goster()

kopek = Kopek(isim='Çomar')
kopek.konus()
kopek.turunu_goster()