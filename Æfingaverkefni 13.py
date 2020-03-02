#============================Verkefni 1=============================

# def margfoldunartafla(lina):
#     i = 1
#     while i < 11:
#         print(lina * i, end=" ")
#         i += 1
#
# tala = int(input("Hvada margfoldunartoflu viltu fa? "))
# margfoldunartafla(tala)

#============================Verkefni 2=============================

# def margfoldunartafla(lina):
#     i = 1
#     while i < 11:
#         print(lina * i, end=" ")
#         i += 1
#     print("\n")
#
# def tala():
#     j = 1;
#     while j < 11:
#         margfoldunartafla(j)
#         j +=1
#
# tala()

# ============================Verkefni 3=============================
#
# def talnabil(byrjun, endir):
#
#     for i in range(byrjun, endir+1 ,1):
#         print(i, end=' ')
#
# start = int(input("Start: "))
# stop = int(input("Stop: "))
# talnabil(start, stop)
#
# ============================Verkefni 4=============================

# def talnabil(byrjun, endir):
#
#     if byrjun == endir or endir - byrjun == 1:
#         print("Error")
#     else:
#         for i in range(byrjun+1, endir ,1):
#             print(i, end=' ')
# talnabil(5,10)

# ============================Verkefni 5=============================

# def veldi(tala, veldisvisir):
#     return tala ** veldisvisir
#
# for i in range(5):
#     print(veldi(i,i), end=' ')

# ============================Verkefni 6=============================

# def modulus(a, b):
#     c = a // b
#     c = c * b
#     afgangur = a - c
#     return afgangur
#
# tala1 = int(input("Sladu inn tolu 1: "))
# tala2 = int(input("Sladu inn tolu 2: "))
#
# print("Modulus talnanna er:", modulus(tala1,tala2))
# print("Modulus talnanna er:{}".format(modulus(tala1,tala2)))

# ============================Verkefni 7=============================

# def hlaupar(ar):
#     if ar % 4 == 0 or ar % 100 == 0 or ar % 400 == 0:
#         return "JA"
#     else:
#         return "NEI"
#
# for i in range(2000, 2010, 1):
#     print('Er',i,'hlaupar =',hlaupar(i))