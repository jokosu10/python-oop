from geometri.bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):
    # this function call firstly function when object is creation
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return f'Modul menghitung perhitungan persegipanjang dengan panjang {self.p} dan lebar {self.l} adalah  '

    def hitungLuas(self):
        return self.p * self.l
