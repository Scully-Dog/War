def ave() :
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