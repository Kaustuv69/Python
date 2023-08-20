while True:
    x = int(input("Enter marks of computer"))
    b = int(input("Enter marks of science"))
    c = int(input("Enter marks of math"))
    d = int(input("Enter marks of opt math"))
    e = int(input("Enter marks of english"))
    f = int(input("Enter marks of nepali"))
    g = int(input("Enter marks of social"))
    s = x + b + c + d + e + f + g
    if s>700:
        print("Reenter the values under 100")
        continue
    print("Computer :", x)
    print("Science :", b)
    print("Math :", c)
    print("Opt math :", d)
    print("English :", e)
    print("Nepali :", f)
    print("Social :", g)
    ts = 700
    print("Obtained marks:", s)
    print("Total marks :", 700)
    per = (s / ts) * 100
    print("Percentage :", per)
    g = (s / ts) * 4
    print("GPA :", g)
    if per >= 90:
        print(" You got A+")
    elif per >= 80 and per < 90:
        print("You got A")
    elif per >= 70 and per < 80:
        print("You have got B+")
    elif per >= 60 and per < 70:
        print("You have got B")
    elif per >= 50 and per < 60:
        print("You have passed with too less marks ")
    else:
        print("Go home and read, You're a Failure!!")
    break        
