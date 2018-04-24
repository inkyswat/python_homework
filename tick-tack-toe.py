
import subprocess # subprocess võimaldab antud kontekstis os'ile käske saata
# 'import os' oleks alternatiiv, kuid try ei suuda seda errorit kinni püüda

sisend = ""
roll = False
valik = [[],[],[]]
# ================
# FUNKTISOONID
# ================
def tyhjenda_ekraan():
    try:
        subprocess.call('cls')
    except:
        subprocess.call('clear')


def tyhi_tabel():
    print("")
    print("           A       B       C")
    print("")
    print("       =========================")
    print("       |       |       |       |")
    print("   1   |       |       |       |")
    print("       |       |       |       |")
    print("       =========================")
    print("       |       |       |       |")
    print("   2   |       |       |       |")
    print("       |       |       |       |")
    print("       =========================")
    print("       |       |       |       |")
    print("   3   |       |       |       |")
    print("       |       |       |       |")
    print("       =========================")
    print("")

def ring_voi_x(sisend):
    print()

def kysi_sisendeid():
    global roll # global variable'i accessimine, selleks on vaja fn'i sees global def'da
    if (roll):
        global valik
        valik[1] = input("Sisesta palun rida (1 - 3) ")
        valik[2] = input("Sisesta palun veerg (A - C) ")
    else:
        sisend = input("kes alustab, kas O või X ?")
        roll = True
    

def arvuta_tabel(hetke_seis):
    print()



tyhjenda_ekraan()
tyhi_tabel()
kysi_sisendeid()

# hetke_seis = [[0,1,0],[1,0,1],[0,1,0]]
# print (hetke_seis[1][2])
