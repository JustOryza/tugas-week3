# Oryza Valendio 

# # user defined function
# def halo_dunia():
#     print('Hallo dunia!')
# halo_dunia()

# # Parameter wajib
# def perkenalan (nama, asal):
#     print(f'Perkenalkan saya {nama} berasal dari {asal}')
# perkenalan('Abdul','Ngawi')

# # Parameter opsional
# def suhu_udara (daerah, derajat, satuan = 'celcius'):
#     print(f'suhu di daerah {daerah} adalah {derajat} {satuan}')

# suhu_udara('Surabaya', 30)
# suhu_udara('Surabaya', 89, 'fahrenheit')

# def suhu_udara (daerah, derajat = 30, satuan = 'celcius'):
#     print(f'suhu di daerah {daerah} adalah {derajat} {satuan}')
# suhu_udara('jakarta', 'fahrenheit')
# suhu_udara('jakarta', satuan='fahrenheit')
# suhu_udara(satuan='kelvin', daerah='makasar', derajat=100)

# Fungsi yang mengembalikan nilai
# def luas_persegi(sisi):
#     return sisi*sisi

# luas_persegi(100)
# print(f'luas persegi dengan sisi 4 adalah {luas_persegi(4)}')
# persegi_besar = luas_persegi(100)
# persegi_kecil = luas_persegi(50)

# print(f'total luas persegi besar dan kecil adalah {persegi_besar + persegi_kecil} ')

# def persentase (total, jumlah):
#     if (total >= 0 and total <= jumlah):
#         return total / jumlah * 100
#     return False
# print(persentase(30, 60))
# print(persentase(100, 60))

# kota = 'bogor'
# def halo():
#     print(kota)

# print(f'[print secara langsung] {kota}')
# print('Panggil fungsi halo ', end='')
# halo()

# kota, provinsi = 'Bogor', 'Jawa barat'
# def hello():
#     provinsi = 'Jawa Timur'
#     print(kota, provinsi)
# print('Panggil fungsi hello()')
# hello()
# print('\n [Secara Langsung]')
# print(kota, provinsi)

# def tampilAngka (batas, i=1):
#     print(f'Perulangan ke {i}')

#     if (i < batas):
#         tampilAngka(batas, i+1)

# tampilAngka(5)

# def tampilAngka (batas, i=1):
#     if (i < batas):
#         tampilAngka(batas, i+1)
#     print(f'Perulangan ke {i}')
# tampilAngka(5)

# 1
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
angka = int(input("Masukkan angka: "))
hasil = faktorial(angka)
print(f"{angka}! = {hasil}")

# 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Masukkan jumlah bilangan Fibonacci: "))
print(f"Deret Fibonacci sebanyak {n} bilangan:")
for i in range(n):
    print(fibonacci(i), end=" ")

