class Canli:
    tur = 'Canlı'


class Insan(Canli):
    tur = 'İnsan'
    boy = ''
    yas = 0

    def get_boy(self):
        print(self.boy)

    def get_yas(self):
        print(self.yas)


class Anne(Insan):
    isim = 'Güler'
    boy = '1.65'
    yas = 47

    def calisma_alani(self):
        print('Kozmetik')

    def yemek(self):
        print('Anneden gelen özel yemek yapma yeteneği')


class Baba(Insan):
    isim = 'Şahin'
    boy = '1.80'
    yas = 48

    def calisma_alani(self):
        print('Plastik')

    def plan(self):
        print('Babadan gelen özel plan yapma yeteneği')


class Cocuk(Anne, Baba):
    isim = 'Rüzgar'
    boy = '1.80'
    yas = 23

    def calisma_alani(self):
        print('Yazılım')


anne = Baba()
baba = Anne()
cocuk = Cocuk()

cocuk.calisma_alani()
cocuk.yemek()
cocuk.plan()
cocuk.get_boy()
