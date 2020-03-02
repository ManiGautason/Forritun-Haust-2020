#============================Verkefni A=============================

# texti = "Hallo heimur"
# print("Fyrsti stafur",texti[0])
# print("Sidasti stafur",texti[-1])
# print("Textin er",len(texti),"stafa langur")

#============================Verkefni B=============================

# texti = "A Santa at Nasa"
# for i in texti:
#     print(i)
#
# print("\n")
# texti_afturabak = texti[::-1]
# for j in texti_afturabak:
#     print(j)

#============================Verkefni C=============================

# texti = input("Sladu inn texta: ")
# fjoldi = int(input("sladu in fjolda stafa sem tu vilt prenta ur: "))
# i = 0
# while i < fjoldi:
#     print(texti[i])
#     i += 1

#============================Verkefni D=============================

# texti = input("Sladu inn texta: ")
# skref = int(input("sladu in tolu: "))
# nyr_texti = texti[::skref]
# print(nyr_texti)

#============================Verkefni E=============================

# texti = input("Sladu inn texta: ")
# stafur = int(input("1 fyrir hastafi. 2 fyrir lagstofum: "))
# texti_breyttur = ""
# for i in texti:
#     if stafur == 1:
#         if i.isupper() == True:
#             texti_breyttur += i
#     else:
#         if i.islower() == True:
#             texti_breyttur += i
#
# print(texti_breyttur)

#============================Verkefni F=============================

# nafn = input("Sladu inn nafn: ")
# aldur = int(input("Sladu inn aldur: "))
# starf = input("Sladu inn starf: ")
#
# strengur = "Eg heiti {}, eg er {} og starfa sem {}"
# print(strengur.format(nafn, aldur, starf))

#============================Verkefni G=============================

# strengur = input("Sladu in streng: ")
#
# if "hallo" in strengur:
#     print("Já strengurinn er í strengnum")
# else:
#     print("nei tvi midur er hann ekki")

#============================Verkefni H=============================

# strengur = input("Sladu in streng: ")
#
# if strengur.isdigit():
#     print("Strengurinn inniheldur adeins tolustafi")
# elif strengur.isalpha():
#     print("Strengurinn inniheldur adeins bokstafi")
# else:
#     print("Strengurinn er skrítinn")

