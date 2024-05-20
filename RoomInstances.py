from Room import Szoba

class EgyagyasSzoba(Szoba):
      
    def __init__(self, ar, szobaszam, tipus):
        super().__init__(ar,szobaszam,tipus)

    def ShowData(self):
        print(f"{self.tipus}, Szobaszám: {self.szobaszam}, Ár: {self.ar}")



class KetagyasSzoba(Szoba):
      
    def __init__(self, ar, szobaszam, tipus):
        super().__init__(ar,szobaszam, tipus)

    def ShowData(self):
        print(f"{self.tipus}, Szobaszám: {self.szobaszam}, Ár: {self.ar}")