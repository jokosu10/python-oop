from geometri.bangunruang import BangunRuang


class Segitiga(BangunRuang):
    # this function call firstly function when object is creation
    def __init__(self, a,t):
        self.a = a
        self.t = t

    def info(self):
        return f'Modul menghitung perhitungan Segitiga dengan alas {self.a} dan lebar {self.t} adalah  '

    def hitungLuas(self):
        return (self.a * self.t) / 2