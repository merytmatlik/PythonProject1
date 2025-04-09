class Fruit:  #defineerime klassi

    def __init__(self, name, clr):  #sulgudes on selle klassi objekti parameetrid
        """uus objekti loomisel kutsutav meetod, mis määrab parameetritele konkreetse objekti väärtused"""
        self.name = name  #määrab järjekorras esimese argumendi objekti nimeks
        self.colour = clr  #määrab järjekorras teise argumendi objekti värviks
        self.exp_date = "07.20.2021"  #kuna seda pole klassi parameetrite hulgas, siis see väärtus on igal objektil sama

    def details(self):  #saab oma andmed läbi __init__ meetodi
        """meetod, mis väljastab antud objekti andmed"""
        print("my " + self.name + " is " + self.colour)  #prindib nime ja värvi
        print("expires on " + self.exp_date)  #prindib kõlblik kuni kuupäeva


apple = Fruit("apple", "red")  #luuakse uus objekt klassi Fruit ja määratakse nimeks apple ja värviks red
banana = Fruit("banana", "yellow")  #luuakse uus objekt klassi Fruit ja määratakse nimeks banana ja värviks yellow
kiwi = Fruit("kiwi", "green")  #luuakse uus objekt klassi Fruit ja määratakse nimeks kiwi ja värviks green

apple.details()  #kutsub objektile apple meetodi .details