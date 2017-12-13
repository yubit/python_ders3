class Deneme:

    def __init__(self):
        print('Başlatma')

    def __new__(cls):
        print('Yaratma')
        # return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print('Çağırıldı')

    def __str__(self):
        print('String olarak yazılışı')
        return 'Deneme Classı'


deneme = Deneme()
# d()
# print(d, type(d))

