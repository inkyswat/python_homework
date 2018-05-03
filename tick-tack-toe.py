import os  # for os operations
import platform # os platform tools
import time

# ====================
# Colors
# ====================
class Colors:
    CEND      = ['\33[0m',''] # <- for ending color or blinking
    CBOLD     = ['\33[1m', '']
    CITALIC   = ['\33[3m', '']
    CURL      = ['\33[4m', ''] # <- underline
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
color_os = 0
platform = platform.system()
if (platform == "Windows"):
    color_os = 1
else:
    color_os = 0
RolePicked = False
role = ""
GameLooping = True
WriteData = 0
CurState = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]]
row = ""
column = ""
Notific = ""
ErrorMsg = ""
GameOver = False
GameDraw = False
Winner = 2
WinningState = ["",""]
TestMode = 0
WinningStats = ""
GameIterations = 0
X_wins = 0
O_wins = 0
# colors
tableColor = Colors.CBEIGE[color_os]
disp_X_color = Colors.CBLACK[color_os] + Colors.CGREYBG[color_os]
disp_O_color = Colors.CBLACK[color_os] + Colors.CYELLOWBG[color_os]
ErrorMsgCol = Colors.CWHITE[color_os]
disp_X_win_color = Colors.CBLINK[color_os] + Colors.CGREEN[color_os] # + Colors.CGREYBG[color_os]
disp_O_win_color = Colors.CBLINK[color_os] + Colors.CGREEN[color_os] # + Colors.CYELLOWBG[color_os]
PlayAgainCol = Colors.CYELLOW[color_os]

# Table Stuff
dispRow_separator = tableColor + " " * 8 + "-" * 23 + " " + Colors.CEND[color_os]
dispEmptyCell = tableColor + "       |" + Colors.CEND[color_os]

disp_X_Line_1 = disp_X_color + "x     x" + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_X_Line_2 = disp_X_color + "   x   " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_X_Line_3 = disp_X_color + "x     x" + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]

disp_X_Winner_Line_1 = disp_X_win_color + "x \ / x" + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_X_Winner_Line_2 = disp_X_win_color + "   x   " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_X_Winner_Line_3 = disp_X_win_color + "x / \ x" + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]

disp_O_Line_1 = disp_O_color + " (---) " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_O_Line_2 = disp_O_color + "(     )" + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_O_Line_3 = disp_O_color + " (---) " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]

disp_O_Winner_Line_1 = disp_O_win_color + "' 000 '" + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_O_Winner_Line_2 = disp_O_win_color + " 0   0 " + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]
disp_O_Winner_Line_3 = disp_O_win_color + "' 000 '" + Colors.CEND[color_os] + tableColor + "|" + Colors.CEND[color_os]


dispRow_1_number = tableColor + "   1   |" + Colors.CEND[color_os]
dispRow_2_number = tableColor + "   2   |" + Colors.CEND[color_os]
dispRow_3_number = tableColor + "   3   |" + Colors.CEND[color_os]

dispRows = [
    [
        ["0", "0", "0", "0"], 
        ["0", "0", "0", "0"], 
        ["0", "0", "0", "0"]
    ], 
    [
        ["0", "0", "0", "0"], 
        ["0", "0", "0", "0"], 
        ["0", "0", "0", "0"]
    ], 
    [
        ["0", "0", "0", "0"], 
        ["0", "0", "0", "0"], 
        ["0", "0", "0", "0"]
    ]]

# Debug Data
debugData = 1
def debug_fn():
    global DD_head
    global DD_1
    global DD_2
    global DD_3
    global DD_4
    global DD_5
    global DD_6
    global CurState
    DD_head = ["    " + Colors.CWHITE[color_os] + Colors.CBOLD[color_os] + "CurState" + Colors.CEND[color_os], ""]
    DD_1 = [f"       {CurState[0][0]}     {CurState[0][1]}     {CurState[0][2]}",""]
    DD_2 = [f"       {CurState[1][0]}     {CurState[1][1]}     {CurState[1][2]}",""]
    DD_3 = [f"       {CurState[2][0]}     {CurState[2][1]}     {CurState[2][2]}",""]
    DD_4 = [f"    " + Colors.CWHITE[color_os] + Colors.CBOLD[color_os] + "GameIterations = " + Colors.CEND[color_os] + f"{GameIterations}", ""]
    DD_5 = [f"    " + Colors.CWHITE[color_os] + Colors.CBOLD[color_os] + "Player \'X\' wins = " + Colors.CEND[color_os] + f"{X_wins}", ""]
    DD_6 = [f"    " + Colors.CWHITE[color_os] + Colors.CBOLD[color_os] + "Player \'O\' wins = " + Colors.CEND[color_os] + f"{O_wins}", ""]
# ====================
# Functions
# ====================
def debugToggle():
    global debugData
    if (debugData == 1):
        debugData = 0
    else:
        debugData = 1
# -------------------------------------------


def ClearScreen():
	os.system('cls' if os.name=='nt' else 'clear')
# -------------------------------------------

def DisplayTable():
    global Notific
    global ErrorMsg
    global CurState
    global debugData
    global DD_head
    global DD_1
    global DD_2
    global DD_3
    global DD_4
    global DD_5
    global DD_6
    debug_fn() # for realoading debug vars
    print(tableColor)
    print("           A       B       C")
    print("")
    print(dispRow_separator)
    print(dispRows[0][0][0]+dispRows[0][0][1]+dispRows[0][0][2]+dispRows[0][0][3] + DD_head[debugData])
    print(dispRows[0][1][0]+dispRows[0][1][1]+dispRows[0][1][2]+dispRows[0][1][3] + DD_1[debugData])
    print(dispRows[0][2][0]+dispRows[0][2][1]+dispRows[0][2][2]+dispRows[0][2][3] + DD_2[debugData])
    print(dispRow_separator + DD_3[debugData])
    print(dispRows[1][0][0]+dispRows[1][0][1]+dispRows[1][0][2]+dispRows[1][0][3])
    print(dispRows[1][1][0]+dispRows[1][1][1]+dispRows[1][1][2]+dispRows[1][1][3] + DD_4[debugData])
    print(dispRows[1][2][0]+dispRows[1][2][1]+dispRows[1][2][2]+dispRows[1][2][3])
    print(dispRow_separator + DD_5[debugData])
    print(dispRows[2][0][0]+dispRows[2][0][1]+dispRows[2][0][2]+dispRows[2][0][3] + DD_6[debugData])
    print(dispRows[2][1][0]+dispRows[2][1][1]+dispRows[2][1][2]+dispRows[2][1][3])
    print(dispRows[2][2][0]+dispRows[2][2][1]+dispRows[2][2][2]+dispRows[2][2][3])
    print(dispRow_separator)
    print("")
    print(Notific)
    print(ErrorMsg)
    print(WinningStats)
    print(Colors.CGREY[color_os] + "_" * 40)
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
    global debugData
    while (not RolePicked):
        ClearScreen()
        DisplayTable()
        role = input(Colors.CWHITE[color_os] + "      Who goes first \'o\' or \'x\'? " + Colors.CEND[color_os])
        if (role == "o" or role == "x" or role == "O" or role == "X" or role == "debug"):
            if (role != "debug"):
                role = role.lower()
                RolePicked = True
                if (role == "x"):
                    Notific = Colors.CVIOLET[color_os] + "It is your turn " + Colors.CBOLD[color_os] + Colors.CGREY[color_os] +  Colors.CURL[color_os] + f"{role}" + Colors.CEND[color_os]
                    WriteData = 1 # <- for 'x' is -1
                else:
                    Notific = Colors.CVIOLET[color_os] + "It is your turn " + Colors.CBOLD[color_os] + Colors.CYELLOW[color_os] + Colors.CURL[color_os] + f"{role}" + Colors.CEND[color_os]
                    WriteData = -1 # <- for 'o' is -1
            else:
                debugToggle()
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
# calcutates where results will be placed for displaying
def UpdateDispArray():
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
def TableSetup_init():
    global dispRows
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

def TableSetup_final(_winStatParam1, _winStatParam2, _winner):
    global dispRows
    _winner = int(_winner)
    _winStatParam2 = int(_winStatParam2)
    if(_winStatParam1 == "row"):
        for _row_cell in range(3):    
            if (_winner == 1):
                    dispRows[_winStatParam2-1][0][_row_cell+1] = disp_X_Winner_Line_1
                    dispRows[_winStatParam2-1][1][_row_cell+1] = disp_X_Winner_Line_2
                    dispRows[_winStatParam2-1][2][_row_cell+1] = disp_X_Winner_Line_3
            else:    
                    dispRows[_winStatParam2-1][0][_row_cell+1] = disp_O_Winner_Line_1
                    dispRows[_winStatParam2-1][1][_row_cell+1] = disp_O_Winner_Line_2
                    dispRows[_winStatParam2-1][2][_row_cell+1] = disp_O_Winner_Line_3

    if(_winStatParam1 == "column"):
        for _column_cell in range(3):
            if (_winner == 1):
                    dispRows[_column_cell][0][_winStatParam2] = disp_X_Winner_Line_1
                    dispRows[_column_cell][1][_winStatParam2] = disp_X_Winner_Line_2
                    dispRows[_column_cell][2][_winStatParam2] = disp_X_Winner_Line_3
            else:    
                    dispRows[_column_cell][0][_winStatParam2] = disp_O_Winner_Line_1
                    dispRows[_column_cell][1][_winStatParam2] = disp_O_Winner_Line_2
                    dispRows[_column_cell][2][_winStatParam2] = disp_O_Winner_Line_3

    if(_winStatParam1 == "diagonal"):
        if(_winStatParam2 == -1):
            for _diagonal_fall in range(3):
                if (_winner == 1):
                    dispRows[_diagonal_fall][0][_diagonal_fall+1] = disp_X_Winner_Line_1
                    dispRows[_diagonal_fall][1][_diagonal_fall+1] = disp_X_Winner_Line_2
                    dispRows[_diagonal_fall][2][_diagonal_fall+1] = disp_X_Winner_Line_3
                else:
                    dispRows[_diagonal_fall][0][_diagonal_fall+1] = disp_O_Winner_Line_1
                    dispRows[_diagonal_fall][1][_diagonal_fall+1] = disp_O_Winner_Line_2
                    dispRows[_diagonal_fall][2][_diagonal_fall+1] = disp_O_Winner_Line_3
        if(_winStatParam2 == 1):
            _diagonal_rise1 = 0
            for _diagonal_rise2 in range(2, -1, -1):
                if (_winner == 1):
                    dispRows[_diagonal_rise2][0][_diagonal_rise1+1] = disp_X_Winner_Line_1
                    dispRows[_diagonal_rise2][1][_diagonal_rise1+1] = disp_X_Winner_Line_2
                    dispRows[_diagonal_rise2][2][_diagonal_rise1+1] = disp_X_Winner_Line_3
                    _diagonal_rise1 = _diagonal_rise1 + 1
                else:
                    dispRows[_diagonal_rise2][0][_diagonal_rise1+1] = disp_O_Winner_Line_1
                    dispRows[_diagonal_rise2][1][_diagonal_rise1+1] = disp_O_Winner_Line_2
                    dispRows[_diagonal_rise2][2][_diagonal_rise1+1] = disp_O_Winner_Line_3
                    _diagonal_rise1 = _diagonal_rise1 + 1
# -------------------------------------------

def PlayAgainFn():
    global PlayAgainCol
    global GameLooping
    global CurState
    global GameOver
    global RolePicked
    global Notific

    PlayAgain = input(PlayAgainCol + "--- Would you like to play again? --- (Y/N) " + Colors.CEND[color_os])
    while True:
        if (PlayAgain == "N" or PlayAgain == "n" or PlayAgain == "Y" or PlayAgain == "y"):
            if (PlayAgain == "N" or PlayAgain == "n"):
                GameLooping = False
                return False
            else:  # reset variables
                CurState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                GameOver = False
                RolePicked = False
                Notific = ""
                return True
        else:
            PlayAgain = input(PlayAgainCol + "Y or N only " + Colors.CEND[color_os]) 
#    return False               
# -------------------------------------------


def var_dump(_muutuja=""):
    print(f"DEBUG: muutuja väärtus on {_muutuja}")
    input()
# -------------------------------------------

class WinnerCheck():
    global CurState
    WinnerAdder = 0
    TestResult = ""
    def Calc(_TestMode):
        global WinningState
        global TestMode
        TestMode = _TestMode
        if (TestMode == 0): # rows
            for row in range(3):
                for column in range(3):
                    WinnerAdder = CurState[row][0] + CurState[row][1] + CurState[row][2]
                    if (WinnerAdder == 3 or WinnerAdder == -3):
                        WinningState = ["row", row+1]
                        return WinnerAdder
                    WinnerAdder = CurState[0][column] + CurState[1][column] + CurState[2][column]
                    if (WinnerAdder == 3 or WinnerAdder == -3):
                        WinningState = ["column", column+1]
                        return WinnerAdder
        if (TestMode == 1):  # falling diagonal
            WinnerAdder = CurState[0][0] + CurState[1][1] + CurState[2][2]
            if (WinnerAdder == 3 or WinnerAdder == -3):
                WinningState = ["diagonal", -1]
                return WinnerAdder
            
        if (TestMode == 2):  # rising diagonal
            WinnerAdder = CurState[0][2] + CurState[1][1] + CurState[2][0]
            if (WinnerAdder == 3 or WinnerAdder == -3):
                WinningState = ["diagonal", 1]
                return WinnerAdder
        else:
            return


    def test():
        global TestMode
        global Winner
        for TestMode in range(3):
            TestResult = WinnerCheck.Calc(TestMode)

            if(TestResult == 3):
                Winner = "1"
                return 1 # < if winner is x

            if(TestResult == -3):
                Winner = "0"
                return -1 # < if winner is o 
        return

# -------------------------------------------
def setWinningCols():
    global tableColor
    global disp_O_color
    global disp_X_color
    global ErrorMsgCol
    global disp_X_win_color
    global disp_O_win_color
    tableColor = Colors.CBEIGE[color_os]
    disp_X_color = Colors.CBLACK[color_os] + Colors.CGREYBG[color_os]
    disp_O_color = Colors.CBLACK[color_os] + Colors.CYELLOWBG[color_os]
    ErrorMsgCol = Colors.CWHITE[color_os]
    disp_X_win_color = Colors.CBLINK[color_os] + Colors.CGREEN[color_os] # + Colors.CGREYBG[color_os]
    disp_O_win_color = Colors.CBLINK[color_os] + Colors.CGREEN[color_os] # + Colors.CYELLOWBG[color_os]


# ==========================
# Start
# ==========================

while GameLooping:
    GameOver = False
    ClearScreen()
    TableSetup_init()
    DisplayTable()
    AskRole()
    while (GameOver == False):
        for x in range(9):
            AskCoordinates()
            Content_ok = Chck_if_exists(row, column)

            while (not Content_ok):
                ErrorMsg = ErrorMsgCol + "Already filled!" + Colors.CEND[color_os]
                AskCoordinates()
                Content_ok = Chck_if_exists(row, column)
            FillArray(row, column, WriteData)
            _winnerTestResult = WinnerCheck.test()

            if (_winnerTestResult == 1 or _winnerTestResult == -1):
                break
            if (x == 8):
                GameDraw = True
                break
            else:
                ChangeRole(role)
                UpdateDispArray()
                ClearScreen()
                DisplayTable()
        if (GameDraw):
            Notific = f"Draw!"
            UpdateDispArray()
            ClearScreen()
            DisplayTable()
            time.sleep(1)

            if (not PlayAgainFn()):
                break
            else:
                GameOver = True
                TableSetup_init()
                ClearScreen()
                DisplayTable()
                GameIterations = GameIterations + 1
            
        else:   
            GameIterations = GameIterations + 1
            setWinningCols()
            TableSetup_final(WinningState[0], WinningState[1], Winner)
            ClearScreen()
            DisplayTable()
            Winner = int(Winner)
            if (Winner == 1):
                X_wins = X_wins + 1
                Notific = f"Congrats! Player" + Colors.CWHITE[color_os] + " \'X\'" + Colors.CEND[color_os] + " you won!"
            else:
                O_wins = O_wins + 1
                Notific = f"Congrats! Player" + Colors.CWHITE[color_os] + " \'O\'" + Colors.CEND[color_os] + " you won!"
            ClearScreen()
            DisplayTable()
            time.sleep(1.5)

            if (not PlayAgainFn()):
                break
            else:
                GameOver = True
                TableSetup_init()


            
ClearScreen()
print("" + "–" * 47)
print("|"+Colors.CGREEN2[color_os] + "Game Stats:" + Colors.CEND[color_os])
if (X_wins == 1):
    print("|  \'X\' won " + Colors.CBEIGE2[color_os] + f"{X_wins}" + Colors.CEND[color_os] + " game")
else:
    print("|  \'X\' won " + Colors.CBEIGE2[color_os] + f"{X_wins}" + Colors.CEND[color_os] + " games")

if (X_wins == 1):
    print("|  \'O\' won " + Colors.CBEIGE2[color_os] + f"{O_wins}" + Colors.CEND[color_os] + " game")
else:
    print("|  \'O\' won " + Colors.CBEIGE2[color_os] + f"{O_wins}" + Colors.CEND[color_os] + " games")
print("|")
if (GameIterations == 1):
    print("|  You played " + Colors.CBEIGE2[color_os] + f"{GameIterations}" + Colors.CEND[color_os] + " game")
else:
    print("|  You played " + Colors.CBEIGE2[color_os] + f"{GameIterations}" + Colors.CEND[color_os] + " games")
print("|")
print("|" + Colors.CWHITE[color_os] + " -- Thank you for playing, have a nice day! --" + Colors.CEND[color_os])
print(""+"-" * 47)
print("")
