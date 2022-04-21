"""
Problema No.2:Convercion de grados  Celcius a Farenge """

print("-----------------------------------------------------")
print("-------Convercion de grados  Celcius a Farenge-------")
print("-----------------------------------------------------")

# Input
C= input("digite los grados C:")
C= int(C)

#processing
K= C + 273.15
F= 1.8*C + 32

#output
print("\nResultado\n")

print( str (C) + " grados Celcius es igual a: " + str (F) + " grados Farengei")
print( str (C) + " grados Celcius es igual a: " + str (K) + " grados Kelvin")
