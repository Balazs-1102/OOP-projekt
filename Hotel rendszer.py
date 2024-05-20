import datetime

from Booking import Foglalas
from RoomInstances import EgyagyasSzoba, KetagyasSzoba
from User import Felhasznalo




class Hotel():

    
    def __init__(self, HNev, HSzobak, HFoglalasok) -> None: #init rész
        self.HNeve = HNev
        self.HSzobak = HSzobak
        self.HFoglalasok = HFoglalasok
        self.IDCounter = 1  #szobafoglalásnál megadja az ID-t
        self.FirstBookingCheck = False #első szobafoglalás elött elrejti a foglalás lemondás opciót

    def SzobaFoglalas(self,CurrentUser):
        print()
        self.FirstBookingCheck = True
        while True:
            print()
            try:
                ValidRoom = False
                
                #Szobaválasztó és ellenörző
                self.SzobaListazas()
                SelecetedRoom = int(input("Válasszon szobaszámot: ")) 
                for Number in self.HSzobak:
                    if SelecetedRoom == Number.szobaszam:
                        ValidRoom = True
                        break
                
                if ValidRoom == False:
                            raise ValueError ("Nincs ilyen szoba!")
                
                #Dátum beadás és ellenőrzés
                SelectedDate = input("Adja meg a kívánt dátumont ÉÉÉÉ.HH.NN formátumban: ") 
                
                #Dátum formába konvertálás
                Temp = SelectedDate.split(".")
                DateFormatted = datetime.datetime(int(Temp[0]),int(Temp[1]),int(Temp[2])) 
                
                #Múltbéli dátum ellenőrzés
                if DateFormatted < datetime.datetime.now(): 
                    raise ValueError("A dátum nem lehet múltbeli!")
                
                #Szabad időpont megállapítása
                for Bookings in self.HFoglalasok:
                    if DateFormatted == self.HFoglalasok[Bookings].idopont and SelecetedRoom == self.HFoglalasok[Bookings].szobaszam:
                        raise ValueError ("Ez az időpont már foglalt!")
                
                #Adatok felvétele a HFoglalások-ba és kilépés
                UserBooking = Foglalas(SelectedDate,CurrentUser,SelecetedRoom)
                self.HFoglalasok[str(self.IDCounter)] = UserBooking
                self.IDCounter += 1
                print("Foglalás sikeresen rögzítve!")
                break
            
            except Exception as err:
                print(err)
            
    def SzobaListazas(self):
        for Szobak in self.HSzobak:
            Szobak.ShowData()
    
    def FoglalasListazas(self):
        for Foglalasok in self.HFoglalasok:
            self.HFoglalasok[Foglalasok].ShowData()

    def SzobaLemondas(self,CurrentUser):
        while True:
            try:
                #Szobafoglalások id és felhasználó alapján való listázása
                for Bookings in self.HFoglalasok:
                    if self.HFoglalasok[Bookings].vendeg == CurrentUser:
                        print("Id:", Bookings)
                        self.HFoglalasok[Bookings].ShowData()
                        print()
                
                #Foglalás eltávolítása a listából (valamiért kétszer kéri be az ID-t és nem tudom miért)
                RemoveRoom = input("Adja meg a törölni kívánt szoba ID-jét: ")
                                
                for RBooking in self.HFoglalasok:
                    if RemoveRoom == RBooking:
                        del self.HFoglalasok[RemoveRoom]
                print("A szoba sikeresen törlődött!")
                break
            
            except Exception as err:
                print(err)
    
    def OptionMenu(self,CurrentUser):
        while True:
            try:
                #User interface

                print()
                print("Válasszon az alábbi opciók közül!")
                print()
                print("- 1: Szobák listázása!")
                print("- 2: Szobafoglalás!")
                if self.FirstBookingCheck:
                    print("- 3: Foglalás lemondása!")
                print("- x: Kilépés!")
                print()
                UserChoice = input()
                
                if UserChoice == "1": #Listázás
                    self.SzobaListazas()
                elif UserChoice == "2": #Foglalás
                    self.SzobaFoglalas(CurrentUser)
                elif UserChoice == "3" and Alvari.FirstBookingCheck: #Lemondás
                    self.SzobaLemondas(CurrentUser)
                elif UserChoice == "x": #Kilépés
                    print("Viszontlátásra!")
                    break
                else:
                    raise ValueError("Helytelen opció!")


            except Exception as err:
                print(err)



#Rendszer adatokkal feltőltése

Room1 = EgyagyasSzoba(12000, 100, "Egyágyas")
Room2 = EgyagyasSzoba(15000, 101, "Egyágyas")
Room3 = KetagyasSzoba(20000, 102, "Kétágyas")

Vendeg1 = Felhasznalo("Kis Béla", "1234")
Vendeg2 = Felhasznalo("Nagy Tamás", "ABCD")
Vendeg3 = Felhasznalo("Közepes Kelemen", "A2C4")

Booking1 = Foglalas(datetime.datetime(2024,6,19), Vendeg1, 100)
Booking2 = Foglalas(datetime.datetime(2024,6,20), Vendeg1, 100)
Booking3 = Foglalas(datetime.datetime(2024,6,21), Vendeg1, 100)
Booking4 = Foglalas(datetime.datetime(2024,6,25), Vendeg2, 101)
Booking5 = Foglalas(datetime.datetime(2024,6,18), Vendeg3, 102)


Alvari = Hotel("Alvári", [Room1,Room2,Room3], {"990": Booking1, "991": Booking2,"992": Booking3, "993": Booking4, "994" : Booking5})

#Főrész

print("///////////////////////////////////////")
print("           Alvári Hotel")
print("//////////////////////////////////////")
print()

print("Bejelentkezés: ")
print()
UserName = input("Név:")
UserPassword = input("Jelszó:")

CurrentUser = Felhasznalo(UserName,UserPassword)

Alvari.OptionMenu(CurrentUser)
