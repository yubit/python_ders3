"""def cumle_kur(isim, yer, eylem):
    print("{} isimli kişi, {}'nde {}.".format(isim, yer, eylem))



cumle_kur('Burak', 'Yaşar Üniversitesi', 'okuyor')
cumle_kur(kelimeler[0], kelimeler[1], kelimeler[2])
cumle_kur(*kelimeler)"""
kelimeler = ['Burak', 'Yaşar Üniversitesi', 'okuyor']


"""def deneme_fonksiyonu(zorunlu_arguman, *argumanlar, **anahtarli_argumanlar):
    print('Zorunlu:', zorunlu_arguman, type(zorunlu_arguman))
    print('Argümanlar:', argumanlar, type(argumanlar))
    print('Anahtarlı Argümanlar:', anahtarli_argumanlar, type(anahtarli_argumanlar))
    print()


deneme_fonksiyonu(5, 1, 3, 6)
deneme_fonksiyonu(77, kelimeler)
deneme_fonksiyonu('zorunlu', *kelimeler)
deneme_fonksiyonu(3, merhaba='MERHABA')
deneme_fonksiyonu(3, *kelimeler, merhaba='MERHABA', sayi=2)"""


def topla(*sayilar):
    sonuc = 0
    for sayi in sayilar:
        sonuc += sayi

    print('Sonuç:', sonuc)


def arguman_ara(**kwargs):
    isim = kwargs.get('isim', 'YOK')
    print('İsim:', isim)


arguman_ara()
arguman_ara(isim='Rüzgar')