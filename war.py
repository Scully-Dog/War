import time, random
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image

# TO DO
# Do auto 1000 test

class Helpers: # A bunch of helper functions

    def randomColor() : # Returns random HEX color
        color = '#' # Starts the hex string
        for i in range(6) : # Repeats 6 times
            color += random.choice("1234567890ABCDEF") # Adds a random hex digit to the hex string
        print(color) # Prints color
        return color # Returns the HEX color
    
    def ave() : # Gets the average scores
        out = [0,0,0] # List of pl1 wins, average length, pl2 wins
        lis1 = [] # List of player wins
        lis2 = [] # List of round lengths
        data = open("stats.txt", 'r') # Opens past data in read mode
        stats = list(data) # Copies the data into a list
        data.close() # Closes past data file
        try : # For when there is no data
            for i in stats : # Repeats for each data entry
                lis1.append(i[:1]) # Adds the winner at i
                lis2.append(i[2:-1]) # Add round length at i
            for i in lis1 : # Repeats for the total number of data entries
                if int(i) == 1 : # If the entry is player 1
                    out[0] += 1 # Adds to the player 1 total win count
                elif int(i) == 2 : # If player 2
                    out[2] += 1 # Adds to the player 2 total win count
            for i in lis2 : # Repeats for each entry in round length
                out[1] += int(i) # Adds entry length to total round length
            out[1] = float(out[1] / len(lis2)) # Averages the round lengths
            out[1] = float(format(out[1], ".3f")) # Makes the average have only 3 decimals no rounding
        except :
            pass
        out[0] = "Total Wins\n" + str(out[0]) # Creates player 1 info string
        out[1] = "Average\n" + str(out[1]) # Creates average length info string
        out[2] = "Total Wins\n" + str(out[2]) # Creates player 2 info string
        return out # Returns the ino
    
    def clearScn(self) : # Checks that you really want to delete the past
        global clWin # Lets clWin accessable from anywhere
        clWin = Window() # Creates a check clear window
        clWin.createSub() # Creates the window
        clWin.quest['text'] = 'Want to clear?' # Adds the question
        clWin.opt1['command'] = lambda : self.cl1() # Option 1, clear the past data
        clWin.opt2['command'] = lambda : clWin.windo.destroy() # Option 2, closes the window

    def cl1(): # Clear past data and destroy window
        data = Data()
        data.clear()
        clWin.windo.destroy() # Destroys window

class Data: # All the past info handles
    
    def __init__(self): # Opens past data files
        self.data = open('stats.txt', 'r+')
        self.master = open('masterStats.txt', 'a')

    def __delattr__(self): # The close function
        self.data.close() # Closes the data file
        self.master.close() # Closes the master data file

    def addData(self, num):
        if game.cnt != 0:
            txt = str(num) + " " + str(game.cnt) + "\n" # Formats this rounds data
            self.data.write(txt) # Adds this rounds data to stats.txt

    def clear(self):
        self.master.write(self.data.read()) # Adds all of current data to master data
        self.data.truncate(0) # Clears all lines up to the first
        self.data.write('') # Writes blank space to the first line in data
        window.aveDis["text"] = "0" # Changes average displayed to 0
        self.close()

    def close(self): # Closes all open data files
        self.__delattr__() # Runs close function

class Timer: # A timer tool, Pause function is untested

    def __init__(self): # Creates the timer
        self.startTime = None # Creates a start time variable
        self.pauseTime = 0 # Creates a pause length variable

    def start(self): # Starts a new timer

        if self.startTime is not None: # Checks if timer is already running
            print("Timer is already running. Use .stop() to stop it") # Prints error
        else:
            self.startTime = time.perf_counter() # Records the time when it is called

    def getTime(self) : # Returns timer length
        if self.startTime is None: # Checks to see if a timer was started
            print("Timer is not running. Use .start() to start it") # Prints error
        else: # If timer is running
            elapTime = time.perf_counter() - self.startTime # Takes current time minus start time
            if elapTime <= 0.0005 : # Rounds cause y not
                return 0 # Returns pretty number
            return elapTime # Returns the time elapsed

    def pause(self): # Sets the pause time to now plus previous paused time length
        self.pauseTime = time.perf_counter() + self.pauseTime # Should set pauseTime to now + past pause length

    def play(self): # Adds (pause time - time now) to startTime
        self.pauseTime = time.perf_counter() - self.startTime + self.pauseTime

    def stop(self): # Stops timer and returns elapTime

        if self.startTime is None: # If the timer hasn't stated yet
            print("Timer is not running. Use .start() to start it") # Prints error
        else:
            elapTime = time.perf_counter() - self.startTime - self.pauseTime # Calculates the elapTime
            self.startTime = None # Stops the timer
            print(f"Elapsed time: {elapTime:0.4f} seconds") # Prints elapTime to 4 decimals no rounding
            return f"{elapTime:0.4f}" # Returns elapTime to 4 decimals no rounding

class Cards: # All card checks, movement, and creation
    
    def __init__(self): # Creates the base deck and image locations
        # Your standard deck of 52 cards
        self.deck = [['1','2S'],['2','3S'],['3','4S'],['4','5S'],['5','6S'],['6','7S'],['7','8S'],['8','9S'],['9','10S'],['10','JS'],['11','QS'],['12','KS'],['13','AS'],['1','2C'],['2','3C'],['3','4C'],['4','5C'],['5','6C'],['6','7C'],['7','8C'],['8','9C'],['9','10C'],['10','JC'],['11','QC'],['12','KC'],['13','AC'],['1','2H'],['2','3H'],['3','4H'],['4','5H'],['5','6H'],['6','7H'],['7','8H'],['8','9H'],['9','10H'],['10','JH'],['11','QH'],['12','KH'],['13','AH'],['1','2D'],['2','3D'],['3','4D'],['4','5D'],['5','6D'],['6','7D'],['7','8D'],['8','9D'],['9','10D'],['10','JD'],['11','QD'],['12','KD'],['13','AD']]
        # Card Names
        self.cardNames = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD']
        # Image locations for each card
        self.img = ['images/2S.png','images/3S.png','images/4S.png','images/5S.png','images/6S.png','images/7S.png','images/8S.png','images/9S.png','images/10S.png','images/JS.png','images/QS.png','images/KS.png','images/AS.png','images/2C.png','images/3C.png','images/4C.png','images/5C.png','images/6C.png','images/7C.png','images/8C.png','images/9C.png','images/10C.png','images/JC.png','images/QC.png','images/KC.png','images/AC.png','images/2H.png','images/3H.png','images/4H.png','images/5H.png','images/6H.png','images/7H.png','images/8H.png','images/9H.png','images/10H.png','images/JH.png','images/QH.png','images/KH.png','images/AH.png','images/2D.png','images/3D.png','images/4D.png','images/5D.png','images/6D.png','images/7D.png','images/8D.png','images/9D.png','images/10D.png','images/JD.png','images/QD.png','images/KD.png','images/AD.png']

        self.p1 = [] # Base player 1 hand
        self.p2 = [] # Base player 2 hand

    def deal(self): # Shuffles and deals this rounds cards
        random.shuffle(self.deck) # Shuffles the base deck
        lent = len(self.deck) // 2 # Gets deck midpoint
        self.p1 = self.deck[lent:] # Sets player 1's hand to the first half of the deck
        self.p2 = self.deck[:lent] # Sets player 2's hand to the second half of the deck
    
    def checkHand(self, num=0): # Returns this rounds process
        num = int(num) # Current war position
        try:
            if self.p1[num][0] > self.p2[num][0]: # If player 1 > player 2
                return 1 # Returns p1
            elif self.p1[num][0] < self.p2[num][0]: # If player 2 > player 1
                return 2 # Returns p2
            elif self.p1[num][0] == self.p2[num][0]: # If player 1 = player 2
                return 0 # Returns war
        except: # Means player 1 or 2 has no cards
            try: # Checks if player 1 ran out of cards
                if self.p1 == []:
                    None
            except: # Player 2 wins
                game.cnt = 0 # Resets round length
                game.game = False # Stops this round
                return 4 # Returns player 2 win
            try: # Checks if player 2 ran out of cards
                if self.p2 == []:
                    None
            except: # Player 1 wins
                game.cnt = 0 # Resets round length
                game.game = False # Stops this round
                return 3 # Returns player 1 win

    def changeCard(self, num): # Moves cards from front to back of each hand
        try:
            if num == 1: # If player 1 win the round
                self.p1.append(self.p1[0]) # Adds player 2's losing card to the end of player 1's deck
                self.p1.append(self.p2[0]) # Adds player 1's first card to the end of player 1's deck
                self.p1.remove(self.p1[0]) # Removes player 1's first card
                self.p2.remove(self.p2[0]) # Removes player 2's first card
            elif num == 2: # If player 2 win the round
                self.p2.append(self.p2[0]) # Adds player 1's losing card to the end of player 2's deck
                self.p2.append(self.p1[0]) # Adds player 2's first card to the end of player 2's deck
                self.p2.remove(self.p2[0]) # Removes player 2's first card
                self.p1.remove(self.p1[0]) # Removes player 1's first card
            else :
                print('Error: Change Hand') # Prints an error and where it occurred
        except:
            None # Game is over and somehow this was still called

class Game: # The gameplay it self

    def __init__(self): # Inits the game and the game variables

        self.round = 0  # The Number of rounds left
        self.game = True # Weather or not to run the next round
        self.warLast = None # Weather p1 or p2 has not enough cards in a war
        self.warCnt = 0 # Number of chained wars
        self.cnt = 0 # Number of hands this round
        self.pl1 = 0 # Number of player 1 wins
        self.pl2 = 0 # Number of player 2 wins

    def setRnd(self, num): # Starts the auto runs for num rounds

        self.round = num # Total rounds
        self.run() # Starts auto code

    def war(self, num) : # Runs when p1 and p2 have the same card, num is the last war pos, used for multiple wars
        num += 4 # The number of cards to move after the first card
        try :
            if deck.p1[num] == 'Sup' : # Checks if there is a card at position num for player 1
                pass
        except : # Ran if player 1 ran out of cards
            num = self.overWar(1) # Gets the last card position for player 1
            game.warLast = True # Makes warLast to player 1
        try :
            if deck.p2[num] == 'Sup' : # Checks if there is a card at position num for player 2
                pass
        except : # Ran if player 2 ran out of cards
            num = self.overWar(2) # Gets the last card position for player 2
            game.warLast = False # Makes warlast to player 2
        val = deck.checkHand(num) 
        if val == 0: # Double war time
            if self.warLast != None: # If the last card is a war the win is given to the player who has more cards
                if self.warLast : # Decides winner via trig
                    print("Sorry player 1 but you ran out of cards") # Prints sorry p1
                    deck.p1 = [] # Enables win for player 2
                else :
                    print("Sorry player 2 but you ran out of cards") # Prints sorry p2
                    deck.p2 = [] # Enables win for player 1
            elif self.warCnt <= 5: # Double war up to 5 times
                self.warCnt += 1 # Adds 1 to current war count
                self.war(num) # MOAR WAR
            else: # Magic beans
                pass
        elif val == 1 or val == 2: # Determines if p1 or p2 wins this war
            for i in range(num): # Gives all cards to winner
                deck.changeCard(val)
            game.addWin(val) # Adds to winners win count
        elif val == 3 or val == 4: # Checks if game is over
            self.win(val) # Display and logging
            self.game = False # Prevents more rounds
        self.update() # Updates GUI
        self.warCnt = 0 # Resets for future wars

    def overWar(self, num): # For double or more wars
        if num == 1 : # If player 1 has not enough cards
            num = len(deck.p1) - 1 # Sets num to the position of the last card
            return num # Returns num
        elif num == 2 : # If player 2 has not enough cards
            num = len(deck.p2) - 1 # Sets num to the position of the last card
            return num # Returns num

    def run(self): # Automatic code
        while self.round > 0: # While there are still more rounds left
            self.reset() # Resets variables
            deck.deal() # Shuffles and deals cards to p1 and p2
            while self.game: # While game
                num = deck.checkHand() # Returns round process
                if num == 0: # If war
                    self.war(0) # Runs war with a starting index of 0
                elif num == 1 or num == 2: # If player 1 or 2 won this round
                    deck.changeCard(num) # Adds losers card to winner's cards
                    self.addWin(num) # Adds win to winner win count
                elif num == 3 or num == 4: # If player 1 or 2 won the game
                    self.win(num - 3) # Prints and logs the winner
                elif num == None: # Just some catch code
                    self.game = False # Ends this round
                self.update() # Updates GUI
                self.cnt += 1 # Adds 1 to current round count
                if self.cnt % 10 == 0: # Runs once every 10 rounds
                    window.updateCard() # Updates displayed cards
            self.round = self.round - 1 # Lowers total round cnt by 1
            self.update() # Updates GUI

    def addWin(self, num): # Adds win to winner
        if num == 1: # If player 1
            self.pl1 += 1 # Add 1 to player 1 win cnt
        elif num == 2: # If player 2
            self.pl2 += 1 # Add 1 to player 2 win cnt

    def next(self, num = 5): # Manual stepping code
        for i in range(int(num)): # Runs num times
            if self.game: # If the game is not over
                print(game.cnt) # Prints the current round cnt
                num = deck.checkHand() # Returns current round process
                if num == 0: # If war
                    self.war(0) # Runs war with a starting index of 0
                elif num == 1 or num == 2: # If player 1 or 2 won this round
                    deck.changeCard(num) # Adds losers card to winner's cards
                    self.addWin(num) # Adds win to winner win count
                elif num == 3 or num == 4: # If player 1 or 2 won the game
                    self.win(num - 3) # Prints and logs the winner
                    break # Breaks out of loop to prevent multiple win statements and excess logging
                elif num == None: # Catch code
                    self.game = False # Ends game
                    break # Breaks from loop
                self.update() # Updates GUI
                window.updateCard() # Updates card GUI
                self.cnt += 1 # Adds to current round cnt

    def untilWar(self): # Steps until a war
        while deck.checkHand() != 0: # While there is no war
            self.next(1) # Steps once

    def xCmd(self): # Runs step code entered number of times
        num = window.rXEnt.get() # Gets number entered
        if num == int : # Checks to see if a whole number
            self.next(num) # Steps num times
        elif str(num).lower() == 'until war': # If entered == until war
            self.untilWar() # Repeats until there is a war

    def win(self, num): # Prints and logs win
        print('congrats player ', str(num)) # Prints win statement
        data = Data() # Opens past data
        data.addData(num) # Adds this rounds data
        data.close() # Closes past data

    def update(self): # Updates GUI
        window.updateAve() # Updates averages GUI section
        if window.endBut["state"] == "active" : # If end button is pushed
            exit() # Ends program
        try: # Tries to output current round info
            window.rndDis['text'] = "Current Round: " + str(game.cnt) # The current round number
            window.p1Dis['text'] = "Card: " + deck.p1[0][1] + "\nCards Left: " + str(len(deck.p1)) + '\nRound Wins: ' + str(self.pl1) # Player 1 info
            window.lftDis['text'] = 'Rounds Left: ' + str(game.round) # Rounds left to run
            window.p2Dis["text"] = "Card: " + deck.p2[0][1] + "\nCards Left: " + str(len(deck.p2)) + '\nRound Wins: ' + str(self.pl2) # Player 2 info
        except:
            pass

    def reset(self): # Resets variable
        self.cnt = 0 # Sets current round count to 0
        deck.p1 = [] # Clears player 1's hand
        deck.p2 = [] # Clears player 2's hand
        self.pl1 = 0 # Sets player 1 wins to 0
        self.pl2 = 0 # Sets player 2 wins to 0
        self.game = True # Lets the game continue
        window.windo.tk_setPalette(Helpers.randomColor()) # Randomizes the background color

    def finish(self): # Runs until the hand is over
        while game.game: # Runs if game is true
            self.next(1) # Steps once

class Window: # The GUIs

    def __init__(self): # Makes the 2 main windows
        self.windo = tk.Tk() # Main UI
        self.cards = tk.Tk() # Card display

    def createMain(self): # The main GUI
        ftSize = 20 # Label font size
        self.windo.tk_setPalette(Helpers.randomColor()) # Sets main background color to 'teal'
        self.windo.title("WAR") # Labels the window 'WAR'
        self.windo.rowconfigure([0,1,2,3,4], minsize = 150, weight = 1)  # Adds rows to the window and sets each to be 150 pixels tall
        self.windo.columnconfigure([0, 1, 2], minsize = 300, weight = 1) # Adds columns to the rows at a width of 300 pixels each
        self.windo.geometry('+200+100') # Windo position on screen
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
        ftSize = 27 # Increases font size
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
        self.update() # Updates GUI

    def createSub(self): # A secondary selector window
        ftSize = 20 # Font size
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

    def createCards(self): # The cards display
        self.cards.rowconfigure([0,1], weight = 1) # Number of rows
        self.cards.columnconfigure([0, 1], weight = 1) # Number of columns
        self.cards.geometry('200x100+1200+100') # Size and location of card window
        self.cards.tk_setPalette(Helpers.randomColor()) # Randomizes the background color of the new window
        loc = 'images/green_back.png' # Default card displayed
        img = PhotoImage(master = self.cards, file = loc) # Makes the image viewable for tkniter
        self.cards.pl1 = tk.Label(master = self.cards, image = img) # Sets left image to given image
        self.cards.pl2 = tk.Label(master = self.cards, image = img) # Sets right image to given image
        self.cards.pl1.grid(column = 0, row = 1, sticky = 'sw') # Positions the left image
        self.cards.pl2.grid(column = 1, row = 1, sticky = 'sw') # Positions the right image
        self.cards.update() # Updates the card display
        self.updateCard() # Updates card display to show current cards

    def updateAve(self): # Updates the averages GUI section
        num = Helpers.ave() # Gets the averages
        self.p1WDis["text"] = num[0] # Sets the player 1 averages
        self.aveDis["text"] = num[1] # Sets the total averages
        self.p2WDis["text"] = num[2] # Sets the player 2 averages
        self.update() # Updates the display

    def updateCard(self): # Updates card visual
        try:
            self.img1loc = 'images/green_back.png' # Sets default left image
            self.img2loc = 'images/blue_back.png' # Sets default right image
            for i in range(len(deck.cardNames)): # Used to determine the image corresponding with the current cards
                if deck.cardNames[i] == deck.p1[0][1]: # Checks player 1
                    self.img1loc = deck.img[i] # Sets player 1
                if deck.cardNames[i] == deck.p2[0][1]: # Checks player 2
                    self.img2loc = deck.img[i] # Sets player 2
            self.geo = self.cards.geometry() # Gets card display dimension
            self.geo = self.geo.split('+', 4) # Splits numbers at the + symbol
            self.geo = self.geo[0].split('x') # Splits at the x
            self.x = int(int(self.geo[0]) / 2) # Gets half of the width
            self.y = int(self.geo[1]) # Gets the height
            img = Image.open(self.img1loc) # Opens left image
            img = img.resize((self.x,self.y)) # Resizes image to new height and width
            img.save('images/img1tmp.png') # Saves image to the left img location
            img = Image.open(self.img2loc) # Opens right image
            img = img.resize((self.x,self.y)) # Resizes right image to new height and width
            img.save('images/img2tmp.png') # Saves left image to the right img location
            self.img1loc = 'images/img1tmp.png' # Sets the left image location to the temp location
            self.img2loc = 'images/img2tmp.png' # Sets the right image location to the temp location
            self.img1 = PhotoImage(master = self.cards, file = self.img1loc) # Makes the image viewable for tkniter
            self.img2 = PhotoImage(master = self.cards, file = self.img2loc) # Makes the image viewable for tkniter
            self.cards.pl1['image'] = self.img1 # Sets left image to img1
            self.cards.pl2['image'] = self.img2 # Sets right image to img2
            self.update() # Updates GUI windows
        except:
            None

    def update(self): # Used as a shortcut
        self.windo.update() # Updates the windo window
        self.cards.update() # Updates the cards window

def automatic(): # Auto Mode
    global window, game, deck # The main game items
    mode.destroy() # Gets rid of the game select screen
    window = Window() # Creates the main GUI
    game = Game() # Starts the gameplay
    deck = Cards() # Creates a deck a cards
    window.createMain() # Creates the main window
    window.updateAve() # Updates the ave info
    window.createCards() # Creates the card window
    window.runBut['text'] = 'Run 1x' # Sets upper left button
    window.rn5But['text'] = 'Run 5x' # Sets lower left button
    window.r10But['text'] = 'Run 10x' # Sets lower center button
    window.rXBut['text'] = 'Run\n\nTimes' # Sets lower right button
    window.runBut['command'] = lambda : game.setRnd(1) # Gives the button its command
    window.rn5But['command'] = lambda : game.setRnd(5) # Gives the button its command
    window.r10But['command'] = lambda : game.setRnd(10) # Gives the button its command
    window.rXBut['command'] = lambda : game.setRnd(int(window.rXEnt.get())) # Gives the button its command
    window.update() # Updates the windows
    window.windo.mainloop() # Runs forever while still excepting and following the button commands
            
def manual(): # Manual Mode, step by step
    global window, game, deck # The main game items
    mode.destroy() # Gets rid of the game select screen
    window = Window() # Creates the main GUI
    game = Game() # Starts the gameplay
    deck = Cards() # Creates a deck a cards
    window.createMain() # Creates the main window
    window.updateAve() # Updates the ave info
    window.createCards() # Creates the card window
    window.runBut['text'] = 'Step 1x' # Sets upper left button
    window.rn5But['text'] = 'Step 5x' # Sets lower left button
    window.r10But['text'] = 'Step\n\nTimes' # Sets lower center button
    window.rXBut['text'] = 'Finish' # Sets lower right button
    window.rXEnt.grid(column = 1) # Changes the position of the entry box from default
    window.runBut['command'] = lambda : game.next(1) # Gives the button its command
    window.rn5But['command'] = lambda : game.next(5) # Gives the button its command
    window.r10But['command'] = lambda : game.xCmd # Gives the button its command
    window.rXBut['command'] = game.finish # Gives the button its command
    deck.deal() # Deals the cards
    window.update() # Updates the windows
    window.windo.mainloop() # Runs forever while still excepting and following the button commands

# Code starts here

global mode # So i can destroy it later
mode = tk.Tk() # Makes the mode selection window
mode.title('Game Mode') # Sets the window name 
mode.tk_setPalette(Helpers.randomColor()) # Sets main background color to a random HEX color
mode.rowconfigure([0,1], minsize = 75, weight = 1) # Adds rows at a min height of 75
mode.columnconfigure([0,1], minsize = 150, weight = 1) # Adds columns at a min width of 150
modeDis = tk.Label(master = mode, text = 'Which version?', font = ('TkDefaultFont', 20)) # Label asking which version
modeDis.grid(row = 0, column = 0, columnspan = 2, sticky = 'nsew') # Label location
mode1But = tk.Button(master = mode, text = 'Auto', command = automatic, font = ('TkDefaultFont', 20)) # Automatic mode
mode1But.grid(row = 1, column = 0, sticky = "nsew") # Auto button position
mode2But = tk.Button(master = mode, text = "Step", command = manual, font = ('TkDefaultFont', 20)) # Manual mode
mode2But.grid(row = 1, column = 1, sticky = 'nsew') # Manual button position
mode.update() # Updates the mode window
mode.mainloop() # Runs forever