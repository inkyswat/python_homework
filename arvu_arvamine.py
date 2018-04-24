# see programm genereerib numbri 1 - 50 ja palub selle ära arvata
# juhul kui arvamise käigus pakutakse vigast sisendit, siis arvamiste kord ei suurene

arvatav = 0
katseid = 0
arvatud = False # ära arvamise staatus
vigane = False # vigase sisendi alg staatus

import random
for x in range(1):
  arvatav = random.randint(1, 50)
while True:
    sisend = input("Siseste number vahemikus 1 - 50: ")
    if len(sisend) == 0:
        break
    elif (not vigane): 
        katseid += 1
    else:  # kui eelneval sisestamisel toodeti pläma, siis ei suurendata katseid muutujat
        print()
    try: # proovib siin tsüklis stringi teha numbriks, kui saab vea, siis läheb excepti ja loobib kama välja, et jama oli
        sisend_arvuna = int(sisend) # sisestatud string numbriks

        if (sisend_arvuna == arvatav):
            arvatud = True
            break
        elif (sisend_arvuna < arvatav):
            print("Suuremat on vaja!")
            vigane = False
        else:    
            print("Liiga suur!")
            vigane = False
    except:
        print("Vigane arv, proovi uuesti")
        vigane = True

if(arvatud): # f enne stringi on selleks, et stringi seest loetaks muutujaid
    print(f"Tubli, arvasid korrektselt, õige number on {arvatav}! Sa tegid seda {katseid} korraga")
else:
    print(f"Katkestasid ilma arvamata! Proovisid {katseid} korda.")
