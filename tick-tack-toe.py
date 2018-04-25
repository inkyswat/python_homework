
#import subprocess # subprocess võimaldab antud kontekstis os'ile käske saata
import os #oleks alternatiiv, kuid try ei suuda seda errorit kinni püüda

alustaja_valitud = False
roll = ""
hetke_seis = [[0,0,0],[0,0,0],[0,0,0]]
rida = ""
veerg = ""
teade = ""
veateade = ""
m2ng_l2bi = False
sisu_test = True
# ================
# FUNKTISOONID
# ================
def tyhjenda_ekraan():
	os.system('cls' if os.name=='nt' else 'clear')
#    try:
 #       subprocess.call('cls')
  #  except:
   #     subprocess.call('clear')


def tyhi_tabel():
    global teade
    print("")
    print("           A       B       C")
    print("")
    print("       -------------------------")
    print("       |       |       |       |")
    print("   1   |       |       |       |")
    print("       |       |       |       |")
    print("       -------------------------")
    print("       |       |       |       |")
    print("   2   |       |       |       |")
    print("       |       |       |       |")
    print("       -------------------------")
    print("       |       |       |       |")
    print("   3   |       |       |       |")
    print("       |       |       |       |")
    print("       -------------------------")
    print(teade)
    print(veateade)
    print("________________________________")


def kysi_koordinaadid():
    global rida
    global veerg
    global veateade
    korrektsed_koordinaadid = False
    while (not korrektsed_koordinaadid):
        tyhjenda_ekraan()
        tyhi_tabel()

        rida = input("Sisesta palun rida (1 - 3) ")
        try:
            rida = int(rida)
            rida -= 1  # et array index oleks õige vähendame rida
            veerg = input("ja nüüd palun veerg (a - c) ")
            veerg = veerg.lower()
            if ((rida >= 0 and rida <= 2) and (veerg == "a" or veerg == "b" or veerg == "c")):
                if (veerg == "a"):
                    veerg = 0
                if (veerg == "b"):
                    veerg = 1
                if (veerg == "c"):
                    veerg = 2

                korrektsed_koordinaadid = True
                veateade = ""
            else:
                korrektsed_koordinaadid = False  
                veateade = f"mängija \'{roll}\' poolt valesti sisestatud koordinaadid"
        except ValueError:
            korrektsed_koordinaadid = False
            veateade = f"mängija \'{roll}\' poolt valesti sisestatud koordinaadid"


def kysi_roll():
    global roll
    global alustaja_valitud
    while (not alustaja_valitud):
        tyhjenda_ekraan()
        tyhi_tabel()
        roll = input("Kumb enne, kas \'o\' või \'x\'? ")
        if (roll == "o" or roll == "x" or roll == "O" or roll == "X"):
            roll = roll.lower()
            alustaja_valitud = True
        else:
            alustaja_valitud = False

def sisu_kontroll(rida, veerg):
    global hetke_seis
    if (hetke_seis[rida][veerg] == 0):
        return True
    else:
        return False    

def sisu_t2itmine(rida, veerg, _roll):
    global hetke_seis
    hetke_seis[rida][veerg] = _roll
    
def rolli_muutmine(_roll):
    global roll
    global teade
    if (_roll == "x"):
        roll = "o"
        teade = f"Preagu on mängija \'{roll}\' kord"
    else:
        roll = "x"
        teade = f"Preagu on mängija \'{roll}\' kord"
# ==========================
# Start
# ==========================
tyhjenda_ekraan()
tyhi_tabel()

kysi_roll()
teade = f"Preagu on mängija \'{roll}\' kord"
for x in range(4):
    kysi_koordinaadid()
    sisu_seis_ok = sisu_kontroll(rida, veerg)
    while (not sisu_seis_ok):
        veateade = "Seal on juba olemas"
        kysi_koordinaadid()
        sisu_seis_ok = sisu_kontroll(rida, veerg)
    sisu_t2itmine(rida, veerg, roll)
    rolli_muutmine(roll)
print(hetke_seis)
