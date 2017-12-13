# sonuc = 2 / 0
# print(sonuc)
telefonlar = ['Android', 'IOS']

try:

    sonuc = 2 / 1
    print('Telefon:', telefonlar[1])

except IndexError as error:
    print('Telefon bulunamadı', type(error))

except ZeroDivisionError:
    print('0 ile bölme yapılamaz')

else:
    print('Hiçbir hata gerçekleşmedi.')

finally:
    print('Program çalışmasını bitirdi')

# try:
#     print('Telefon:', telefonlar[2])
#
# except:
#     print('Telefon bulunamadı')
