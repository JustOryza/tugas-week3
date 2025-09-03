#Soal 1
import math
print("===menghitung keliling lingkaran dan jarak tempuh===")
r = int(input("Masukkan jari jari dalam cm: "))
pi = math.pi
k = pi*2*r
k = round(k, 2)
jt = k*2
jt = round(jt, 2)

print("Diameter lingkaran adalah : ", 2*r)
print("Keliling lingkaran adalah : ", k, "cm persegi")
print("jarak tempuh lingkaran adalah ; ", jt, "cm persegi")

# Soal 2
import math
print("===Menghitung bunga bank===")
i = int(input("Masukkan saldo awal anda : "))
t = int(input("Berapa tahun anda ingin mendepositkan uang anda : "))
h = i*math.pow(1.15, t)
h = round(h, 2)
print("Tabungan anda setelah ", t, " tahun adalah ", h)

# Soal 3
import scipy.constants as const

g = const.G
p = const.atm       
m = float(input("Masukkan Massa dalam kg : "))
a = float(input("Masukkan luas penampang piston dalam meter persegi: "))
f = m*g+p*a
f = f/1000
f = round(f, 2) 
print("Gaya penahan piston adalah : ", f, "N")

