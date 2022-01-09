from random import *

zahlenraum = randint(1, 10)

spiel_aktiv = True
versuche = 4

while spiel_aktiv:
    benutzer_input = int(input("Nenne deine Zahl: "))
    if versuche > 0:
        if zahlenraum > benutzer_input:
            print("Deine Zahl ist zu niedrig")
            versuche = versuche -1
            print(f"Verbleibende Versuche: {versuche}")
            
        elif zahlenraum < benutzer_input:
            print("Deine Zahl ist zu groß")
            versuche = versuche -1
            print(f"Verbleibende Versuche: {versuche}")
            
        else:
            print("Du hast richtig geraten")
            spiel_aktiv = False
    else:
        spiel_aktiv = False
        print("Du hast deine Versuche verbraucht")
        print(f"Die richtige Zahl wäre {zahlenraum} gewesen")