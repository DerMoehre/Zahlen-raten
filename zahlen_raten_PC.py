from random import *

#Range definieren
start_range = 1
end_range = 100

spiel_aktiv = True
pc_try = 1
benutzer_input = int(input(f"Nenne deine Zahl im Bereich von {start_range} und {end_range}: "))

#Computer erste Zahl raten lassen
pc_guess = randint(start_range,end_range)

def cut_range(last_guess, start, end, status):
    if status == "k":
        start = last_guess + 1
        return last_guess, start, end, status
    elif status == "g":
        end = last_guess - 1
        return last_guess, start, end, status
        
#Findet Mitte von verbleibenden Zahlen und gibt diese zurück
def next_guess(start, end):
    mid = end - start
    next = start + (round(mid/2))
    return next

while spiel_aktiv:

    guess_print = input(f"Ist deine Zahl die {pc_guess}? J/N: ")
    
    if guess_print == "J":
        spiel_aktiv = False
        print(f"Der PC hat {pc_try} Versuche gebraucht")
    else:
        guess_status = input("War der Versuch zu (g)ross oder zu (k)lein?: ")
        pc_guess, start_range, end_range, guess_status = \
        cut_range(pc_guess, start_range, end_range, guess_status)
        pc_try += 1
        pc_guess = next_guess(start_range, end_range)
        continue

