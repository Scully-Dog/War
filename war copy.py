import random

cards = ['1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13']
cardNames = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD']

def win(num) :
    print("Congrats Player", num, "You Won")
    stat = open('stats.txt', 'a')
    txt = str(num) + " " + str(cnt) + "\n"
    stat.write(txt)
    exit()

def overWar(plr, num) :
    if plr == 1 :
        num1 = len(pl1) - 1
        print(num1, "num 1")
        return num1
    elif plr == 2 :
        num2 = len(pl2) - 1
        print(num2, "num 2")
        return num2
    else :
        print('bruh how')
        return 0
            
def war(num, warCnt) :
    print(pl1)
    print(pl2)
    num += 4
    numM = num
    trig = None
    try :
        if pl1[numM] == 'None' :
           numM = overWar(1, numM)
    except :
        numM = overWar(1, numM)
        trig = True
    try :
        if pl2[numM] == 'None' :
            numM = overWar(2, numM)
    except :
        numM = overWar(2, numM)
        trig = False
    print(numM)
    if pl1[numM] > pl2[numM] :
        for i in range(numM) :
            print(i)
            pl1.append(pl2[0])
            pl2.remove(pl2[0])
            pl1.append(pl1[0])
            pl1.remove(pl1[0])
    elif pl1[numM] < pl2[numM] :
        for i in range(numM) :
            print(i)
            pl2.append(pl1[0])
            pl1.remove(pl1[0])
            pl2.append(pl2[0])
            pl2.remove(pl2[0])
    elif pl1[numM] == pl2[numM] and numM == 0 :
        if trig :
            print("Sorry player 1 but you ran out of cards")
            win(2)
        else :
            print("Sorry player 2 but you ran out of cards")
            win(1)
    elif pl1[numM] == pl2[numM] :
        warCnt += 1
        print('war', warCnt)
        if warCnt > 25 :
            print("error")
            if trig :
                print("Sorry player 1 but you ran out of cards")
            win(2)
        elif trig == False :
            print("Sorry player 2 but you ran out of cards")
            win(1)
        war(num, warCnt)
    else :
        print("Bruh get out of me hidey hole")
        exit()

def main() :
    game = True
    global cnt
    cnt = 0
    while game :
        warCnt = 0
        if game and pl1[0] > pl2[0]:
            pl1.append(pl2[0])
            pl2.remove(pl2[0])
            pl1.append(pl1[0])
            pl1.remove(pl1[0])
            print('pl1')
        elif game and pl1[0] < pl2[0]:
            pl2.append(pl1[0])
            pl1.remove(pl1[0])
            pl2.append(pl2[0])
            pl2.remove(pl2[0])
            print("pl2")
        elif game and pl1[0] == pl2[0]:
            war(0, 0)
        cnt += 1
        print(cnt)
        try :
            if pl1[0] == 'None' :
                win(2)
                game = False
        except :
            win(2)
            game = False
        try : 
            if pl2[0] == 'None' :
                win(1)
                game = False
        except :
            win(1)
            game = False

random.shuffle(cards)
lent = len(cards) // 2
pl1 = cards[lent:]
pl2 = cards[:lent]
print(pl1)
print(pl2)
main()