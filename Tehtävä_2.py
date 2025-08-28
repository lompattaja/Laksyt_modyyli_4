#En ihan ymmärtäny, mitä tehtävän annossa haluttiin, joten tein vain ohjelman, joka
#lopettaa toiminnan, jos käyttäjä antaa negatiivisen arvon.
while True:
    tuumat = float(input("anna tuumamäärä (lopeta negatiivisella arvolla)"))

    if tuumat <0:
        print("Lopetit ohjelman")
        break

    cm = tuumat * 2.54
    print(f"{tuumat}tuumaa = {cm}cm")
