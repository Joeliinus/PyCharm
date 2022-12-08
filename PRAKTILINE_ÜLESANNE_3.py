#Videos näidatud: kuidas luua tavalist pangandussüsteemi või nagu väikest internetipanga süsteemi, kasutades objektorienteeritud programmeerimise abil

#Sellel pangasüsteemil saavad olema mõned funktsioonid.
#vanemaklassid ja lasteklassid
#Vanemaklass on põhiliselt see klass, millel on põhiteave.
#Ja seejärel pärib lapsklass kogu selle teabe vanemklassilt.
#Ilmselgelt on meie pangarakendusel kasutajad.
#"Kasutajatest" saab vanemklass, sest me pärime üksikasjad oma kasutajaklassist.
#Kasutajaklass peab sisaldama andmeid kasutaja kohta ja sellel peab olema funktsioon, mis näitab kõiki üksikasju, mille oleme selle kasutaja kohta salvestanud.
#Pangarakendus või pangaklass aga aitab meil salvestada andmeid kontojäägi kohta, selle kohta, milline on kontojääk.
#Pidage meeles, et iga kasutaja saldo algab nullist.
#See salvestab andmed sissemakse, äravõtmise või väljavõtmise summa kohta.
#See võimaldab ka rollide sissemakseid ja teist funktsiooni, mida nimetatakse tasakaalu vaatamiseks, et vaadata tasakaaluefekti.



#OOP-i kasutav pangandussüsteem
#Vanemaklass: "User"
#Hoiab kasutaja üksikasju
#Sellel on funktsioon kasutaja andmete kuvamiseks
#Lapseklass: "Bank"
#Salvestab üksikasju konto saldo kohta
#Salvestab üksikasjad summa kohta
#Võimaldab sissemakseid teha, välja võtta, vaadata saldot

#Vanemaklass
#Kõigepealt loome vanemklassi "User"
#Seejärel lisame midagi, mida nimetatakse algatajaks. Sulgudes on meil argumendid, mida oma kasutajalt vajame.
#Ärge unustage alustada "self" muutujaga.
#Kui lisame "self" muutuja, tuvastab see selle viitena objektile endale. Nii et kõik, mis on määratud "self-ile", on suures osas määratud ka objektidele.
#Loome oma objektile uued omadused, 3 tükki: nimi, vanus, sugu.
#Iga kord, kui kasutame punk mis iganes "self-i" järel, lisatakse see enam-vähem omaduse või meetodina "User" objektile, mida saab hiljem luua. Praegu on see lihtsalt klass, mistõttu kasutame "self-i".
class User():
    def __innit__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
#hoiab kasutaja üksikasju osa on nüüd tehtud, järgmiseks on funktsioon kasutaja andmete kuvamiseks
#loob veel ühe funktsiooni def, mis on siinkohal meetod, sest see on klassi sisesne, mis teisendatakse objektiks
#kui sulu sisse panna "self", siis sellel on ligipääs kõigile sellele objektile määratud omadustele ja meetoditele
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)
#andmete kuvamine on valmis ja sellega on "User" klassiga kõik

#Lapseklass
#Pärime vanemaklassi meie lasteklassi, mis saab olema "Bank"
#siin samuti loob uue klassi ning kuna tahame pärida kõik omadused ja meetodid "User" klassilt, peane "User" klassi mainima sulgudes
#siis jällegi algataja
#kuna kasutame "User" omadusi, peab neid ka siin sulgudes kahjuks mainima(nimi, vanus, sugu) ja siis võib veel lisada mida iganes vaja on lisaks, aga hetkel pole
#on olemas asi nagu superfunktsioon, mida superfunktsioon teeb, on see, et me ei pea kirjutama "self" punkt mis iganes ridu, see teeb seda meie eest
#ehk selle asemel teeb siis seda superfunktsiooni asja
#põhjus miks on siis tegemist on lapseklassig, on see et see pärib kõik vanemaklassist lapseklassi, see on põhiliselt see mis pärilus endast kujutab
class Bank(User):
    def __init__(self, name, age, gender):
        super().__innit__(name, age, gender)
#nüüd on vaja panna salvestama üksikasju konto saldo kohta, see on veel üks asi, mille peame "self-ile" määrama
#nagu sai öldud, see algab nullist, ja sellega on nüüd korras, uuendab tulevikus
        self.balance = 0
#summa detailide asjad teeb hiljem, nii et jägmiseks hoolitseb, et Võimaldaks sissemakseid teha, välja võtta, vaadata saldot
#esmalt sissemaksed, sulgudesse paneb "amount", kuna on vaja teada palju kasutaja sisse paneb
#kasutaja paneb siis sinna summa palju ta tahb sisse panna
#summa sisestades, see uuendab ja kui uuesti panna, see ei ole läinud nulli ja lisab juurde, läheb nulli kui sellest väljuda
    def deposit(self, amount):   #ära ei tohi unustada "self-i
        self.balance = self.balance + amount   #võtab kontojäägi ja uuendab seda sisestatud summaga
        print("Account balance has been undated: £", self.balance)
    """
    selle asemel võib teha ka:
    
    def deposit(amount):
        self.amount = amount
        self.balance = self.balance + self.ammount
        
    aga see on lihtsalt pikem viis selle tegemiseks
    """
#välja võtmisega natuke keerukam
#tuleb panna self, jällegi vaja teada välja võetava raha kogust
#siinkohal tuleb teha valideerimise kontroll, et kontrollida kas kontol on välja võtmiseks piisavalt raha
#kui pole, siis ütleb seda ning väljastab kontojäägi
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: £", self.balance)
        else:
            self.balance = self.balance - self.amount   #alandab saldot välja võetud summaga
            print("Account Balance has been updated: £", self.balance)   #uuendab saldot
#nüüd tuleb siis kontojäägi vaatamise osa
#siin ei ole summa vajalik, sest me lihtsalt vaatame saldot
#lisaks rahasumma vaatamisele, näitab ka kasutaja isiklikke detaile, mis päritakse kasutaja klassilt
    def view_balance(self):
        self.show_details()
        print("Account Balance: £", self.balance)
#ja sellega ongi kõik