

import os  # võimaldab os'ile käske saata
import platform # os'i platformi vahendid
platform = platform.system()
color_os = 0
RolePicked = False
role = ""
CurState = [[0,0,0],[0,0,0],[0,0,0]]
row = ""
column = ""
Notific = ""
ErrorMsg = ""
GameOver = False
sisu_test = True

# ================
# FUNKTISOONID
# ================
class Colors:
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

def platform_ja_Colors():
    global platform
    if (platform == "Windows"):
        print()
def ClearScreen():
	os.system('cls' if os.name=='nt' else 'clear')

def DisplayTable(): # pane siia sisend ja kontroll kuhu tulemus kirjutada
    global Notific
    print(Colors.CBEIGE[color_os])
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
    print(Notific)
    print(ErrorMsg)
    print(Colors.CGREY[color_os] + "________________________________")


def AskCoordinates():
    global row
    global column
    global ErrorMsg
    Coordin_ok = False
    while (not Coordin_ok):
        ClearScreen()
        DisplayTable()

        row = input(Colors.CBOLD[color_os] + Colors.CGREY[color_os] + "Sisesta palun row (1 - 3) " + Colors.CEND[color_os])
        try:
            row = int(row)
            row -= 1  # et array index oleks õige vähendame row
            column = input(Colors.CBOLD[color_os] + Colors.CGREY[color_os] + "ja nüüd palun column (a - c) " + Colors.CEND[color_os])
            column = column.lower()
            if ((row >= 0 and row <= 2) and (column == "a" or column == "b" or column == "c")):
                if (column == "a"):
                    column = 0
                if (column == "b"):
                    column = 1
                if (column == "c"):
                    column = 2

                Coordin_ok = True
                ErrorMsg = ""
            else:
                Coordin_ok = False  
                ErrorMsg = Colors.CBLINK[color_os] + Colors.CRED2[color_os] + f"mängija {role} poolt valesti sisestatud koordinaadid" + Colors.CEND[color_os]
        except ValueError:
            Coordin_ok = False
            ErrorMsg = Colors.CBLINK[color_os] + Colors.CRED2[color_os] + f"mängija {role} poolt valesti sisestatud koordinaadid" + Colors.CEND[color_os]


def AskRole():
    global role
    global RolePicked
    global Notific
    while (not RolePicked):
        ClearScreen()
        DisplayTable()
        role = input(Colors.CGREEN2[color_os] + "Kumb enne, kas \'o\' või \'x\'? " + Colors.CEND[color_os])
        if (role == "o" or role == "x" or role == "O" or role == "X"):
            role = role.lower()
            RolePicked = True
            if (role == "x"):
                Notific = Colors.CVIOLET[color_os] + "Preagu on mängija " + Colors.CURL[color_os] + Colors.CGREY[color_os] + f"{role}" + Colors.CEND[color_os] + Colors.CVIOLET[color_os] + " kord" + Colors.CEND[color_os]
            else:
                Notific = Colors.CVIOLET[color_os] + "Preagu on mängija " + Colors.CGREEN[color_os] + Colors.CURL[color_os] + f"{role}" + Colors.CEND[color_os] + Colors.CVIOLET[color_os] + " kord" + Colors.CEND[color_os]
        else:
            RolePicked = False

def sisu_kontrole(row, column):
    global CurState
    if (CurState[row][column] == 0):
        return True
    else:
        return False    

def FillArray(row, column, _role):
    global CurState
    CurState[row][column] = _role
    
def ChangeRole(_role):
    global role
    global Notific
    if (_role == "x"):
        role = "o"
        Notific = Colors.CVIOLET[color_os] + "Preagu on mängija " + Colors.CGREEN[color_os] + Colors.CURL[color_os] + f"{role}" + Colors.CEND[color_os] + Colors.CVIOLET[color_os] + " kord" + Colors.CEND[color_os]
    else:
        role = "x"
        Notific = Colors.CVIOLET[color_os] + "Preagu on mängija " + Colors.CURL[color_os] + Colors.CGREY[color_os] + f"{role}" + Colors.CEND[color_os] + Colors.CVIOLET[color_os] + " kord" + Colors.CEND[color_os]
# massiivist mitme elemedi korraga accessimine
# massiiv[1:3] => ühest kolmeni elemendid

# ==========================
# Start
# ==========================
if (platform == "Windows"):
    color_os = 1
else:
    color_os = 0  
# print(Colors.CGREEN2[color_os])
# while True:
#     print      
ClearScreen()
DisplayTable()

AskRole()
for x in range(2):
    AskCoordinates()
    sisu_seis_ok = sisu_kontrole(row, column)
    while (not sisu_seis_ok):
        ErrorMsg = Colors.CWHITE2[color_os] + "Seal on juba olemas"
        AskCoordinates()
        sisu_seis_ok = sisu_kontrole(row, column)
    FillArray(row, column, role)
    ChangeRole(role)
print(CurState)
