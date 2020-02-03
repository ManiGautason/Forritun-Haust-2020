import numpy as np
#=========================================APAR====================================================

a_bros = input("Brosir api 1? ")
b_bros = input("Brosir api 2? ")

if (a_bros == 'j' and b_bros == 'j') or (a_bros == 'j' and b_bros == 'n') or (a_bros == 'n' and b_bros == 'j'):
    print("TAd er eitthvad ekki i lagi")
else:
    print("Allt er i godu")

#========================================='ikornar i palo alto"====================================================

sumar = input("Er sumar? ")
hitastig = int(input("hvad er hitastigid"))

if sumar == 'j':
    if hitastig > 59 and 101 > hitastig:
        print("Tad er sumar og teir eru ad leika ser")
    else:
        print("tad er sumar en teir eru EKKI ad leika ser")
else:
    if hitastig > 59 and 91 > hitastig:
        print("Tad er ekki sumar en teir eru uti ad leika ser")
    else:
        print("Tad er ekki sumar og teir eru EKKI ad leika ser")

#========================================='Talnabil fyrir utan margfeldi af 5"====================================================

byrjun = int(input("Sladu in upphaf bils: "))
endir = int(input("Sladu in enda bils: "))

for i in range(byrjun, endir + 1, 1):
    if i%5 != 0:
        print(i)

#=========================================Töfratalan 666====================================================

tala1 = int(input("Sladu in tolu a: "))
tala2 = int(input("Sladu in tolu b: "))

if tala1 + tala2 == 666 or tala2 - tala1 == 666 or tala1 == 666 or tala2 == 666:
    print("Merki dyrsins")
else:
    print("Ekkert ahugavert")

#=========================================Skákborð====================================================

x = np.zeros((8, 8), dtype = int)

x[1::2, ::2] = 1
x[::2, 1::2] = 1

for i in range(8):
    for j in range(8):
        print(x[i][j], end="")
    print()


