"""
02 - trips-traps-trull.py
Ülesande eesmärgiks on luua Trips-Traps-Trulli mäng, mis palub vaheldumisi 'X' ja 'O'
mängijal öelda rea ja veeru koordinaadid (mõlemad vahemikus 1-3, esmalt rida, siis veerg),
kuhu ta oma sümbolit sisestada soovib.
Peale igat sisestust kuvab tabeli hetkeseisu ning niipea kui kas üks veerg, rida või
diagonaal on kõik sama märgi käes, kuulutatakse ta võitjaks. Kui kõik mänguväljad on
täis ja ühtegi täisrida, -veergu ega -diagonaali pole, jääb mäng viiki.
Sisestamisel tuleb kontrollida ka kas soovitud väljas on juba midagi ees ja kui on,
siis sellest teada anda ja paluda uuesti koordinaadid sisestada. Koordinaatide puhul
tuleb kontrollida ka nende korrektsust ning õiget numbrite vahemikku. Väära koordinaadi
tuvastamisel tuleb veast teavitada ja samuti küsimust korrata. 
Kui kasutaja soovib arvamise katkestada enne mängu lõppu, võib ta sisestada lihtsalt 
tühja rea (rida, milles on vaid ENTER klahvi vajutus)
"""

import os
import sys
import re

# Ekraani puhastamine
def clear():
     # windows
    if os.name == 'nt':
        _ = os.system('cls')
     # mac ja linux
    else:
        _ = os.system('clear')


# Tabeli joonistamise funktsioon
def joonista_tabel():
    clear()
    print(" ")    
    print("", tabel["1:1"], "|", tabel["1:2"], "|", tabel["1:3"])
    print ("---+---+---")
    print("", tabel["2:1"], "|", tabel["2:2"], "|", tabel["2:3"])
    print ("---+---+---")
    print("", tabel["3:1"], "|", tabel["3:2"], "|", tabel["3:3"])
    print(" ")

# Sisestamise funktsioon
def sisesta(n):
    while True:
        print("Palun sisesta",n, end='')
        ruut = input(" asukoht rida:veerg. Lopetamiseks enter: ")
        if  len(str(ruut)) == 0:
            sys.exit(0)
        if re.search("[1-3]:[1-3]", ruut):
            if tabel[ruut] == " ":
                tabel[ruut] = n
                break
            else:
                print("See ruut on juba täis!")
        
        
# Kontrollimise funktsioon
def kontrolli():
    if (tabel["1:1"] !=" "):
        if (((tabel["1:1"] == tabel["1:2"]) and (tabel["1:1"] == tabel["1:3"])) or ((tabel["1:1"] == tabel["2:1"]) and (tabel["1:1"] == tabel["3:1"]) or ((tabel["1:1"] == tabel["2:2"]) and (tabel["1:1"] == tabel["3:3"])))) :
            print("Võitis:", tabel["1:1"])
            sys.exit(0)
    if (tabel["2:2"] !=" "): 
        if ((tabel["2:2"] == tabel["2:1"] and tabel["2:2"] == tabel["2:3"]) or (tabel["2:2"] == tabel["1:2"] and tabel["2:2"] == tabel["3:2"]) or (tabel["2:2"] == tabel["3:1"] and tabel["2:2"] == tabel["1:3"])):
            print("Võitis:", tabel["2:2"])
            sys.exit(0)
    if (tabel["3:3"] !=" "):
        if ((tabel["3:3"] == tabel["3:1"] and tabel["3:3"] == tabel["3:2"]) or (tabel["3:3"] == tabel["2:3"] and tabel["3:3"] == tabel["1:3"])):
            print("Võitis:", tabel["3:3"])
            sys.exit(0)





tabel = {"1:1":" ", "1:2":" ", "1:3":" ", "2:1":" ", "2:2":" ", "2:3":" ", "3:1":" ", "3:2":" ", "3:3":" "}

i = 1

joonista_tabel()
while i < 9:
    sisesta("X")
    joonista_tabel()
    kontrolli()
    sisesta("O")
    joonista_tabel()
    kontrolli()
    i = i+2
    if i == 9 :
        print("Viik!!!")


