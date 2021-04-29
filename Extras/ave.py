import tkinter as tk

def ave() :
    window = tk.Tk()
    window.title("WAR")
    window.rowconfigure([0, 1], minsize = 150, weight = 1)
    window.columnconfigure([0, 1, 2], minsize = 150, weight = 1)
    lft = tk.Label(master = window, text = "Player 1 Wins")
    lft.grid(row = 0, column = 0, sticky="nw")
    cn = tk.Label(master = window, text = "Average Game\nLength")
    cn.grid(row = 0, column = 1, sticky="n")
    cnr = tk.Label(master=window, text = "tmp txt")
    cnr.grid(row = 1, column = 1, sticky="s")
    rht = tk.Label(master = window, text = "Player 2 Wins")
    rht.grid(row = 0, column = 2, sticky="ne")
    window.update()

    data = open("War/stats.txt", "r")
    lis = []
    liz = []
    ttl = 0
    p1 = 0
    p2 = 0
    for i in data :
        lis.append(i[:1])
        liz.append(i[2:-1])
    lis.remove(lis[0])
    for i in lis :
        if int(i) == 1 :
            p1 += 1
        elif int(i) == 2 :
            p2 += 1
    lb = tk.Label(master=window, text = p1)
    lb.grid(row = 1, column = 0, sticky="sw")
    rb = tk.Label(master=window, text = p2)
    rb.grid(row = 1, column = 2, sticky="se")
    if p2 <  p1 :
        p1 = p1 - p2
        print("\n\nPlayer 1 has more wins than Player 2 by ", p1)
    else :
        p2 = p2 - p1
        print("\n\nPlayer 2 has more wins than Player 1 by ", p2)
    liz.remove(liz[0])
    for i in liz :
        ttl += int(i)
    ttl = ttl / len(liz)
    ttl = float(format(ttl, ".3f"))
    print("\nAverage game length is" , ttl, " rounds\n\n")
    data.close()
    while True :
        window.mainloop()
       # window.update()

def clear() :
    txt = [""]
    data = open("War/stats.txt", 'r+')
    data.truncate(0)
    data.write("Win\tRounds\n")
    data.close()

def main() :
    print("ave or clear")
    val = input()
    if val == "clear" :
        clear()
    elif val == "ave" :
        ave()

main()