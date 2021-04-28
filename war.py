import time, random
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image

# COMPLETELY remake war here for one file and multimode option
#
# TO DO
# Fix clear fast
# Do auto 1000 test
# Move war and overWar into game from card

class Helpers:

    def randomColor() :
        color = '#'
        for i in range(6) :
            color += random.choice("1234567890ABCDEF")
        print(color)
        return color
    
    def ave() : # Gets the average scores
        out = [0,0,0]
        lis1 = []
        lis2 = []
        data = open("stats.txt", 'r')
        stats = list(data)
        data.close()
        try :
            for i in stats :
                lis1.append(i[:1])
                lis2.append(i[2:-1])
            for i in lis1 :
                if int(i) == 1 :
                    out[0] += 1
                elif int(i) == 2 :
                    out[2] += 1
            for i in lis2 :
                out[1] += int(i)
            out[1] = float(out[1] / len(lis2))
            out[1] = float(format(out[1], ".3f"))
        except :
            pass
        out[0] = "Total Wins\n" + str(out[0])
        out[1] = "Average\n" + str(out[1])
        out[2] = "Total Wins\n" + str(out[2])
        return out
        # PL1 wins, ave Dub, PL2 wins
    
    def clearScn() : # Checks that you really want to delete the past
        global clWin
        clWin = Window()
        clWin.createSub()
        clWin.quest['text'] = 'Want to clear?'
        clWin.opt1['command'] = lambda : Helpers.cl1()
        clWin.opt2['command'] = lambda : clWin.windo.destroy()

    def cl1():
        Helpers.clearScn()
        clWin.windo.destroy()

    def clrScreen() : # Clears the past data while adding it to a master data file
        data = open("stats.txt", 'r+')
        master = open("masterStats.txt", 'a')
        master.write(data.read())
        master.close()
        data.truncate(0)
        data.write('')
        data.close()
        window.aveDis["text"] = "0"

class Data:
    
    def __init__(self):
        self.dataa = open('stats.txt', 'a')
        self.datar = open('stats.txt', 'r')
        self.master = open('masterStats.txt', 'a')

    def __delattr__(self):
        self.dataa.close()
        self.datar.close()
        self.master.close()

    def addData(self, num):
        txt = str(num) + " " + str(game.cnt) + "\n" # Formats this rounds data
        self.dataa.write(txt) # Adds this rounds data to stats.txt

class TimerError(Exception): # Needed for Timer class
    """A custom exception used to report errors in use of Timer class"""

class Timer: # A simple timer tool
    def __init__(self):
        self.startTime = None
        self.pauseTime = 0

    def start(self):
        """Start a new timer"""
        if self.startTime is not None:
            raise TimerError(f"Timer is already running. Use .stop() to stop it")

        self.startTime = time.perf_counter()

    def getTime(self) :
        if self.startTime is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        print(self.startTime)
        elapTime = time.perf_counter() - self.startTime
        if elapTime <= 0.0005 : # Rounds cause y not
            return 0
        return elapTime

    def pause(self):
        self.pauseTime = time.perf_counter() + self.pauseTime

    def play(self):
        self.pauseTime = time.perf_counter() - self.startTime - self.pauseTime

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self.startTime is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapTime = time.perf_counter() - self.startTime - self.pauseTime
        self.startTime = None
        print(f"Elapsed time: {elapTime:0.4f} seconds")
        return f"{elapTime:0.4f}"

class Cards:
    
    def __init__(self) -> None:
        self.deck = [['1','2S'],['2','3S'],['3','4S'],['4','5S'],['5','6S'],['6','7S'],['7','8S'],['8','9S'],['9','10S'],['10','JS'],['11','QS'],['12','KS'],['13','AS'],['1','2C'],['2','3C'],['3','4C'],['4','5C'],['5','6C'],['6','7C'],['7','8C'],['8','9C'],['9','10C'],['10','JC'],['11','QC'],['12','KC'],['13','AC'],['1','2H'],['2','3H'],['3','4H'],['4','5H'],['5','6H'],['6','7H'],['7','8H'],['8','9H'],['9','10H'],['10','JH'],['11','QH'],['12','KH'],['13','AH'],['1','2D'],['2','3D'],['3','4D'],['4','5D'],['5','6D'],['6','7D'],['7','8D'],['8','9D'],['9','10D'],['10','JD'],['11','QD'],['12','KD'],['13','AD']]
        self.cardNames = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD']
        self.img = ['images/2S.png','images/3S.png','images/4S.png','images/5S.png','images/6S.png','images/7S.png','images/8S.png','images/9S.png','images/10S.png','images/JS.png','images/QS.png','images/KS.png','images/AS.png','images/2C.png','images/3C.png','images/4C.png','images/5C.png','images/6C.png','images/7C.png','images/8C.png','images/9C.png','images/10C.png','images/JC.png','images/QC.png','images/KC.png','images/AC.png','images/2H.png','images/3H.png','images/4H.png','images/5H.png','images/6H.png','images/7H.png','images/8H.png','images/9H.png','images/10H.png','images/JH.png','images/QH.png','images/KH.png','images/AH.png','images/2D.png','images/3D.png','images/4D.png','images/5D.png','images/6D.png','images/7D.png','images/8D.png','images/9D.png','images/10D.png','images/JD.png','images/QD.png','images/KD.png','images/AD.png']
        self.p1 = []
        self.p2 = []
        self.warCnt = 0

    def deal(self):
        random.shuffle(self.deck)
        lent = len(self.deck) // 2
        self.p1 = self.deck[lent:]
        self.p2 = self.deck[:lent]
    
    def checkHand(self, num=0):
        num = int(num)
        time.sleep(0.005)
        try:
            if self.p1[num][0] > self.p2[num][0]:
                return 1
            elif self.p1[num][0] < self.p2[num][0]:
                return 2
            elif self.p1[num][0] == self.p2[num][0]:
                return 0
        except:
            try:
                if self.p1 == []:
                    self.win(2)
                    game.cnt = 0
                    game.game = False
                    return 5
            except:
                self.win(2)
                game.cnt = 0
                game.game = False
                return 5
            try:
                if self.p2 == []:
                    self.win(1)
                    game.cnt = 0
                    game.game = False
                    return 4
            except:
                self.win(1)
                game.cnt = 0
                game.game = False
                return 4

    def changeCard(self, num):
        try:
            if num == 1:
                self.p1.append(self.p1[0]) # Adds player 2's losing card to the end of player 1's deck
                self.p1.append(self.p2[0]) # Adds player 1's first card to the end of player 1's deck
                self.p1.remove(self.p1[0]) # Removes player 1's first card
                self.p2.remove(self.p2[0]) # Removes player 2's first card
            elif num == 2:
                self.p2.append(self.p2[0]) # Adds player 1's losing card to the end of player 2's deck
                self.p2.append(self.p1[0]) # Adds player 2's first card to the end of player 2's deck
                self.p2.remove(self.p2[0]) # Removes player 2's first card
                self.p1.remove(self.p1[0]) # Removes player 1's first card
            else :
                print('Error: Change Hand')
        except:
            None # Game is over need this for reasons

    def war(self, num) :
        num += 4
        print('war')
        print(num)
        try :
            if self.p1[num] == 'Sup' : # Checks if there is a card at position num for player 1
                pass
        except : # Ran if player 1 ran out of cards
            num = self.overWar(1) # Gets the last card position for player 1
            game.war = True
        try :
            if self.p2[num] == 'Sup' : # Checks if there is a card at position num for player 2
                pass
        except : # Ran if player 2 ran out of cards
            num = self.overWar(2) # Gets the last card position for player 2
            game.war = False
        val = self.checkHand(num)
        print(val)
        print(str(self.warCnt) + 'fart')
        if val == 0:
            if game.war != None:
                if game.war : # Decides winner via trig
                    print("Sorry player 1 but you ran out of cards") # Prints sorry p1
                    print(self.p1)
                    print(self.p2)
                    self.p1 = [] # Enables win for player 2
                else :
                    print("Sorry player 2 but you ran out of cards") # Prints sorry p2
                    print(self.p1)
                    print(self.p2)
                    self.p2 = [] # Enables win for player 1
            elif self.warCnt < 5:
                self.warCnt += 1
                self.war(num)
                self.warCnt = 0
            else:
                pass
        elif val == 1 or val == 2:
            for i in range(num):
                self.changeCard(val)
        elif val == 3 or val == 4:
            self.win(val)
            game.game = False
        self.update()
        self.warCnt = 0

    def overWar(self, num):
        if num == 1 : # If player 1 has not enough cards
            num = len(self.p1) - 1 # Sets num to the position of the last card
            return num # Returns num
        elif num == 2 : # If player 2 has not enough cards
            num = len(self.p2) - 1 # Sets num to the position of the last card
            return num # Returns num

    def win(self, num):
        print('congrats player ', str(num))
        data = Data()
        data.addData(num)

    def update(self):
        window.updateAve()
        if window.endBut["state"] == "active" :
            exit()
        try:
            window.rndDis['text'] = "Current Round: " + str(game.cnt)
            window.p1Dis['text'] = "Card: " + self.p1[0][1] + "\nCards Left: " + str(len(self.p1)) + '\nRound Wins: ' + str(game.pl1)
            window.lftDis['text'] = 'Rounds Left: ' + str(game.round)
            window.p2Dis["text"] = "Card: " + self.p2[0][1] + "\nCards Left: " + str(len(self.p2)) + '\nRound Wins: ' + str(game.pl2)
        except:
            pass

class Game:

    def __init__(self):
        self.round = 0
        self.game = True
        self.war = None
        self.cnt = 0
        self.pl1 = 0
        self.pl2 = 0

    def setRnd(self, num):
        self.round = num
        self.run()

    def reset(self):
        self.cnt = 0
        deck.p1 = []
        deck.p2 = []
        self.pl1 = 0
        self.pl2 = 0
        self.game = True
        window.windo.tk_setPalette(Helpers.randomColor())

    def run(self):
        while self.round > 0:
            self.reset()
            deck.deal()
            while self.game:
                num = deck.checkHand()
                if num == 0:
                    deck.war(0)
                elif num == 1 or num == 2:
                    deck.changeCard(num)
                elif num == 3 or num == 4:
                    self.game = False
                    deck.win(num - 3)
                elif num == None:
                    self.game = False
                deck.update()
                self.cnt += 1
                print(self.cnt)
                if self.cnt % 10 == 0:
                    window.updateCard()
            self.round = self.round - 1
            print("finished this round")
            deck.update()

    def next(self, num = 5):
        for i in range(int(num)):
            if self.game:
                print(game.cnt)
                num = deck.checkHand()
                if num == 0:
                    deck.war(0)
                elif num == 1 or num == 2:
                    deck.changeCard(num)
                elif num == 3 or num == 4:
                    self.game = False
                    deck.win(num - 3)
                    break
                elif num == None:
                    self.game = False
                    break
                deck.update()
                window.updateCard()
                game.cnt += 1

    def finish(self):
        while game.game:
            self.next(1)

class Window:

    def __init__(self) -> None:
        self.windo = tk.Tk()
        self.cards = tk.Tk()

    def createMain(self):
        ftSize = 20 # Label font size
        self.windo.tk_setPalette(Helpers.randomColor()) # Sets main background color to 'teal'
        self.windo.title("WAR") # Labels the window 'WAR'
        self.windo.rowconfigure([0,1,2,3,4], minsize = 150, weight = 1)  # Adds rows to the window and sets each to be 150 pixels tall
        self.windo.columnconfigure([0, 1, 2], minsize = 300, weight = 1) # Adds columns to the rows at a width of 300 pixels each
        self.windo.geometry('+200+100')
        self.p1NDis = tk.Label(master = self.windo, text = 'Player 1\n', font = ("TkDefaultFont", ftSize)) # The label for player 1
        self.p1NDis.grid(row = 0, column = 0) # The labels position on the grid
        self.lftDis = tk.Label(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # The label for the number of rounds left
        self.lftDis.grid(row = 0, column = 1) # The labels position on the grid
        self.p2NDis = tk.Label(master = self.windo, text = 'Player 2\n', font = ("TkDefaultFont", ftSize)) # The label for player 2
        self.p2NDis.grid(row = 0, column = 2) # The labels position on the grid
        self.p1Dis = tk.Label(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Default player 1 info
        self.p1Dis.grid(row = 1, column = 0) # The labels position on the grid
        self.rndDis = tk.Label(master = self.windo, text = "Push Run to Begin", font = ("TkDefaultFont", ftSize)) # Default info text
        self.rndDis.grid(row = 1, column = 1) # The labels position on the grid
        self.p2Dis = tk.Label(master =self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Default player 2 info
        self.p2Dis.grid(row = 1, column = 2) # The labels position on the grid
        self.p1WDis = tk.Label(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Total number of wins for player 1
        self.p1WDis.grid(row = 2, column = 0) # The labels position on the grid
        self.aveDis = tk.Label(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Average game length in rounds
        self.aveDis.grid(row = 2, column = 1) # The labels position on the grid
        self.p2WDis = tk.Label(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Total number of wins for player 2
        self.p2WDis.grid(row = 2, column = 2) # The labels position on the grid
        ftSize = 27 # Label font size
        self.runBut = tk.Button(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Button to ___ once
        self.runBut.grid(row = 3, column = 0, sticky = "nsew") # Position of the button on the grid
        self.clrBut = tk.Button(master = self.windo, text = "Clear Past", command = Helpers.clearScn, font = ("TkDefaultFont", ftSize)) # Button to clear all past data
        self.clrBut.grid(row = 3, column = 1, sticky = "nsew") # Position of the button on the grid
        self.endBut = tk.Button(master = self.windo, text = "End", command = exit, font = ("TkDefaultFont", ftSize)) # Button to end program at nearly anytime
        self.endBut.grid(row = 3, column = 2, sticky = "nsew") # Position of the button on the grid
        self.rn5But = tk.Button(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Button to ___ 5 times
        self.rn5But.grid(row = 4, column = 0, sticky = "nsew") # Position of the button on the grid
        self.r10But = tk.Button(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Button to ___ 10 times
        self.r10But.grid(row = 4, column = 1, sticky = "nsew") # Position of the button on the grid
        self.rXBut = tk.Button(master = self.windo, text = '', font = ("TkDefaultFont", ftSize)) # Button to ___ X times
        self.rXBut.grid(row = 4, column = 2, sticky = "nsew") # Position of the button on the grid
        self.rXEnt = tk.Entry(master = self.windo, font = ("TkDefaultFont", ftSize), justify = 'center', width = 0) # User input for ____ing X times
        self.rXEnt.grid(row = 4, column = 2) # Position of the text box
        self.update() # Updates gui

    def createSub(self):
        ftSize = 20
        self.windo.tk_setPalette(Helpers.randomColor()) # Sets main background color to 'teal'
        self.windo.title("Are You Sure") # Labels the window 'Are You Sure'
        self.windo.resizable(width = False, height = False) # Disables resizing of window
        self.windo.rowconfigure([0,1], minsize = 50) # Adds rows at a min height of 50
        self.windo.columnconfigure([0,1], minsize = 50) # Adds columns at a min width of 50
        self.windo.geometry('+500+450') # Positions sure at 500x450
        self.quest = tk.Label(master = self.windo, text = 'Question', font = ("TkDefaultFont", ftSize)) # Label asking if you want to clear
        self.quest.grid(row = 0, columnspan = 2) # Positions label
        self.opt1 = tk.Button(master = self.windo, text = 'Yes', font = ("TkDefaultFont", ftSize)) # Creates yes button on sure window
        self.opt1.grid(row = 1, column = 0, sticky = 'nsew') # Positions option Yes
        self.opt2 = tk.Button(master = self.windo, text = 'No', font = ("TkDefaultFont", ftSize)) # Creates no button on sure window
        self.opt2.grid(row = 1, column = 1, sticky = 'nsew') # Positions option No
        self.update() # Updates sure

    def createCards(self):
        self.cards.rowconfigure([0,1], minsize = 150, weight = 1)
        self.cards.columnconfigure([0, 1], minsize = 300, weight = 1)
        self.cards.geometry('+200+100')
        img = PhotoImage(master = self.cards, file = 'images/green_back.png')
        self.cards.pl1 = tk.Label(master = self.cards, image = img)
        self.cards.pl2 = tk.Label(master = self.cards, image = img)
        self.cards.pl1.grid(column = 0, row = 1)
        self.cards.pl2.grid(column = 1, row = 1)
        self.cards.update()

    def updateAve(self):
        num = Helpers.ave()
        self.p1WDis["text"] = num[0]
        self.aveDis["text"] = num[1]
        self.p2WDis["text"] = num[2]
        self.update()

    def updateCard(self):
        try:
            self.img1loc = 'images/green_back.png'
            self.img2loc = 'images/blue_back.png'
            for i in range(len(deck.cardNames)):
                if deck.cardNames[i] == deck.p1[0][1]:
                    self.img1loc = deck.img[i]
                    print(self.img1loc)
                if deck.cardNames[i] == deck.p2[0][1]:
                    self.img2loc = deck.img[i]
                    print(self.img2loc)
            self.img1 = PhotoImage(master = self.cards, file = self.img1loc)
            self.img2 = PhotoImage(master = self.cards, file = self.img2loc)
            
            self.cards.pl1['image'] = self.img1
            self.cards.pl2['image'] = self.img2
        except:
            None

    def update(self):
        self.windo.update()

def automatic():
    global window, game, deck
    mode.destroy()
    window = Window()
    game = Game()
    deck = Cards()
    window.createMain()
    window.updateAve()
    window.createCards()
    window.runBut['text'] = 'Run 1x'
    window.rn5But['text'] = 'Run 5x'
    window.r10But['text'] = 'Run 10x'
    window.rXBut['text'] = 'Run\n\nTimes'
    window.runBut['command'] = lambda : game.setRnd(1)
    window.rn5But['command'] = lambda : game.setRnd(5)
    window.r10But['command'] = lambda : game.setRnd(10)
    window.rXBut['command'] = lambda : game.setRnd(int(window.rXEnt.get()))
    window.update()
    window.windo.mainloop()
            
def manual():
    global window, game, deck
    mode.destroy()
    window = Window()
    game = Game()
    deck = Cards()
    window.createMain()
    window.updateAve()
    window.createCards()
    window.runBut['text'] = 'Step 1x'
    window.rn5But['text'] = 'Step 5x'
    window.r10But['text'] = 'Step\n\nTimes'
    window.rXBut['text'] = 'Finish'
    window.rXEnt.grid(column = 1)
    window.runBut['command'] = lambda : game.next(1)
    window.rn5But['command'] = lambda : game.next(5)
    window.r10But['command'] = game.next
    window.rXBut['command'] = game.finish
    deck.deal()
    window.update()
    window.windo.mainloop()

global mode
mode = tk.Tk()
mode.title('Game Mode')
mode.tk_setPalette(Helpers.randomColor())
mode.rowconfigure([0,1], minsize = 75, weight = 1)
mode.columnconfigure([0,1], minsize = 150, weight = 1)
modeDis = tk.Label(master = mode, text = 'Which version?', font = ('TkDefaultFont', 20))
modeDis.grid(row = 0, column = 0, columnspan = 2, sticky = 'nsew')
mode1But = tk.Button(master = mode, text = 'Auto', command = automatic, font = ('TkDefaultFont', 20))
mode1But.grid(row = 1, column = 0, sticky = "nsew")
mode2But = tk.Button(master = mode, text = "Step", command = manual, font = ('TkDefaultFont', 20))
mode2But.grid(row = 1, column = 1, sticky = 'nsew')
mode.update()
mode.mainloop()