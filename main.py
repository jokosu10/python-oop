from geometri.bangunruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print("Use OOP")

p1 = PersegiPanjang(5, 10)
print(p1.info())
print(p1.hitungLuas())

s1 = Segitiga(7, 10)
print(s1.info())
print(s1.hitungLuas())

print('\ncreate class from bangun ruang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitungLuas())

# Polymorphism kemampuan object untuk merespon tipe object berbeda
bangun_ruang = []
bangun_ruang.append(p1)
bangun_ruang.append(s1)

print('\n print menggunakan konsep Polymorphism')
for i in bangun_ruang:
    print(i.info())
