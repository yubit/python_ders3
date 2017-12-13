class Sinif:
    def merhaba(self):
        print('Merhaba')


def hello():
    print('Hello')


objeler = []
for x in range(10):
    obje = Sinif()
    objeler.append(obje)


for obje in objeler:
    obje.merhaba()


for obje in objeler:
    obje.merhaba = hello


for obje in objeler:
    obje.merhaba()
