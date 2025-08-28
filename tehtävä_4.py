#Arvaus peli, joka arpoo numeron ja kehottaa käyttäjää arvaamaan sen
import random
luku = random.randint(1,10)
while True:
    arvaus = float(input("anna arvaus (1-10)"))
    if arvaus == luku:
        print("arvasit oikein!")
        break
    elif arvaus < luku:
        print("Arvauksesi on liian pieni")

    elif arvaus > luku:
        print("Arvauksesi on liian suuri")

