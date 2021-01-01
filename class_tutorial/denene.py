class Employes():
    def __init__(self):
        self.isim = ""
        self.soyisim = ""
        self.adres = ""
        self.age = 0

class muhendis():
    def __init__(self):
        self.programming = ""

class bok():
    def __init__(self, iletisim = "n/a"):
        self.iletisim = iletisim

enes = bok()
enes.iletisim = "good"
print(enes.iletisim)