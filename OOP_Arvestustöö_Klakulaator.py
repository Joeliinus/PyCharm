class Kalko:                      #Lõin klassi "Kalko" ja siis hakkan määrama mida see teha saab
    def __init__(self, x, y):     #init-meetod võimaldab meil objekti instantseerida, sulgudes on argumendid, mida klassilt vaja on
        self.x = x                #lisab "Kalko" objekti omaduse või meetodina, mida saab hiljem luua
        self.y = y                #“self” on alati esimene kuna see on klassi objekt, sellest läheb nähtamatult mööda, see viitab ojektile

    def liitmine(self):           #loob uue meetodi "liikumine", lihtalt "self" pannes, on sellel ligipääs kõigile sellele objektile määratud omadustele ja meetoditele
        return self.x + self.y    #liidab x-i ja y-i

    def lahutamine(self):         #uus meetod "lahutamine", ligipääsuga kõigile objektile määratud omadustele ja meetoditele
        return self.x - self.y    #lahutab x-i ja y-i

    def korrutamine(self):        #loob meetodi "korrutamine", ligipääsuga kõigile objektile määratud omadustele ja meetoditele
        return self.x * self.y    #korrutab x-i ja y-i

    def jagamine(self):           #lõpuks loob meetodi "jagamine", ligipääsuga kõigile objektile määratud omadustele ja meetoditele
        return self.x / self.y    #liidab x-i ja y-i


x = int(input("Sisesta arv: "))      #x on arv mille kasutaja sisestab
y = int(input("Ja veel üks arv: "))    #samuti on ka y-iga
tasko = Kalko(x, y)      #loob Kalko objekti tasko

while True:      #while tsükkel vale sisestuse jaoks
    def menuu():      #loob menuu funktsiooni
        m = "\nKALKULAATORI MENÜÜ \n1. Liitmine \n2. Lahutamine \n3. Korrutamine \n4. Jagamine"    #m on võrdne kalkulaatori menüü tekstiga
        print(m)     #väljastab m-ile määratud teksti
    menuu()      #viitab menuu funktsioonile ja kutsub selle välja
    valitu = int(input("\nVali arvutuse tüüp(1-4): "))     #kasutaja sisestab arvu, sisestatud arv on valituga võrdne
    if valitu == 1:      #kui valitu on võrdeline arvuga 1
        print("\nLiitmise tulemus: ", tasko.liitmine())     #siis liidetakse omavehel x ning y ja nende summa väljastatakse
        break      #sellisel asjade käigul tsükkel lõpetatakse
    if valitu == 2:     #kui valitu on võrdeline arvuga 2
        print("\nLahutamise tulemus: ", tasko.lahutamine())     #siis lahutatakse omavehel x ning y ja nende summa väljastatakse
        break     #sellisel asjade käigul tsükkel lõpetatakse
    if valitu == 3:     #kui valitu on võrdeline arvuga 3
        print("\nKorrutamise tulemus: ", tasko.korrutamine())     #siis korrutatakse omavehel x ning y ja nende summa väljastatakse
        break     #sellisel asjade käigul tsükkel lõpetatakse
    if valitu == 4:     #kui valitu on võrdeline arvuga 4
        print("\nJagamise tulemus: ", tasko.jagamine())     #siis jagatakse omavehel x ning y ja nende summa väljastatakse
        break     #sellisel asjade käigul tsükkel lõpetatakse
    if valitu > 4 or valitu < 1:     #kui valitu on suurem kui 4, või valitu on väiksem kui 1
        print("\nSiestatud number ei olnud valikute seas \nVali uuesti")     #siis teatatakse kasutajale valest siestusest ning läheb tsükli algusesse
