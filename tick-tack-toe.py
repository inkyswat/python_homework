

import os  # võimaldab os'ile käske saata
import platform # os'i platvormi vahendid
platvorm = platform.system()
color_os = 0
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
class v2rvid:
    CEND      = ['\33[0m',''] # värvi lõpetamiseks (näiteks: vilkumine))
    CBOLD     = ['\33[1m', '']
    CITALIC   = ['\33[3m', '']
    CURL      = ['\33[4m', '']
    CBLINK    = ['\33[5m', '']
    CBLINK2   = ['\33[6m', '']
    CSELECTED = ['\33[7m', '']

    CBLACK    = ['\33[30m', '']
    CRED      = ['\33[31m', '']
    CGREEN    = ['\33[32m', '']
    CYELLOW   = ['\33[33m', '']
    CBLUE     = ['\33[34m', '']
    CVIOLET   = ['\33[35m', '']
    CBEIGE    = ['\33[36m', '']
    CWHITE    = ['\33[37m', '']
# background colors
    CBLACKBG  = ['\33[40m', '']
    CREDBG    = ['\33[41m', '']
    CGREENBG  = ['\33[42m', '']
    CYELLOWBG = ['\33[43m', '']
    CBLUEBG   = ['\33[44m', '']
    CVIOLETBG = ['\33[45m', '']
    CBEIGEBG  = ['\33[46m', '']
    CWHITEBG  = ['\33[47m', '']

    CGREY     = ['\33[90m', '']
    CRED2     = ['\33[91m', '']
    CGREEN2   = ['\33[92m', '']
    CYELLOW2  = ['\33[93m', '']
    CBLUE2    = ['\33[94m', '']
    CVIOLET2  = ['\33[95m', '']
    CBEIGE2   = ['\33[96m', '']
    CWHITE2   = ['\33[97m', '']

    CGREYBG    = ['\33[100m', '']
    CREDBG2    = ['\33[101m', '']
    CGREENBG2  = ['\33[102m', '']
    CYELLOWBG2 = ['\33[103m', '']
    CBLUEBG2   = ['\33[104m', '']
    CVIOLETBG2 = ['\33[105m', '']
    CBEIGEBG2  = ['\33[106m', '']
    CWHITEBG2  = ['\33[107m', '']

def platvorm_ja_v2rvid():
    global platvorm
    if (platvorm == "Windows"):
        print()
def tyhjenda_ekraan():
	os.system('cls' if os.name=='nt' else 'clear')

def kuva_tabel():
    global teade
    print(v2rvid.CBEIGE[color_os])
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
    print(v2rvid.CGREY[color_os] + "________________________________")


def kysi_koordinaadid():
    global rida
    global veerg
    global veateade
    korrektsed_koordinaadid = False
    while (not korrektsed_koordinaadid):
        tyhjenda_ekraan()
        kuva_tabel()

        rida = input(v2rvid.CBOLD[color_os] + v2rvid.CGREY[color_os] + "Sisesta palun rida (1 - 3) " + v2rvid.CEND[color_os])
        try:
            rida = int(rida)
            rida -= 1  # et array index oleks õige vähendame rida
            veerg = input(v2rvid.CBOLD[color_os] + v2rvid.CGREY[color_os] + "ja nüüd palun veerg (a - c) " + v2rvid.CEND[color_os])
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
                veateade = v2rvid.CBLINK[color_os] + v2rvid.CRED2[color_os] + f"mängija {roll} poolt valesti sisestatud koordinaadid" + v2rvid.CEND[color_os]
        except ValueError:
            korrektsed_koordinaadid = False
            veateade = v2rvid.CBLINK[color_os] + v2rvid.CRED2[color_os] + f"mängija {roll} poolt valesti sisestatud koordinaadid" + v2rvid.CEND[color_os]


def kysi_roll():
    global roll
    global alustaja_valitud
    global teade
    while (not alustaja_valitud):
        tyhjenda_ekraan()
        kuva_tabel()
        roll = input(v2rvid.CGREEN2[color_os] + "Kumb enne, kas \'o\' või \'x\'? " + v2rvid.CEND[color_os])
        if (roll == "o" or roll == "x" or roll == "O" or roll == "X"):
            roll = roll.lower()
            alustaja_valitud = True
            if (roll == "x"):
                teade = v2rvid.CVIOLET[color_os] + "Preagu on mängija " + v2rvid.CURL[color_os] + v2rvid.CGREY[color_os] + f"{roll}" + v2rvid.CEND[color_os] + v2rvid.CVIOLET[color_os] + " kord" + v2rvid.CEND[color_os]
            else:
                teade = v2rvid.CVIOLET[color_os] + "Preagu on mängija " + v2rvid.CGREEN[color_os] + v2rvid.CURL[color_os] + f"{roll}" + v2rvid.CEND[color_os] + v2rvid.CVIOLET[color_os] + " kord" + v2rvid.CEND[color_os]
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
        teade = v2rvid.CVIOLET[color_os] + "Preagu on mängija " + v2rvid.CGREEN[color_os] + v2rvid.CURL[color_os] + f"{roll}" + v2rvid.CEND[color_os] + v2rvid.CVIOLET[color_os] + " kord" + v2rvid.CEND[color_os]
    else:
        roll = "x"
        teade = v2rvid.CVIOLET[color_os] + "Preagu on mängija " + v2rvid.CURL[color_os] + v2rvid.CGREY[color_os] + f"{roll}" + v2rvid.CEND[color_os] + v2rvid.CVIOLET[color_os] + " kord" + v2rvid.CEND[color_os]
# massiivist mitme elemedi korraga accessimine
# massiiv[1:3] => ühest kolmeni elemendid

# ==========================
# Start
# ==========================
if (platvorm == "Windows"):
    color_os = 1
else:
    color_os = 0  
# print(v2rvid.CGREEN2[color_os])
# while True:
#     print      
tyhjenda_ekraan()
kuva_tabel()

kysi_roll()
for x in range(4):
    kysi_koordinaadid()
    sisu_seis_ok = sisu_kontroll(rida, veerg)
    while (not sisu_seis_ok):
        veateade = v2rvid.CWHITE2[color_os] + "Seal on juba olemas"
        kysi_koordinaadid()
        sisu_seis_ok = sisu_kontroll(rida, veerg)
    sisu_t2itmine(rida, veerg, roll)
    rolli_muutmine(roll)
print(hetke_seis)
