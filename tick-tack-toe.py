import os  # for os operations
import platform # os platform tools

# ====================
# Colors
# ====================
class Colors:
    CEND      = ['\33[0m',''] # <- for ending color or blinking

    CBOLD     = ['\33[1m', '']
    CITALIC   = ['\33[3m', '']
    CURL      = ['\33[4m', '']
    CBLINK    = ['\33[5m', ''] # <- blinking
    CBLINK2   = ['\33[6m', ''] # <- blinking
    CSELECTED = ['\33[7m', '']

    CBLACK    = ['\33[30m', '']
    CRED      = ['\33[31m', '']
    CGREEN    = ['\33[32m', '']
    CYELLOW   = ['\33[33m', '']
    CBLUE     = ['\33[34m', '']
    CVIOLET   = ['\33[35m', '']
    CBEIGE    = ['\33[36m', '']
    CWHITE    = ['\33[37m', '']

    CGREY     = ['\33[90m', '']
    CRED2     = ['\33[91m', '']
    CGREEN2   = ['\33[92m', '']
    CYELLOW2  = ['\33[93m', '']
    CBLUE2    = ['\33[94m', '']
    CVIOLET2  = ['\33[95m', '']
    CBEIGE2   = ['\33[96m', '']
    CWHITE2   = ['\33[97m', '']

# background colors
    CBLACKBG  = ['\33[40m', '']
    CREDBG    = ['\33[41m', '']
    CGREENBG  = ['\33[42m', '']
    CYELLOWBG = ['\33[43m', '']
    CBLUEBG   = ['\33[44m', '']
    CVIOLETBG = ['\33[45m', '']
    CBEIGEBG  = ['\33[46m', '']
    CWHITEBG  = ['\33[47m', '']

    CGREYBG    = ['\33[100m', '']
    CREDBG2    = ['\33[101m', '']
    CGREENBG2  = ['\33[102m', '']
    CYELLOWBG2 = ['\33[103m', '']
    CBLUEBG2   = ['\33[104m', '']
    CVIOLETBG2 = ['\33[105m', '']
    CBEIGEBG2  = ['\33[106m', '']
    CWHITEBG2  = ['\33[107m', '']


# -------------------------------------------
# variables
# -------------------------------------------
platform = platform.system()
color_os = 0
RolePicked = False
role = ""
WriteData = 0
CurState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
row = ""
column = ""
Notific = ""
ErrorMsg = ""
GameOver = False
WinnerAdder = ""
WinnerObj = ""
# colors
tableColor = Colors.CBEIGE[color_os]
disp_X_color = Colors.CBLACK[color_os] + Colors.CGREYBG[color_os]
disp_O_color = Colors.CBLACK[color_os] + Colors.CYELLOWBG[color_os]
ErrorMsgCol = Colors.CWHITE[color_os]


# Table Stuff
dispRow_separator = tableColor + "        =======================" + Colors.CEND[color_os]
dispEmptyCell = tableColor + "       |" + Colors.CEND[color_os]

disp_X_Line_1 = disp_X_color + "  \ /  " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_X_Line_2 = disp_X_color + "   x   " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_X_Line_3 = disp_X_color + "  / \  " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]

disp_O_Line_1 = disp_O_color + " /---\ " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_O_Line_2 = disp_O_color + "(CRCLE)" + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_O_Line_3 = disp_O_color + " \---/ " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]

dispRow_1_number = tableColor + "   1   |" + Colors.CEND[color_os]
dispRow_2_number = tableColor + "   2   |" + Colors.CEND[color_os]
dispRow_3_number = tableColor + "   3   |" + Colors.CEND[color_os]

dispRows = [[["0", "0", "0", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]], [["0", "0", "0", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]], [["0", "0", "0", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]]]


# ====================
# Functions
# ====================

def ClearScreen():
	os.system('cls' if os.name=='nt' else 'clear')
# -------------------------------------------

def DisplayTable():
    global Notific
    global ErrorMsg
    print(tableColor)
    print("           A       B       C")
    print("")
    print(dispRow_separator)
    print(dispRows[0][0][0]+dispRows[0][0][1]+dispRows[0][0][2]+dispRows[0][0][3])
    print(dispRows[0][1][0]+dispRows[0][1][1]+dispRows[0][1][2]+dispRows[0][1][3])
    print(dispRows[0][2][0]+dispRows[0][2][1]+dispRows[0][2][2]+dispRows[0][2][3])
    print(dispRow_separator)
    print(dispRows[1][0][0]+dispRows[1][0][1]+dispRows[1][0][2]+dispRows[1][0][3])
    print(dispRows[1][1][0]+dispRows[1][1][1]+dispRows[1][1][2]+dispRows[1][1][3])
    print(dispRows[1][2][0]+dispRows[1][2][1]+dispRows[1][2][2]+dispRows[1][2][3])
    print(dispRow_separator)
    print(dispRows[2][0][0]+dispRows[2][0][1]+dispRows[2][0][2]+dispRows[2][0][3])
    print(dispRows[2][1][0]+dispRows[2][1][1]+dispRows[2][1][2]+dispRows[2][1][3])
    print(dispRows[2][2][0]+dispRows[2][2][1]+dispRows[2][2][2]+dispRows[2][2][3])
    print(dispRow_separator)
    print(Notific)
    print(ErrorMsg)
    print(Colors.CGREY[color_os] + "________________________________")
# -------------------------------------------


def AskCoordinates():
    global row
    global column
    global ErrorMsg
    Coordin_ok = False
    while (not Coordin_ok):
        ClearScreen()
        DisplayTable()

        row = input(Colors.CBOLD[color_os] + Colors.CGREY[color_os] + "      Please enter row (1 - 3) " + Colors.CEND[color_os])
        try:
            row = int(row)
            row -= 1  # <- for correct array index we'll to -1
            column = input(Colors.CBOLD[color_os] + Colors.CGREY[color_os] + "  ... and now column please (a - c) " + Colors.CEND[color_os])
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
                ErrorMsg = Colors.CBLINK[color_os] + Colors.CRED2[color_os] + f"Incorrect parameters given by player {role}" + Colors.CEND[color_os]
        except ValueError:
            Coordin_ok = False
            ErrorMsg = Colors.CBLINK[color_os] + Colors.CRED2[color_os] + f"Incorrect parameters given by player {role}" + Colors.CEND[color_os]
# -------------------------------------------


def AskRole():
    global role
    global RolePicked
    global Notific
    global WriteData
    while (not RolePicked):
        ClearScreen()
        DisplayTable()
        role = input(Colors.CWHITE[color_os] + "      Who goes first \'o\' or \'x\'? " + Colors.CEND[color_os])
        if (role == "o" or role == "x" or role == "O" or role == "X"):
            role = role.lower()
            RolePicked = True
            if (role == "x"):
                Notific = Colors.CVIOLET[color_os] + "It is your turn " + Colors.CBOLD[color_os] + Colors.CGREY[color_os] +  Colors.CURL[color_os] + f"{role}" + Colors.CEND[color_os]
                WriteData = 1
            else:
                Notific = Colors.CVIOLET[color_os] + "It is your turn " + Colors.CBOLD[color_os] + Colors.CYELLOW[color_os] + Colors.CURL[color_os] + f"{role}" + Colors.CEND[color_os]
                WriteData = -1 # <- for 'o' is -1
        else:
            RolePicked = False
# -------------------------------------------


def Chck_if_exists(row, column):
    global CurState
    if (CurState[row][column] == 0):
        return True
    else:
        return False    
# -------------------------------------------


def FillArray(row, column, _role):
    global CurState
    CurState[row][column] = _role
# -------------------------------------------


def ChangeRole(_role):
    global role
    global Notific
    global WriteData
    if (_role == "x"):
        role = "o"
        WriteData = -1
        Notific = Colors.CVIOLET[color_os] + "It is your turn " + Colors.CBOLD[color_os] + Colors.CYELLOW[color_os] + Colors.CURL[color_os] + f"{role}" + Colors.CEND[color_os]
    else:
        role = "x"
        WriteData = 1
        Notific = Colors.CVIOLET[color_os] + "It is your turn " + Colors.CBOLD[color_os] + Colors.CGREY[color_os] + Colors.CURL[color_os] + f"{role}" + Colors.CEND[color_os]

# -------------------------------------------
def CalcDispArrays():
    global CurState
    for row in range(0, 3):
        for cell in range(0, 3):
            if(CurState[row][cell] == -1):
                dispRows[row][0][cell+1] = disp_O_Line_1
                dispRows[row][1][cell+1] = disp_O_Line_2
                dispRows[row][2][cell+1] = disp_O_Line_3
            if(CurState[row][cell] == 1):
                dispRows[row][0][cell+1] = disp_X_Line_1
                dispRows[row][1][cell+1] = disp_X_Line_2
                dispRows[row][2][cell+1] = disp_X_Line_3

# -------------------------------------------

def TableInit():
    for row in range(0, 3):
        for line in range(0, 3):
            for cell in range(0, 4):
                if ((row == 0 and line == 1 and cell == 0) or (row == 1 and line == 1 and cell == 0) or (row == 2 and line == 1 and cell == 0)):
                    dispRows[0][1][0] = dispRow_1_number
                    dispRows[1][1][0] = dispRow_2_number
                    dispRows[2][1][0] = dispRow_3_number
                else:
                    dispRows[row][line][cell] = dispEmptyCell
# -------------------------------------------

class WinnerCheck:
    global CurState
    global WinnerAdder
    TempVar = ""
    def Calc(TestCounter):
        if (TestMode == 0):
            for line in range(3):
                WinnerAdder = CurState[line][0] + CurState[line][1] + CurState[line][2]
                if (WinnerAdder == 3):
                    return 3
                if (WinnerAdder == -3):
                    return -3
            else:
                return    
        if (TestMode == 1):
            print()
        if (TestMode == 2):
            print()

    def test():
        for TestMode in range(3):
            TempVar = self.Calc(TestMode)

            if(TempVar == 3):
                return 1 # < if winner is x
            if(TempVar == -3):
                return -1 # < if winner is o 
        print()
  #  if ((CurState[0][0] + CurState[0][1] + CurState[0][2] == 3) or )
     
# -------------------------------------------

def MarkWinnerCells():
    print()

# ===========================================
# ===========================================



# ==========================
# Start
# ==========================
if (platform == "Windows"):
    color_os = 1
else:
    color_os = 0  

ClearScreen()
TableInit()
DisplayTable()

AskRole()
for x in range(9):
    AskCoordinates()
    Content_ok = Chck_if_exists(row, column)
    if (not GameOver):
        while (not Content_ok):
            ErrorMsg = ErrorMsgCol + "Already filled!" + Colors.CEND[color_os]
            AskCoordinates()
            Content_ok = Chck_if_exists(row, column)
        FillArray(row, column, WriteData)
        ChangeRole(role)
        CalcDispArrays()
        ClearScreen()
        DisplayTable()
    else:
        MarkWinnerCells()
        DisplayTable()
print(CurState)
