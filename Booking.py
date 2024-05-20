class Foglalas():
    def __init__(self, idopont, vendeg, szobaszam) -> None:
        self.idopont = idopont
        self.vendeg = vendeg
        self.szobaszam = szobaszam

    def ShowData(self):
        print(f"Szobaszám: {self.szobaszam}, Időpont: {self.idopont}; Vendég: {self.vendeg.nev}, Jelszó: {self.vendeg.jelszo} ")
        print()

    