t = int(input())

for i in range(t):
    d, m = input().split()
    d = int(d)

    if (21<=d<=31 and m=="Mar") or (1<=d<=20 and m=="Apr"):
        print("Aries")
    elif (21<=d<=30 and m=="Apr") or (1<=d<=20 and m=="May"):
        print("Taurus")
    elif (21<=d<=31 and m=="May") or (1<=d<=20 and m=="Jun"):
        print("Gemini")
    elif (21<=d<=30 and m=="Jun") or (1<=d<=22 and m=="Jul"):
        print("Cancer")
    elif (23<=d<=31 and m=="Jul") or (1<=d<=22 and m=="Aug"):
        print("Leo")
    elif (23<=d<=31 and m=="Aug") or (1<=d<=22 and m=="Sep"):
        print("Virgo")
    elif (23<=d<=30 and m=="Sep") or (1<=d<=22 and m=="Oct"):
        print("Libra")
    elif (23<=d<=31 and m=="Oct") or (1<=d<=22 and m=="Nov"):
        print("Scorpio")
    elif (23<=d<=30 and m=="Nov") or (1<=d<=21 and m=="Dec"):
        print("Sagittarius")
    elif (22<=d<=31 and m=="Dec") or (1<=d<=19 and m=="Jan"):
        print("Capricorn")
    elif (20<=d<=31 and m=="Jan") or (1<=d<=19 and m=="Feb"):
        print("Aquarius")
    elif (20<=d<=29 and m=="Feb") or (1<=d<=20 and m=="Mar"):
        print("Pisces")