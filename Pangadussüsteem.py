class Kasutaja:
    # Kasutajakontode loomise vanem klass
    def __init__(self, nimi, sugu, vanus):
        self.nimi = nimi
        self.sugu = sugu
        self.vanus = vanus

    def andmed(self):
        print("Kasutaja andmed:")
        print("Nimi:", self.nimi)
        print("Sugu:", self.sugu)
        print("Vanus:", self.vanus)

class Pangakasutaja(Kasutaja):
    # Pangandus kasutajakonto loomise klass
    def __init__(self, nimi, vanus, sugu):
        super().__init__(nimi, vanus, sugu)
        self.jaak = 0

    def sissemakse(self, summa):
        self.jaak += summa
        print("Raha sisestatud. Uus konto jääk:", self.jaak, "€")

    def valjavot(self, summa):
        self.summa = summa
        if(self.summa > self.jaak):
            print("Pole piisavalt vaba raha! Väljavõetav raha:", self.jaak, "€")
        else:
            self.jaak -= self.summa
            print("Raha väljastatud. Uus konto jääk:", self.jaak, "€")

    def jaagivaade(self):
        print("Konto jääk on hetkel:", self.jaak, "€")

# Kasutajainfo sisestamine
nimi = input("Sisestage konto kasutajanimi: ")
sugu = input("Sisestage oma sugu: ")
vanus = input("Sisestage oma vanus: ")

Konto = Pangakasutaja(nimi, vanus, sugu)

while True:
    print("\nValitud tegevused: \n1. Sissemakse \n2. Väljavõtt \n3. Konto jääk \n4. Andmete ülevaade \n5. Välja logimine")
    TegevusValik = int(input("Sisesta valiku number, mida soovite teostada: "))

    if TegevusValik == 1:
        Summa = int(input("Sisestage soovitud sissemakse summa: "))
        Konto.sissemakse(Summa)

    elif TegevusValik == 2:
        Summa = int(input("Sisestage soovitud väljavõtte summa: "))
        Konto.valjavot(Summa)

    elif TegevusValik == 3:
        Konto.jaagivaade()

    elif TegevusValik == 4:
        Konto.andmed()

    elif TegevusValik == 5:
        print("Logite kontolt välja. Head päeva!")
        break

    else:
        print("Vale valik, proovige uuesti.")
