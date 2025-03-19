import math  # Impordin matemaatika teegi

# Kalkulaatori klass, mis sisaldab erinevaid matemaatilisi tehteid
class Cal:
    def __init__(self, a=None, b=None):
        """Konstruktor, mis võtab vastu kaks arvu (või jätab need tühjaks, kui pole vaja)"""
        self.a = a
        self.b = b

    def liitmine(self):
        """Liidab kaks arvu"""
        return self.a + self.b

    def lahutamine(self):
        """Lahutab teise arvu esimesest"""
        return self.a - self.b

    def korrutamine(self):
        """Korrutab kaks arvu"""
        return self.a * self.b

    def jagamine(self):
        """Jagab esimese arvu teisega, kontrollides, et jagamine nulliga poleks võimalik"""
        if self.b == 0:
            return "Viga: Jagamine nulliga pole lubatud!"
        return self.a / self.b

    def jaak(self):
        """Leiab jäägi jagamisel, kui jagamine nulliga poleks võimalik"""
        if self.b == 0:
            return "Viga: Jäägi leidmine nulliga pole lubatud!"
        return self.a % self.b

    def ruutjuur(self, number):
        """Arvutab arvu ruutjuure, kontrollides, et arv poleks negatiivne"""
        if number < 0:
            return "Viga: Negatiivse arvu ruutjuur pole reaalne arv!"
        return math.sqrt(number)

    def astendamine(self):
        """Tõstab esimese arvu teise arvu astmesse"""
        return self.a ** self.b

    def keskmine(self):
        """Leiab kahe arvu aritmeetilise keskmise"""
        return (self.a + self.b) / 2


# Funktsioon, mis kuvab kalkulaatori menüü
def menu():
    print("\nVali tehe:")
    print("1. Liitmine")
    print("2. Lahutamine")
    print("3. Korrutamine")
    print("4. Jagamine")
    print("5. Jäägi leidmine")
    print("6. Ruutjuure leidmine")
    print("7. Astendamine")
    print("8. Keskmise leidmine")
    print("0. Välju")

# Peamine tsükkel, mis hoiab kalkulaatori käigus
while True:
    menu()  # Kuvame menüü
    valik = input("Sisesta valik: ")  # Kasutaja sisestab valiku

    # Kui valik eeldab kahte arvu, siis küsime need kasutajalt
    if valik in ["1", "2", "3", "4", "5", "7", "8"]:
        try:
            a = int(input("Sisesta esimene number: "))
            b = int(input("Sisesta teine number: "))
            kalk = Cal(a, b)  # Loome klassi objekti ja anname sellele sisestatud arvud

            # Kontrollime, milline tehe valiti ja kuvame vastuse
            if valik == "1":
                print("Vastus:", kalk.liitmine())
            elif valik == "2":
                print("Vastus:", kalk.lahutamine())
            elif valik == "3":
                print("Vastus:", kalk.korrutamine())
            elif valik == "4":
                print("Vastus:", kalk.jagamine())
            elif valik == "5":
                print("Vastus:", kalk.jaak())
            elif valik == "7":
                print("Vastus:", kalk.astendamine())
            elif valik == "8":
                print("Vastus:", kalk.keskmine())

        except ValueError:
            print("Viga: Palun sisesta ainult numbreid!")

    # Kui valik on ruutjuur, siis küsime ainult ühe arvu
    elif valik == "6":
        try:
            number = int(input("Sisesta arv, millest ruutjuur võtta: "))
            kalk = Cal()  # Loome klassi objekti ilma arvudeta, sest ruutjuur vajab ainult ühte arvu
            print("Vastus:", kalk.ruutjuur(number))

        except ValueError:
            print("Viga: Palun sisesta kehtiv arv!")

    # Kui kasutaja soovib programmist väljuda
    elif valik == "0":
        print("Programm lõpetatakse.")
        break  # Väljumine tsüklist

    else:
        print("Vigane sisestus, proovi uuesti.")

    input("\nVajuta Enter, et jätkata...")  # Lisame pausi, et vastus ei kaoks menüü taha ära
