import math

x = input("Geben Sie ein paar 'X'e ein: ")
o = input("Geben Sie ein paar 'O'`s ein: ")

if x.count("X") == o.count("O"):
    print(True)
else:
    print(False)