def menu():
    print ("\n1. Pare xartaki\n2. Eksuphrethsh\n3. Eksodos\n")
    choice = int(input("Dialekse energeia: \n"))
    return choice

def xartakia(oura):
    global n,check,firstTime, avrg
    oura.append(n)
    print ("phres to xartaki sou einai to {}\n".format(n))
    check = time.localtime()
    firstTime = int(time.strftime("%M", check))
    avrg.append(firstTime)
    n+=1

def eksupirethsh(oura):
    global check,secondTime, avrg
    if isEmpty(oura):
        print ("den yparxoyn pelates")
    else:
        print ("eksuphrethte o {} twra\n".format(oura[0]))
        oura.pop(0)
        check2 = time.localtime()
        secondTime = int(time.strftime("%M", check2))
        avrgS.append(secondTime)
        check = avrgS[0] - avrg[0]
        avrga.append(check)
        avrg.pop(0), avrgS.pop(0)

def isEmpty(oura):
    return oura == []

import time
n = 1
avrg = []
avrgS = []
avrga = []
oura = []
ans = True
while ans:
    choice = menu()
    if choice == 1:
        xartakia(oura)
    elif choice == 2:
        eksupirethsh(oura)
    elif choice == 3:
        ans = False
    try:
        e = str(sum(avrga) / len(avrga))
        print ("Average waiting time:", e[:3] , "min(s)")
    except ZeroDivisionError:
        print ("Average waiting time:", "0.0 min(s)")
