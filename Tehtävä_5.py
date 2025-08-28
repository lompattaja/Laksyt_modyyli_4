#Ohjelma, joka kysyy käyttäjä tunnuksen ja salasanan, jotka on aiemmin annettu tehtävässä
#Käyttäjä tunnus: python
#salasana: rules
user = "python"
password = "rules"
tries = 5 #kuinka monta yritystä on jäljellä
while True:
    user_guess= input("anna käyttäjänimi")
    password_guess = input("anna salasana")
    if user_guess == user and password_guess == password:
        print("Käyttäjänimi ja salasana on oikein!")
        break
    elif tries <= 1:
        print("5 yritystäsi on mennyt umpeen")
        break
    else:
        print("Käyttäjänimi, tai salasana on väärin.")
        tries = tries - 1
        print(f"sinulla on {tries} yritystä jäljellä.")

