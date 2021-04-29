from playsound import playsound
from datetime import datetime
from timer import Timer
import random, time
import tkinter as tk

# TO DO
# Add times to data.txt

# Just a deck of cards in the 'Value, Name' format
cards = [['1','2S'],['2','3S'],['3','4S'],['4','5S'],['5','6S'],['6','7S'],['7','8S'],['8','9S'],['9','10S'],['10','JS'],['11','QS'],['12','KS'],['13','AS'],['1','2C'],['2','3C'],['3','4C'],['4','5C'],['5','6C'],['6','7C'],['7','8C'],['8','9C'],['9','10C'],['10','JC'],['11','QC'],['12','KC'],['13','AC'],['1','2H'],['2','3H'],['3','4H'],['4','5H'],['5','6H'],['6','7H'],['7','8H'],['8','9H'],['9','10H'],['10','JH'],['11','QH'],['12','KH'],['13','AH'],['1','2D'],['2','3D'],['3','4D'],['4','5D'],['5','6D'],['6','7D'],['7','8D'],['8','9D'],['9','10D'],['10','JD'],['11','QD'],['12','KD'],['13','AD']]

global pl1, pl2 # Player 1's hand, Player 2's hand
pl1 = [] # Creating player 1's hand
pl2 = [] # Creating player 2's hand

def win(num) : # Outputs the winner and adds this rounds data to data.txt
    print("Congrats Player", num, "You Won") # Prints to terminal a winning message
    stat = open('War/stats.txt', 'a') # Opens the stats.txt
    txt = str(num) + " " + str(cnt) + "\n" # Formats this rounds data
    stat.write(txt) # Adds this rounds data to stats.txt
    stat.close() # Closes the file
    #if num == 1 :
    #    playsound("sounds/classic_hurt.mp3", False) # Plays the Minecraft hurt sound if player 1 wins
    #else :
    #    playsound("sounds/roblox-death-sound_1.mp3", False) # Plays the Roblox oof sound when player 2 wins

def again() :
    random.shuffle(cards)
    lent = len(cards) // 2
    global pl1, pl2, cnt
    cnt = int(0)
    pl1 = cards[lent:]
    pl2 = cards[:lent]
    print(pl1)
    print(pl2)
    display()
    main()
    ave()

def run1() :
    run(1)
def run5() :
    run(5)
def run10() :
    run(10)
def runX() :
    num = rXEnt.get()
    try :
        num = int(num)
    except :
        num = 2
    run(num)

def sizeUpdate() :

    sz = window.geometry()
    cut = sz.find('x')
    x = int(sz[:cut])
    cut2 = sz.find('+')
    y = int(sz[cut + 1:cut2])
    x = x / 3
    y = y / 5
    r1 = x / y
    r2 = y / x
    ratio = (r1 + r2) / 2
    
    window.update()

def getPad(pad) :
    sz = window.geometry()
    if pad == 'x' :
        cut = sz.find('x')
        x = float(sz[:cut])
        print(x)
        x = x / 30
        print(x)
        x = x / window.grid_size()[1]
        print(x)
        return x
    elif pad == 'y' :
        cut = sz.find('x')
        cut2 = sz.find('+')
        y = float(sz[cut + 1:cut2])
        y = y / 3
        y = y / window.grid_size()[0]
        print(y)
        return y
    else :
        print("FUCK")
        return 5

def randomColor() :
    color = '#'
    for i in range(6) :
        color = color + random.choice("1234567890ABCDEF")
    print(color)
    return color

def run(num) :
    now = datetime.now()
    p1NDis["text"] = "Player 1\nStart Time : " + now.strftime("%H:%M:%S")
    p2NDis["text"] = "Player 2\n"
    timmyTimer = Timer()
    timmyTimer.start()
    for i in range(int(num)) :
        lftDis["text"] = 'Rounds Left: ' + str(int(num) - i) + "\nTime Elapsed: " + str(round(timmyTimer.getTime(), 3)) + " Seconds\nPredicted Time Left: " + timeLeft(i, int(num), timmyTimer, 1)
        p2NDis["text"] =  'Player 2\nPredicted Finish:\n' + timeLeft(i, int(num), timmyTimer, 2)
        again()
        color = randomColor()
        window.tk_setPalette("background", color)
        window.update()

    lftDis["text"] = 'Finished: ' + str(num) + '\nElapsed Time: ' + timmyTimer.stop()
    p2NDis["text"] = "Player 2\nEnd Time : " + datetime.now().strftime("%H:%M:%S")
    window.update()
    if num >= 50 :
        playsound('sounds/air-raid_1.mp3', False)

def timeLeft(crnt, ttl, tim, lvl) : # To return predicted time left
    rtn = tim.getTime() / (crnt + 1)
    rtn = rtn * (ttl - crnt)
    if lvl == 1 :
        rtn = round(rtn, 3)
        numM = rtn % 3600
        numH = rtn - numM
        numH = numH / 3600
        numS = numM % 60
        numM = (rtn - (numH * 3600)) / 60
        if numS < 10 :
            numS = '0' + str(int(numS))
        else :
            numS = str(int(numS))
        if numM < 10 :
            numM = '0' + str(int(numM))
        else :
            numM = str(int(numM))
        if numH >= 24 :
            numD = int(numH % 24)
            numH = numH - (numD * 24)
            return str(int(numD)) + ' Days ' + str(int(numH)) + ':' + numM + ':' + numS
        elif numH > 0 :
            return str(int(numH)) + ':' + numM + ':' + numS
        elif int(numM) > 0 :
            return numM + ':' + numS
        elif int(numS) > 10 :
            return str(numS)
        else :
            return '0:' + str(numS)
    elif lvl == 2 :
        rtn = rtn + tim.getStartTime()
        tim = time.time()
        rtn = rtn + tim
        rtn = time.localtime(rtn)
        if rtn.tm_yday != time.localtime().tm_yday :
            return time.strftime("%D %H:%M:%S", rtn)
        else :
            return time.strftime("%H:%M:%S", rtn)
    
def ave() :
    p1W = 0
    avW = 0
    p2W = 0
    tmp = 0
    lis1 = []
    lis2 = []
    data = open("War/stats.txt", 'r')
    stats = list(data)
    data.close()
    try :
        for i in stats :
            lis1.append(i[:1])
            lis2.append(i[2:-1])
        for i in lis1 :
            if int(i) == 1 :
                p1W += 1
            elif int(i) == 2 :
                p2W += 1
        for i in lis2 :
            tmp += int(i)
        tmp = float(tmp / len(lis2))
        avW = float(format(tmp, ".3f"))
    except :
        print("fail")

    p1WDis["text"] = "Total Wins\n" + str(p1W)
    aveDis["text"] = "Average\n" + str(avW)
    p2WDis["text"] = "Total Wins\n" + str(p2W)

    sizeUpdate()

    window.update()

def clearScn() :
    global sure # Makes sure global
    sure = tk.Tk() # Creates new window
    sure.tk_setPalette("teal") # Sets main background color to 'teal'
    sure.title("Are You Sure") # Labels the window 'Are You Sure'
    sure.resizable(width = False, height = False) # Disables resizing of sure
    sure.rowconfigure([0,1], minsize = 50) # Adds rows at a min height of 50
    sure.columnconfigure([0,1], minsize = 50) # Adds columns at a min width of 50
    sure.geometry('+500+450') # Positions sure at 500x450
    areSure = tk.Label(master = sure, text = 'Are you sure you want to erase the past', font = ("TkDefaultFont", ftSize)) # Label asking if you want to clear
    areSure.grid(row = 0, columnspan = 2) # Positions label
    yesBut = tk.Button(master = sure, text = 'Yes', command = clrScreen, font = ("TkDefaultFont", ftSize)) # Creates yes button on sure window
    yesBut.grid(row = 1, column = 0, sticky = 'nsew') # Positions Yes
    noBut = tk.Button(master = sure, text = 'No', command = sure.destroy, font = ("TkDefaultFont", ftSize)) # Creates no button on sure window
    noBut.grid(row = 1, column = 1, sticky = 'nsew') # Positions No
    sure.update() # Updates sure

def clrScreen() : # Clears the past data while adding it to a master data file
    sure.destroy()
    data = open("War/stats.txt", 'r+')
    master = open("War/masterStats.txt", 'a')
    master.write(data.read())
    master.close()
    data.truncate(0)
    data.write('')
    data.close()
    aveDis["text"] = "0"
    ave()
    window.update()

def display() :
    try :
        p1Dis["text"] = "Card: " + pl1[0][1] + "\nCards Left: " + str(len(pl1)) + '\nRound Wins: ' + str(p1Cnt)
        rndDis['text'] = "Current\nRound\n" + str(cnt)
        p2Dis["text"] = "Card: " + pl2[0][1] + "\nCards Left: " + str(len(pl2)) + '\nRound Wins: ' + str(p2Cnt)
        time.sleep(.005)
    except :
        None
    if endBut["state"] == "active" :
        exit()
    if cnt % 10 :
        ave()
    window.update()

def overWar(plr) : # Which player has not enough cards
    if plr == 1 : # If player 1 has not enough cards
        num = len(pl1) - 1 # Sets num to the position of the last card
        print(num, "num 1") # Prints num
        return num # Returns num
    elif plr == 2 : # If player 2 has not enough cards
        num = len(pl2) - 1 # Sets num to the position of the last card
        print(num, "num 2") # Prints num
        return num # Returns num
    else :
        print('bruh how') # Should be unreachable
        exit() # Kills to make sure the user knows something big went wrong
  
def war(num, warCnt) :
    num += 4 # The number of cards after 0 to do the war at
    numM = num
    trig = None
    try :
        if pl1[numM] == 'Sup' : # Checks if there is a card at position numM for pl1
            None
    except : # ran if pl1 ran out of cards
        numM = overWar(1) # Gets the last card position for player 1
        trig = True # Sets trig to player 1
    try :
        if pl2[numM] == 'Sup' :# Checks if there is a card at position numM for pl2
            None
    except : # Runs if pl2 ran out of cards
        numM = overWar(2) # Gets the last card position for player 2
        trig = False # Sets trig to player 2
    if pl1[numM][0] > pl2[numM][0] :   # Checks if pl1 at numM if greater than pl2 at numM
        for i in range(numM) :   # Repeats for each card until numM
            pl1.append(pl2[0]) # Adds player 2's losing card to the end of player 1's deck
            pl2.remove(pl2[0]) # Removes player 2's first card
            pl1.append(pl1[0]) # Adds player 1's first card to the end of player 1's deck
            pl1.remove(pl1[0]) # Removes player 1's first card
    elif pl1[numM][0] < pl2[numM][0] : # Checks if pl1 at numM if greater than pl2 at numM
        for i in range(numM) :   # Repeats for each card until numM
            pl2.append(pl1[0]) # Adds player 1's losing card to the end of player 2's deck
            pl1.remove(pl1[0]) # Removes player 1's first card
            pl2.append(pl2[0]) # Adds player 2's first card to the end of player 2's deck
            pl2.remove(pl2[0]) # Removes player 2's first card
    elif pl1[numM][0] == pl2[numM][0] :
        warCnt += 1
        print('war again', warCnt)
        if trig != None: # Something went wrong and the code is looping
            if trig : # Decides winner via trig
                print("Sorry player 1 but you ran out of cards") # Prints sorry p1
                pl1.clear() # Enables win for player 2
            else :
                print("Sorry player 2 but you ran out of cards") # Prints sorry p2
                pl2.clear() # Enables win for player 1
        else :
            war(num, warCnt)
    else :
        print("Bruh get out of me hidey hole") # Should be impossible to even trigger
        exit() # Kills game cause it failed really bad

def main() :
    game = True # Weather or not a player has won yet
    global cnt, p1Cnt, p2Cnt # Round count, Player 1 hand wins, Player 2 Hand wins, Number of wars that of occurred this round
    cnt = 0     # Must have to reset each round
    p1Cnt = 0   # Must have to reset each round
    p2Cnt = 0   # Must have to reset each round
    warCnt = 0  # Must have to reset each round
    while game : # Run until a player has won
        if game and pl1[0][0] > pl2[0][0]: # Checks to see if player 1 beats player 2
            pl1.append(pl2[0]) # Adds player 2's losing card to the end of player 1's deck
            pl2.remove(pl2[0]) # Removes player 2's first card
            pl1.append(pl1[0]) # Adds player 1's first card to the end of player 1's deck
            pl1.remove(pl1[0]) # Removes player 1's first card
            p1Cnt += 1         # Adds 1 to the player 1 hand win counter
        elif game and pl1[0][0] < pl2[0][0]: # Checks to see if player 2 beats player 1
            pl2.append(pl1[0]) # Adds player 1's losing card to the end of player 2's deck
            pl1.remove(pl1[0]) # Removes player 1's first card
            pl2.append(pl2[0]) # Adds player 2's first card to the end of player 2's deck
            pl2.remove(pl2[0]) # Removes player 2's first card
            p2Cnt += 1         # Adds 1 to the player 2 hand win counter
        elif game and pl1[0][0] == pl2[0][0]: # Checks to see if player 1 and player 2 have the same card
            war(0, warCnt) # Runs war, sends war: How many chained wars
        cnt += 1 # Adds one to the total round count
        try : # Used for pl1[0] cannot == 'None', it throws an out of bounds
            if pl1[0] == 'None' : # Checks to see if player 1 ran out of cards
                None
        except : # Runs if player 1 has no cards
            win(2) # Sends win player 2
            game = False # Ends game
        try : # Used for pl1[0] cannot == 'None', it throws an out of bounds
            if pl2[0] == 'None' : # Checks if player 2 has ran out of cards
                None
        except : # Runs if player 2 has no cards
            win(1) # Sends win player 1
            game = False # Ends game
        display() # Updates the display

global warCnt
tmp = ''
cnt = 0
warCnt = 0
ftSize = 20 # Label font size
window = tk.Tk() # Creates the window
window.tk_setPalette("teal") # Sets main background color to 'teal'
window.title("WAR") # Labels the window 'WAR'
window.rowconfigure([0,1,2,3,4], minsize = 150, weight = 1)  # Adds rows to the window and sets each to be 150 pixels tall
window.columnconfigure([0, 1, 2], minsize = 300, weight = 1) # Adds columns to the rows at a width of 300 pixels each
p1NDis = tk.Label(master = window, text = 'Player 1\n', font = ("TkDefaultFont", ftSize)) # The label for player 1
p1NDis.grid(row = 0, column = 0) # The labels position on the grid
lftDis = tk.Label(master = window, text = '', font = ("TkDefaultFont", ftSize)) # The label for the number of rounds left
lftDis.grid(row = 0, column = 1) # The labels position on the grid
p2NDis = tk.Label(master = window, text = 'Player 2\n', font = ("TkDefaultFont", ftSize)) # The label for player 2
p2NDis.grid(row = 0, column = 2) # The labels position on the grid
p1Dis = tk.Label(master = window, text = '', font = ("TkDefaultFont", ftSize)) # Default player 1 info
p1Dis.grid(row = 1, column = 0) # The labels position on the grid
rndDis = tk.Label(master = window, text = "Push Run to Begin", font = ("TkDefaultFont", ftSize)) # Default info text
rndDis.grid(row = 1, column = 1) # The labels position on the grid
p2Dis = tk.Label(master = window, text = '', font = ("TkDefaultFont", ftSize)) # Default player 2 info
p2Dis.grid(row = 1, column = 2) # The labels position on the grid
p1WDis = tk.Label(master = window, text = '', font = ("TkDefaultFont", ftSize)) # Total number of wins for player 1
p1WDis.grid(row = 2, column = 0) # The labels position on the grid
aveDis = tk.Label(master = window, text = '', font = ("TkDefaultFont", ftSize)) # Average game length in rounds
aveDis.grid(row = 2, column = 1) # The labels position on the grid
p2WDis = tk.Label(master = window, text = '', font = ("TkDefaultFont", ftSize)) # Total number of wins for player 2
p2WDis.grid(row = 2, column = 2) # The labels position on the grid
ftSize = 27 # Button font size
runBut = tk.Button(master = window, text = "Run", command = run1, font = ("TkDefaultFont", ftSize)) # Button to run once
runBut.grid(row = 3, column = 0, sticky = "nsew") # Position of the button on the grid
clrBut = tk.Button(master = window, text = "Clear Past", command = clearScn, font = ("TkDefaultFont", ftSize)) # Button to clear all past data
clrBut.grid(row = 3, column = 1, sticky = "nsew") # Position of the button on the grid
endBut = tk.Button(master = window, text = "End", command = exit, font = ("TkDefaultFont", ftSize)) # Button to end program at nearly anytime
endBut.grid(row = 3, column = 2, sticky = "nsew") # Position of the button on the grid
rn5But = tk.Button(master = window, text = "Run 5x", command = run5, font = ("TkDefaultFont", ftSize)) # Button to run 5 times
rn5But.grid(row = 4, column = 0, sticky = "nsew") # Position of the button on the grid
r10But = tk.Button(master = window, text = "Run 10x", command = run10, font = ("TkDefaultFont", ftSize)) # Button to run 10 times
r10But.grid(row = 4, column = 1, sticky = "nsew") # Position of the button on the grid
rXBut = tk.Button(master = window, text = "Run\n\nTimes", command = runX, font = ("TkDefaultFont", ftSize)) # Button to run X times
rXBut.grid(row = 4, column = 2, sticky = "nsew") # Position of the button on the grid
rXEnt = tk.Entry(master = window, font = ("TkDefaultFont", ftSize), justify = 'center', width = 0) # User input for running X times
rXEnt.grid(row = 4, column = 2) # Position of the text box
window.update() # Updates the displayed window
ave() # Used to display the past info before any new info is added
window.mainloop() # Used to let the program run forever