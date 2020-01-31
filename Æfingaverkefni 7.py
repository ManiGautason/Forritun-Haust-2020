#=========================================Verkefni 1====================================================

# timi = int(input("Hvad er klukkan?"))
#
# if timi < 18:
#     print("Godan daginn")
# else:
#     print("Goda kvoldid")

#=========================================Verkefni 2====================================================

# tala1 = int(input("Sladu inn tolu: "))
# tala2 = int(input("sladu inn seinni tolu: "))
#
# if tala1 < tala2:
#     print("seinni talan er staerri")
# elif tala2 < tala1:
#     print("fyrri talan er staerri")
# else:
#     print("tolurnar eru jafn storar")

#=========================================Verkefni 3====================================================

# tala1, tala2, tala3 = input("sladu inn 3 tolur:").split()
#
# if tala1 > tala2 and tala1 > tala3:
#     print("talan nr 1 er staerst")
# elif tala2 > tala1 and tala2 > tala3:
#     print("tala nr 2 er staerst")
# else:
#     print("tala nr 3 er staerst")

#=========================================Verkefni 4====================================================

# aldur = int(input("Hvad ertu gamall? "))
#
# if aldur > -1 and aldur < 20:
#     print("Vonandi ætlar þú í Háskólann í Reykjavík")
# else:
#     print("tað var fróðlegt!")

#=========================================Verkefni 5====================================================

# aldur = int(input("Hvad ertu gamall? "))
#
# if aldur > -1 and aldur < 7:
#     print("svo þú ferð að byrja í skóla")
# elif aldur > 6 and aldur < 16:
#     svar = input("aetlar tu i menntaskola J/N? ")
#     if svar == "j":
#         print("Va frabaert")
#     else:
#         print("tad er ekki nogu gott")
# elif aldur > 15 and aldur < 106:
#     print("Okei bae")
# else: print("tu hefur slegid inn vitlaust")

#=========================================Verkefni 6====================================================


# ar = int(input("sladu inn artal: "))
# ar %= 4
# if ar == 0:
#     print("arid er hlaupar")
# else:
#     print("arid er ekki hlaupar")


#=========================================Verkefni 6====================================================

# ar = int(input("sladu inn artal: "))
# ar1 = ar%4
# ar2 = ar%100
# ar3 = ar%400
#
# if ar1 == 0 or ar2 == 0 or ar3 == 0:
#     print("arid er hlaupar")
# else:
#     print("arid er ekki hlaupar")