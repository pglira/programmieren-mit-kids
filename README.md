# Spaßiges Programmieren mit Kids

## Programmierumbebung

Gehe im Webbrowser zu ``https://www.online-python.com``. Hier können wir in der Sprache ``Python`` programmieren.

Lass uns beginnen!

## Wir lernen Text zu schreiben

### Lerne!

Wir können Text auf den Bildschirm schreiben. Schreibe:

```python
print("Hallo Welt!")
```

und führe aus. Was passiert?

### Spiele!

- Ändere den Code und begrüße dich selbst mit Vor- und Nachnamen!
- Versuchen nun folgende Katze auf den Bildschirm zu schreiben:

```
 /\_/\
( o.o )
 > ^ <
```

## Wir lernen Variablen

### Lerne!

Wir können in Variablen etwas speichern, zum Beispiel Zahlen:

```python
a = 2
b = 3
```

Mit diesen Variablen können wir auch rechnen! Ergänze:

```python
c = a + b
```

Diese können wir auch auf den Bildschirm schreiben:

```python
print(f"{a} plus {b} ist {c}")
```

Dabei musst du Variablen in geschwungenen Klammern angeben.

Merke: Damit das funktioniert, muss vor dem ersten Anführungszeichen ein ``f`` stehen.

### Spiele!

- Ändere nun die Variablenwerte, zum Beispiel könnte ``a`` den Wert 10 haben und ``b`` den Wert 15.
- Kannst du die beiden Variablen auch voneinander abziehen (Subtraktion)?

## Wir lernen etwas mehrfach zu wiederholen

### Lerne!

Schreibe 3 mal den gleichen Text:

```python
print("Hallo du!")
print("Hallo du!")
print("Hallo du!")
```

Das alles zu tippen ist ganz schön mühsam oder? Geht das nicht einfacher?

Vielleicht so?

```python
for i in range(3):
    print("Hallo du!")
```

Merke: Mit Schleifen können wir etwas öfter wiederholen. Hier wird der Text ``Hallo du!`` drei mal geschrieben.

### Spiele!

- Kannst du das auch 100x schreiben lassen? Was musst du dazu ändern? Probiere es aus!

## Wie kann man den Benutzer etwas fragen?

### Lerne!

Wir können eine Eingabe vom Benutzer unseres Programmes verlangen und diese in eine Variable speicher. Das geht so:

```python
jahre = input("Wie alt bist du?")
```

Nun ist das Alter in der Variable ``alter`` gespeichert.

Dieses können wir jetzt auf den Bildschirm schreiben:

```python
print(f"Du bist {jahre} Jahre alt!")
```

### Spiele!

- Frage den Benutzer etwas lustiges und schreibe einen Satz mit dieser Eingabe 10x auf den Bildschirm.

## Wir lernen eine Eingabe zu überprüfen

### Lerne!

Wir haben gerade gelernt wie man den Benutzer etwas frägt:

```python
antwort = input("Wie viele Mitglieder hat die Band Deine Freunde?")
```

Nun kannst du überprüfen ob die Antwort richtig ist:

```python
if antwort == "3":
    print("Das ist richtig! Sie heißen Flo, Pauli und Lukas.")
else:
    print("Das ist falsch! Kennst du denn diese Band gar nicht?")
```

Merke: ``if`` bedeuted ``wenn`` und ``else`` bedeuted ``sonst``.

### Spiele!

- Lass dir nun eine eigene Frage einfallen und lass diese von deinem Bruder oder deiner Schwester beantworten. Aber bitte nicht zu schwierig!

## Wir lernen etwas unendlich oft zu wiederholen

### Lerne!

Oben haben wir gelernt etwas x mal zu wiederholen, zum Beispiel so:

```python
for i in range(3):
    print("Hallo du!")
```

Wie können wir aber etwas unendlich oft wiederholen? Das geht so:

```python
while True:
    print("Das wird nun immer wieder auf den Bildschirm geschrieben!")
```

Merke: ``while`` bedeutet ``während``, ``True`` bedeutet ``wahr``.

Wann braucht man das? Zum Beispiel wenn ein Programm laufen soll bis der Benutzer es beendet. Den Code hier kannst du übrigens durch Drücken von ``ctrl+c`` abbrechen.

### Spiele!

- Schaffst du es eine Variable ``i`` innerhalb der unendlichen Schleife immer um 1 zu erhöhen? Gib dabei die Variable auch jedes Mal auf dem Bildschirm aus.

## Raspberry Pi - Sense HAT

### Wir schreiben etwas

### Lerne

Wir müssen zunächst dafür sorgen, dass wir mit dem Sense HAT kommunizieren ("sprechen") können. Dafür müssen immer die folgenden zwei Zeilen ganz oben stehen:

```python
from sense_hat import SenseHat
sense = SenseHat()
```

Nun können wir auf dem Sense HAT Text ausgeben:

```python
sense.show_message("Halli Hallo!")
```

### Spiele

- Ändere den Text auf etwas aufregenderes.

### Referenzen

- https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat
- https://github.com/martinohanlon/AstroPiSnake
- https://github.com/AndrewCRichards/TetriPiSense
- https://nerdyteachers.com/PICO-8/

## Links

Nachfolgend einige Links zu interessanten Projekten die auch als Inpirationsquelle für eigene Projekte dienen können.

