"""
Objektorienteeritud programmeerimine on programmeerimise põhimõtete kogum. See käsitleb pigem objekte kui üksikuid andmeid ja üksikuid protseduure. See paneb andmed kokku funktsionaalsusega, et luua objekte, mis omavahel suhtlevad.

1) KLASSID - šabloon objektide loomiseks; programmeerija poolt kirjutatud kood programmi atribuutide ja operatsioonide määratlemiseks.

2) OBJEKTID - üksus/olem; asi päris maailmast (nt arvuti, raamat, kast);  kontseptsioon (nt kohtumine, intervjuu); protsess (nt paberivirna sorteerimine või kahe arvuti võrdlemine nende jõudluse mõõtmiseks).
Objektid koosnevad atribuutidest ja meetoditest.

3) PÄRILUS - klass saab oma meetodid ja omadused tuletada teisest klassist; määratleb mingit tüüpi suhte.

4) KAPSELDAMINE - mehhanism, mille abil ühendame andmed ja andmeid töötlevad funktsioonid üheks üksuseks; andmed ja neid andmeid töötlevad programmid on omavahel seotud ja nende keerukus on peidetud programmide ning programmeerijate eest.

5) POLÜMORFISM - klass saab rakendada päritud meetodit omal moel; palju vorme. Sama ülemklassi erinevad alamklassid, millel on seetõttu sama liides, saavad neid liideseid omal moel rakendada. Polümorfismi rakendatakse siis, kui klassid alistavad päritavate meetodite koodi.

"""
#Video 1

#Objekt - asi päris maailmast (nt auto, paat v raamat), ei pruugi olla füüsiline (nt hambaarsti aeg, kino istekoha reservatsioon v pangakonto)
#Objekt OOP-s: 1)midagi, mis pakub teie loodavale tarkvararakendusele huvi; 2)midagi, mille kohta soovite andmeid luua ja töödelda
#Objekti teine nimi on üksus/olem(entity).

#Klassi vaja, et luua objekte programmiliselt.
#Klass(class) - 1)šabloon objektide loomiseks; 2)programmeerija poolt kirjutatud kood programmi atribuutide ja operatsioonide määratlemiseks
#Atribuudid kirjeldavad objekti, vahel nimetatud väljateks, sest sisaldavad andmeid. Programmeerijate seas tuntud omadustena(properties).
#Omadused kodeeritakse klassi sees: 1)avalike muutujatena; 2)atribuutprotseduuridena.
#Operatsioonid - toimingud, mida saab objektile teha või mida saab sooritada objekt. Vahel nimetatud käitumiseks, kuid rohkem teatud meetoditena.
#Meetodid - programmid klassi seas, kodeeritud kas protseduuride või funktsioonidena.
#Klasse võrreldakse piparkoogivormidega, sest nendega saab palju sama tüüpi objekte luua.
#Klassi nimetatakse vahel tüübiks. Iga objekt on juhtum, kus klass on arvuti mälus. Objekti loomine on seetõttu teatud instantseerimisena.
#Pärast nende objektide loomist, nende omadustele saab anda väärtuse, tehes iga samat tüüpi objekti ainulaadseks üksuseks.
#Iga klassis olev omadus on defineeritud omadusprotseduuriga, mis võib sisaldada, selle määramise ajal omaduse väärtust kehtivaks tegevat koodi.
#See aitab kinnitada, et objekti sisesed andmed oleksid terviklikud.
#Objektile määratud omadusväärtused - tuntud objekti staatusena.
#Samuti saab omadustele väärtuseid anda, samal ajal kui neid esindatakse eksemplarina või eksemplari poolt.
#Selleks kasutatakse erilist meetodit, uus(new), tuntakse konstruktorina.

#Kapseldamine(encapsulation) - objekti sisemise töö keerukuse varjamine programmide ja programmeerijate eest, kes seda kasutavad; teabe peitmine(sest objekti sisesed andmed ja neid andmeid töötlevad funktsioonid, on omavahel seotud, ning välise sekkumise eest kaitstud)
#Mõned suured tarkvaraarendusprojektid - kogenumad programmeerijad kirjutavad klassid, mida hakkavad kasutama nooremad programmeerijad.
#Klass saadaval klassiraamatu vormis. Mõned tarkvaraarendusettevõtted spetsialiseeruvad teistele tarkvaraarendajatele klasside loomises.
#Koostatud klassiraamatukogud kaitsevad oma intellektuaalset omandit.
#Klassi sisemist toimimist pole vaja mõista: et kirjutada koodi mis loob klassist objekti, siis määrab selle omadused ja meetodid. Vaja teada vaid klassi nime, saada olevaid omadusi ja meetodeid ning lisamist vajavaid andmeid nende määratlemisel. Ehk programmeerijal on vaja teada vaid klassi liidest.
#Nende omaduste ja meetodite rakendamine võib jääda saladuseks, lihtsustab oluliselt objektide kasutamist ning aitab tagada, et andmed ja nendesse kapslitud toimingud on ohutud.

#Pärand(inheritance) - klass saab oma meetodid ja omadused tuletada teisest klassist.
#Tulemuseks võib olla klasside hierarhia.
#Nt kui võõta inimese klass, mis määrab inimese objekti meetodid ja omadused.
#Mingi firma töötaja on samuti inimene, nii et läbi pärandi tuletab töötaja klass meetodid ja omadused inimese klassist.
#Firma klient on samuti inimene, nii et läbi pärandi tuletab kliendi klass samuti oma meetodid ja omadused inimese klassist.
#Töötaja klass võib omada mõningaid lisa omadusi ja meetodeid, see võib laiendada inimeste klassi.
#Samuti on ka kliendiga, aga see ei pea sellega piirduma. Nt programmeerija, firmajuht ja koristaja on mingit tüüpi töötajad.
#Pärand määratleb mingit tüüpi suhte.
#Hierarhia ees alguses olev klass on baasklass. Iga klass mis tuleneb teisest klassist on alamklass. Iga klass millel on alamklass, on superklass.

#Polümorfism - klass saab rakendada päritud meetodit omal moel; sõna otseses mõttes: palju vorme
#Inimese hierarhia tipus oleval inimese klassil on meetod, mis salvestab detaile inimese klassist loodud objektide kohta, nt andmebaasi.
#Tänu pärandile teevad hierarhias olevad klassid samu asju.
#Võib olla vajalik, et külastaja detaile salvestatakse erinevalt, nt erinevasse andmebaasi. Seda polümorfism võimaldabki.
#Kliendiklass võib oma uuelt versioonilt saadud päringuga ümber lükata mis tahes meetodi või omaduse töökäigu.
#Sama liidesega sama tüüpi objektide erinevad vormid võivad käituda erineval viisil.



#Video 2

#sisestud “hello” on string klassi objekt
x = 1
print(type("hello"))
#kui asendada “hello” x-iga, siis annab numbri klassi, x on võrdne objektiga, mis on tüübinumber väärtusega 1
x = 1
print(type(x))
#enamjaolt iga asi millega me pythonis töötleme on mingi klassi objekt
def hello():
    print("hello")
X = 1
print(type(hello))
#pythonisse on sisse ehitatud tüübid, neid saab ise ka luua

#iga kord kui lood midagi pythonis, lood objekt ja see on konkreetse klassi näide, ning see klass teeb kindlaks viisi millel see objekt saab suhelda teiste asjadega meie programmis.

#Programm ei tea kuidas selliste erinevat tüüpi objektide vahel suhelda.
x = 1
y = "hello"
print(x + y)

#meetod mis käitub kindlal objektil = on punktioperaator, mingi nimi ja lõpus 2 sulgu mille sees võib olla mingid argumendid
#sellel juhul on meetod upper, mis käitub string tüüpi objektil, mis on salvestatud sellesse stringimuutujasse
string = "hello"
x = 1
print(x.upper())

#lood klassi nt "dog" ja siis hakkad määrama mida see teha saab, prgu loonud meetodi
#selles näites kõik meie meetodid hakkavad parameetritega “self”
#koeraklassi uue isendi loomine, d on koeratüübi objekt
#meetod on funktsioon mis läheb klassi sisse
#alakriipsud näitavad mis moodulis see klass on defineeritud, vaikimisi on moodul pea(main)moodul
#defineerime "def" juures näitab, mis operatsioone saab "dog" klassiga täita, nt "bark(haugu)"
class Dog:
    def bark(self):
        print("bark")
d = Dog()
d.bark()
print(type(d))

#klassi toiming: 1)nimetad klassi(tavaliselt suure algustähega), 2)klassi sees saab defineerida meetodid ja operatsioonid, mida selle objekti saab saab läbi viia.

#saame luua meetodeid, millega on seotud erinevad argumendid või parameetrid, nagu ma panin siia x, ja see tähendab lihtsalt seda, et kui ma seda meetodit kutsun, pean sisestama konkreetse väärtuse või väärtused, mis võivad toimida ja töötada
class Dog:
    def add_one(self, x):
        return x + 1
    def bark(self):
        print("bark")
d = Dog()
d.bark()
print(d.add_one(5))
print(type(d))

#see init-meetod võimaldab meil objekti instantseerida kohe selle loomisel
def __init__(self):
    pass

#seda meetodit kutsutakse alati, kui me “muutuja = Dog()” kirjutame, nii et kui loome uue koera eksemplari, kirjutades koera ja kaks sulgu, seda init-meetodit kutsutakse välja ja see edastab kõik argumendid, mida me siin ei kasuta

#“self” on alati esimene kuna see on klassi objekt, sellest me tahame nähtamatult mööda minna, et teada millisele koerale me ligi pääseme, kui me ütleme koera nime

#“self” asemel saab olla mis iganes ning saab panna mitu erinevat koera, age leiab vanuse
class Dog:
    def __init__(koer, name, age):
        koer.name = name
        koer.age = age
d = Dog("Tim", 3)
print(d.name)
print(d.age)
d2 = Dog("Bob", 12)
print((d2.name))
print(d2.age)
#“set” meetod muudab millekski muuks
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
d = Dog("Tim", 3)
d.set_age(72)
print(d.get_age())
#loob “Student” klassi, kus leiab nime, vanuse ja hinde
#ning loob “Course” klassi, kus leiab kursuse nime ja õpilaste arvu
#saab leida hetkel 2e õpilase kohta, sest peab maksimumist väiksem olema
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return True
    def get_average_grade(self):
        pass
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)
course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)

#leiab keskmise, võib panna viimases reas ka "student.grade"
#meetodi kasutamine parem (student.get_grade), sest kui hiljem atribuute muuta, siis see kood ei läheks katki
...
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
...

#pärand selle jaoks kui kaks sarnast klassi, näha et neil klassidel aint 1 erinevus, et mida nad räägivad
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("Meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("Bark")
#init-meetodeid pole hetkel vaja, nende puhul eriline vaid mida nad ütlevad
#tuleb luua ülemklass, nt “Pet”, sinna ülemklassi lähevad asjad mis kehtivad siis mõlema kohta, ning individuaalse omadused siis kindla klassi alla
#Et teha “Cat” ja “Dog” klassist alamklassid tuleb neile järele panna sulgudes nende ülemklass
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Iam {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know what I say")
class Cat(Pet):
    def speak(self):
        print("Meow")
class Dog(Pet):
    def speak(self):
        print("Bark")
p = Pet("Tim", 29)
p.speak()
c = Cat("Bill", 44)
c.speak()
d = Dog("Jill", 31)
d.speak()
f = Fish("Bubble", 151)
f.speak()
#Kui alamaklassil on meetod mis on sama nimega mis on meetodil ülemklassis, siis see automaatselt kirjutab selle üle
#ehk alamklassil on rohkem spetsiifiline ning ta võtab pigem selle, kui alamklassil pole võtab ülemklassilt

#superklass = klass millest me pärandame
#innit meetod määrab meetodi, mida tahame kutsuda ning “name” ja “age” on argumendid mida tahame sellele üle anda
#“self”ist pole vaja mööda minna nii et seda ei pane, all vaja lisada värv kui leiame “show” meetodi
...
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
...
c = Cat("Bill", 44, "Red")
c.show()
#me peame kutsuma vanema lähtestamismeetodi välja, enne kui me lihtsalt jätkame ja teeme midagi muud, sest selle vanema lähtestamine võib olla oluline
#see võib teha muid asju, võib kutsuda mõnda teist meetodit
...
class Pet:
    def __init__(self, name, age):
...

#klassi atribuudid - atribuudid, mis on klassile spetsiifilised, mitte selle klassi objektile
class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
p1 = Person("tim")
p2 = Person("jill")
print(p1.number_of_people)
#kuna spetsiifiline klassile mitte juhtumile, siis võib kirjutada “p1” asemel “Person”, saab ligi kasutades klassi nime
print(Person.number_of_people)
#saab muuta samuti klassi nime kasutades, kuna ei muutnud “p2” oma, muutus see ikkagi kuna see oli klassile spetsiifiline
#Python vaatab, et mis on p2-e tüüp, ütleb et “Person”, vaatab kas sellel on omadus “number_of_people”, ei ole, kas klassil on? on küll, siis näitame seda, ning kuna see sai muudetud 8-ks siis on see 8
#kui sama teha p1-ga, saab vastuseks sama numbri, aga kui seda poole pealt muuta siis annab teise numbri
Person.number_of_people = 8
print(p2.number_of_people)
Person.number_of_people = 16
print(p1.number_of_people)
#klassi atribuuti saab kasutada nt inimeste arvu lugemise jaoks, õigemini palju kordi oleme “Person” juhtumeid loonud
class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1
p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("jill")
print(Person.number_of_people)
#vahel tahad määratleda püsiv väärtust, ehk mis kehtib kõigile inimestele, siis sa defineerid selle klassi atribuudina
#et kui tahad võtta selle klassi ja kasutada seda nt kusagil mujal failis, siis see püsiv väärtus on ikkagi defineeritud, erinevalt sellele kui panna see eraldi üles
#nende klassidega on veel see et need on eksporditav
#klassi meetodid on defineeritud natuke erinevalt kui tavalised meetodid, klassimeetodi klassi enda peal, neil pole juhtumitele ligipääsu, mille tõttu on vaja “cls”i “self” asemel, kuna pole objekti, see lihtsalt töötab sellel klassil nt kui tahame suurendada inimeste arvu
#meetod ei saa olla sama mis atribuut, et paneb meetodis “number_of_people” järele alakriipsu
#juhtumile pole vaja ligipääsu, et seda kutsuda, kuigi saab seda teha.
#Saab lihtsalt klassi nimele viidata ja see ei pääse juurde kindlale juhtumile, see ainult pääseb ligi neile klassi atribuutidele, millegile mis on klassile kindel
class Person:
    number_of_people = 0
    GRAVITY = -9.8
    def __init__(self, name):
        self.name = name
        Person.add_person()
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people_())

#Staatilised meetodid - mittemuutuvad meetodid, püsivad samad.
#Nad teevad midagi kuid ei muuda midagi, sest need ei saa seda teha, pole ligipääsu millelegi.
class Math:
    @staticmethod
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr():
        print("run")
Math.pr()
print(Math.add5(5))



#Video 3

#Pythonis kasutame klasse, et luua objekte.
#Objektid koosnevad atribuutidest ja meetoditest.
#Atribuudid esindavad andmeid objekti kohta (nt nimi, värv, kiirus, …)
#Meetodid esindavad funktsionaalsust või tegevusi, mida objektid teha saavad(nt kiirust muuta või dünaamiliselt värvi muuta)

#“Fruit” klass, on 2 atribuuti “name” ja “colour”. Siis võtab muutujanime ja annab selle “Fruit” klassi, nagu tavaliste funktsioonidega.
#Atribuudiväärtustele pääseb lihtsasti ligi, objekti nime välja tuues(“my_fruit”) ning sellel järgneb tahetud atribuudi nimi(“colour”)
class Fruit:
    def __init__(self):
        self.name = "apple"
        self.colour = "red"
my_fruit = Fruit()
print(my_fruit.colour)
#Neid atribuute saab lihtsasti muuta, kirjutades “my_fruit.colour = “green”” või “my_fruit.name = “kiwi””.
#Siis ei ole me piiratud algsetele väärtustele, mille oleme valinud.
#See näide ei ole tegelikult väga hea, sest see piiratud algselt valitud punasele ja õunale
class Fruit:
    def __init__(self):
        self.name = "apple"
        self.colour = "red"
my_fruit = Fruit()
my_fruit.colour = "green"
my_fruit.name = "kiwi"
print(my_fruit.colour)
print(my_fruit.name)
#Parem oleks neid atribuudi väärtuseid koguda parameetritena, mis on “init” funktsiooni sees.
#Oleme määranud parameetrid meie atribuutidele, seeläbi igat klassi “Fruit” juhtumit luues, saab sellele anda erinevaid sorte argumente, mis loovad erinevat sorte “Fruit” objekte.
#Seeläbi pole me ainult piiratud ainult õuntele, saab teha banaane ja mis iganes.
class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
apple = Fruit("apple", "red")
banana = Fruit("banana", "yellow")
kiwi = Fruit("kiwi", "green")
#Meetod “details”, erinevus sellel on see, et peab “self” parameetrist läbi minema sellele funktsioonile, mis seeläbi teeb sellest meetodi.
#Meetodid on kui objektiga seostuvad funktsioonid, see teeb ka “init” funktsioonist meetodi.
#Kui me anname “self” parameetri meetodist meetodile, siis saame me ligi “init” funktsioonis määratletud funktsioonidele, “details” funktsiooni meetodi kehas.
#Nii et kuigi need meetodid on erineva mahuga(scope), “self” võtmesõna kindlustab, et kõik atribuudid on kättesaadavad kõigi meetodite poolt.
class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
    def details(self):
        print("my " + self.name +
              " is " + self.colour)
apple = Fruit("apple", "red")
apple.details()
#Kui unustada “self” parameeter ning üritada inint funktsioonis olevale “experation_date” muutajale ligi pääseda “details” funktsioonist, saab nime vea teate.
#Saab kuna “experation_date” on init funktsiooni kohalik muutuja, kuna on kohalik mitte globaalne, ei tea “details” funktsioon sellest midagi.
#Saab parandada “self” ette pannes või pannes “experation_date” detailidesse.
class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
        exp_date = "07.20.2021"
    def details(self):
        print("expires on " + exp_date)
apple = Fruit("apple", "red")
apple.details()

#Miks "init" meetod oluline: 1)see on koht, kus me lähtestame kõik oma atribuudid; 2)see käivitatakse automaatselt iga uue klassi eksemplari korral; 3)sellel on varunimi

#“self” parameeter alati esindab klassi praegust juhtumit, et kui meetodilt edasi anda meetodile, viitame ikkagi samale objektile
#kuid kui loome uue klassi juhtumi, uue objekti, siis “self” võtmesõna saab uue tähenduse

#OOP: seal initsialiseerime atribuudid; see käivitatakse automaatselt iga uue klassi eksemplariga; sellel on reserveeritud nimi
#Meetodid - klassi sisesed funktsioonid
#Atribuudid - muutujad eesliitega "self"
#Objektid - klassidele määratud muutujad



#Meedium 4

#Objektorienteeritud programmeerimine (OOP) on üks enim kasutatavaid programmeerimise paradigmasid
#Miks seda laialdaselt kasutatakse: 1)Sobib hästi triviaalsete ja keerukate rakenduste ehitamiseks; 2)Võimaldab koodi taaskasutada, suurendades seeläbi tootlikkust; 3)Uusi funktsioone saab hõlpsasti olemasolevasse koodi sisse ehitada; 4)Vähendatud tootmis - ja hoolduskulud
#Levinud OOP-i jaoks kasutatavad programmeerimiskeeled on C++, Java ja C#

#Objektid: Reaalse maailma objekt (nt arvuti, raamat, kast); Kontseptsioon (nt kohtumine, intervjuu); Protsess (nt paberivirna sorteerimine või kahe arvuti võrdlemine nende jõudluse mõõtmiseks)
#Klassid: prototüüp või plaan, millest luuakse objekte
#Klassis on: Atribuutide või omaduste kogum, mis kirjeldab iga objekti; Käitumise või toimingute kogum, mida iga objekt saab sooritada
#Objektil on: Andmekogum (iga selle atribuudi väärtus); Toimingute komplekt, mida see saab teha; Identiteet
#Klass on muutujate kogum (selle atribuutide esindamiseks) ja funktsioonide kogum (selle käitumise kirjeldamiseks), mis toimivad selle muutujatele.
#Objekt on klassi eksemplar, mis hoiab oma muutujates andmeid (väärtusi). Andmetele pääseb juurde selle funktsioonide kaudu.

#Mis on OOP: Paradigma probleemide lahendamiseks objektide interaktsiooni kaudu; See järgib loomulikku probleemide lahendamise viisi
#Nt. Ann tahab oma autot käivitada: (1) Ann kõnnib oma auto juurde; (2) Ann saadab autole teate süüte sisselülitamisega alustamiseks; (3) Auto käivitub

#Abstraktsioon: Olemi oluliste omaduste ja käitumise väljavõtmine; Klass esindab sellist abstraktsiooni ja seda nimetatakse tavaliselt abstraktseks andmetüübiks
#Nt. Rakenduses, mis arvutab karbi saatmiskulu, võtame selle omadused: cost_per_poound, weight ja selle käitumise: shipping_cost()

#Kapseldamine: Mehhanism, mille abil ühendame andmed ja andmeid töötlevad funktsioonid üheks üksuseks; Objektid ja klassid jõustavad kapseldamise

#Pärand: Looge olemasolevatest klassidest (baasklassidest) uusi klasse (tuletatud klassid); Tuletatud klass pärib põhiklassi muutujad ja funktsioonid ning lisab juurde!; Annab võimaluse olemasolevat koodi uuesti kasutada

#Eelised vs miinused: Probleemi klasside ja alamklasside täpseks modelleerimiseks on vaja esialgseid lisapingutusi; Sobib teatud reaalse maailma probleemide modelleerimiseks, erinevalt mõnest teisest

