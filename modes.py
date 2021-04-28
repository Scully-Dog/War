from playsound import playsound
from datetime import datetime
from timer import Timer
import random, time
import tkinter as tk

class modes :
    def mode1() :
        print('nope')

    def mode2() :
        print('FUCk')
        mode.destroy()

    def randomColor() :
        color = '#'
        for i in range(6) :
            color = color + random.choice("1234567890ABCDEF")
        print(color)
        return color

    global mode
    mode = tk.Tk()
    mode.title('Game Mode')
    mode.tk_setPalette(randomColor())
    mode.rowconfigure([0,1], minsize = 75, weight = 1)
    mode.columnconfigure([0,1], minsize = 150, weight = 1)
    modeDis = tk.Label(master = mode, text = 'Which version?', font = ('TkDefaultFont', 20))
    modeDis.grid(row = 0, column = 0, columnspan = 2, sticky = 'nsew')
    mode1But = tk.Button(master = mode, text = 'Auto', command = mode1, font = ('TkDefaultFont', 20))
    mode1But.grid(row = 1, column = 0, sticky = "nsew")
    mode2But = tk.Button(master = mode, text = "Step", command = mode2, font = ('TkDefaultFont', 20))
    mode2But.grid(row = 1, column = 1, sticky = 'nsew')
    mode.update()
    mode.mainloop()