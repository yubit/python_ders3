harfler = ['z', 'x', 'a', 'k', 'e']
sayilar = [10, 5, 3, 0, 15]



#
# print(sorted(harfler, reverse=True))
# print(sorted(sayilar, reverse=True))

#
# kucukler = list(filter(lambda x: x < 5, sayilar))
# print('kucukler', kucukler)

kareleri = list(map(lambda x: x**2, sayilar))
print(kareleri)

tersi = list(reversed(sayilar))
print(tersi)