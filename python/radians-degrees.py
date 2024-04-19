import math

number = int(input("Geben Sie die zu Konvertierende Zahl ein: "))
rad_or_degree = input("Ist die Zahl im Grad- oder im Bogenmaß angegeben? ")

if rad_or_degree == "Gradmaß":
    print(number * (math.pi/180))
elif rad_or_degree == "Bogenmaß":
    print(number * (180/math.pi))