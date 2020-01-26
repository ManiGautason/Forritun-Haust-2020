#============================Virðisaukaskattur=============================

print("Sladu inn upphaed til ad reikna ut virdisaukaskatt")
upphaed = int(input("Upphaed: "))

print("Upphaed med virdisaukaskatti er: ", upphaed*1.255)


#============================Litrafjoldi=====================================

litrar = int(input("Sladu inn litrafjolda: "))
print(litrar,"L eru", litrar * 3.6, "Gallon")

#============================Flatarmál hrings================================

radius = int(input("Sladu inn radius hrings: "))

print("Flatarmál hrings er: ", radius * radius * 3.14)

#============================Flatarmál trapisu================================

langhlid = int(input("Sladu inn langhlid: "))
skammhlid = int(input("Sladu inn skammhlid: "))
haed = int(input("Sladu inn haed: \n"))

print("Flatarmál trapisu er: ", (langhlid + skammhlid) * haed / 2)

#============================Hitastig========================================

print("F -----> C \n")
farenheit = int(input("Sladu inn farenheit: "))

print(farenheit, "f eru ", (5/9)*(farenheit-32), "celsius")

#============================Þyngdarstuðull===================================

print("BMI reiknvel \n")

tyngd = int(input("Sladu inn tyngd (Kg): "))
haed = float(input("Sladu inn haed (m): "))
BMI = tyngd / haed**2
print("BMI thitt er:", BMI)

#============================Skattur============================================

alagningsprosenta = float(input("Sladu inn álagningsprósentu: "))
personuaffslattur = float(input("Sladu inn persónuafslátt: "))
laun = float(input("Sladu inn laun: "))

alagningsprosenta = 0.1 * alagningsprosenta
stadgreidsla = laun * alagningsprosenta - personuaffslattur

if stadgreidsla > 0:
    print("Stadgreidsla skatts er ",stadgreidsla)
else:
    print("Stadgreidsla skatts er neikvaed , Ríkid getur aldrei tapad")