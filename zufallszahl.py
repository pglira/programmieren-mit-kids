import random

zahl_max = 100

gesuchte_zahl = random.randint(1, zahl_max)
versuche = 0

while True:
    versuche += 1
    print(f"Versuch: {versuche}")

    antwort = int(input("Errate die Zufallszahl: "))

    if antwort == gesuchte_zahl:
        print(f"Das ist richtig! Die Zufallszahl ist {gesuchte_zahl}")
        print(f"Das Spiel geht weiter mit einer neuen Zahl.")
        versuche = 0
        gesuchte_zahl = random.randint(1, zahl_max)
        continue  # Schleife neu starten

    elif antwort < gesuchte_zahl:
        print("Die Zufallszahl ist größer!")

    elif antwort > gesuchte_zahl:
        print("Die Zufallszahl ist kleiner")
