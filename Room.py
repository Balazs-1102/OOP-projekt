from abc import ABC, abstractclassmethod

class Szoba(ABC):

    def __init__(self, ar, szobaszam, tipus):
        self.ar = ar
        self.szobaszam = szobaszam
        self.tipus = tipus
    @abstractclassmethod

    def ShowData():
        pass