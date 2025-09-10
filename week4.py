# Oryza Valendio
# NIM F1401241092
# K1/P1

## Latihan if
LuasLahan = float(input('Masukkan luas lahan : '))

if LuasLahan>=10:
    print('Gunakan traktor roda 4')
if LuasLahan<10:
    print("gunakan traktor roda 2")
print('penggunaan alat mesin pertanian akan lebih efektif')
##############################################################

# latihan traktor elif
LuasLahan = float(input('Masukkan luas lahan : '))

if LuasLahan>=100:
    print('Gunakan traktor besar')
elif LuasLahan>=50:
    print("gunakan traktor sedang")
elif LuasLahan>=10:
    print("gunakan traktor kecil")
else :
    print("gunakan traktor roda dua")
##############################################################

# # Soal 1
kmtt = int(input("1. Bibit \n 2. Pertumbuhan \n 3. Pembuahan \n 4. Penuaan \n Masukkan kode masa tumbuh tanaman :"))
ms = True
t = 0
if kmtt == 1 :
    ms,t = 'Bibit', 10
    print("Bibit perlu 10 tetes")
if kmtt == 2 :
    ms, t = 'pertumbuhan', 8
    print("Pertumbuhan perlu 8 tetes")
if kmtt == 3 :
    ms, t = 'pembuahan', 5
    print("Pembuahan perlu 5 tetes")
if kmtt == 4 :
    ms, t = 'penuaan', 3
    print("Penuaan perlu 3 tetes")

print("masa tumbuh : ", ms )
print("Jumlah tetes per detik : ", t , "tetes")
##############################################################

# # PR 1
pdp = int(input('Masukkan komisi : '))
km = 0

if pdp <= 500000:
    km = 0
    print(f"Komisi yang diterima adalah {km}")
    print(f"Pendapatan : {pdp}")
elif pdp > 500000:
    if pdp <= 1000000 and pdp > 500000:
        km = 50000
    elif pdp > 1000000:
        km = 5/100*pdp + 50000
    print(f"Pendapatan : {pdp}")
    print(f"Komisi yang diterima adalah {km}")
##############################################################
        
# # PR 2
umr = int(input('Masukkan umur tanaman : '))
lm = 0
wk = int(input('1. Pagi \n 2. Sore \n Masukkan waktu pemberian air : '))
if umr <= 20:
    if wk == 1: lm = 15
    if wk == 2: lm = 10
    print(f'umur tanaman {umr} dan waktu penanaman {wk}')
    print(f'lama pemberian waktu air {lm}')
elif umr <= 40:
    if wk == 1: lm = 40
    if wk == 2: lm = 20
    print(f'umur tanaman {umr} dan waktu penanaman {wk}')
    print(f'lama pemberian waktu air {lm}')
elif umr <= 60:
    if wk == 1: lm = 20
    if wk == 2: lm = 5
    print(f'umur tanaman {umr} dan waktu penanaman {wk}')
    print(f'lama pemberian waktu air {lm}')
else :
    print('Melebihi batas waktu tanam')