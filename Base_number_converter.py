def Convert10():
    List = []
    Sum = 0
    u = 0
    print("=== Convert to base10 ===")
    try:
        b = int(input("Enter base of number [2-16] : "))
    except:
        print("!!! Enter NUMBER !!!")
    n = input("Enter base "+str(b)+" number : ")   
    for i in n:
        if i == "A":
            i = 10
        if i == "B":
            i = 11
        if i == "C":
            i = 12
        if i == "D":
            i = 13
        if i == "E":
            i = 14
        if i == "F":
            i = 15
        List.append(i)
    List.reverse()
    for x in List:
        Sum = Sum + (int(x)*(b**u))
        u += 1
    print(str(b)+'to10 is',Sum)
    print("")




def BaseConvert():
    print("=== BaseConvert ===")
    List = []
    try:
        num = int(input("Enter base 10 number : "))
        b = int(input("Enter base of number [2 - 16] : "))
        if num == 0:
            print("0")
        else:
            while num != 0:
                x = num % b
                num = num // b
                if x == 10:
                    x = "A"
                if x == 11:
                    x = "B"
                if x == 12:
                    x = "C"
                if x == 13:
                    x = "D"
                if x == 14:
                    x = "E"
                if x == 15:
                    x = "F"     
                List.append(x)
            List.reverse()
            print("10to"+str(b)+" is ",end='')
            for i in List:
                print(i,end='')
        print("\n")
    except ValueError:
        print("!!! Enter NUMBER !!!")






print("=====================\nBase number convertor\n=====================")
while True:
    select = input("[1] Convert to 10\n[2] 10 Convert to\nSelect menu : ")
    if select == "1":
        print()
        Convert10()
    elif select == "2":
        print()
        BaseConvert()
