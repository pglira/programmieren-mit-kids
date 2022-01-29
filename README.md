# Spaßiges Programmieren mit Kids

## Python

### Programmierumbebung

Gehe im Webbrowser zu ``https://www.online-python.com``. Hier können wir in der Sprache ``Python`` programmieren.

Lass uns beginnen!

### Wir lernen Text zu schreiben

#### Lerne!

Wir können Text auf den Bildschirm schreiben. Schreibe:

```python
print("Hallo Welt!")
```

und führe aus. Was passiert?

#### Spiele!

- Ändere den Code und begrüße dich selbst mit Vor- und Nachnamen!
- Versuchen nun folgende Katze auf den Bildschirm zu schreiben:

```
 /\_/\
( o.o )
 > ^ <
```

### Wir lernen Variablen

#### Lerne!

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

#### Spiele!

- Ändere nun die Variablenwerte, zum Beispiel könnte ``a`` den Wert 10 haben und ``b`` den Wert 15.
- Kannst du die beiden Variablen auch voneinander abziehen (Subtraktion)?

### Wir lernen etwas mehrfach zu wiederholen

#### Lerne!

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

#### Spiele!

- Kannst du das auch 100x schreiben lassen? Was musst du dazu ändern? Probiere es aus!

### Wie kann man den Benutzer etwas fragen?

#### Lerne!

Wir können eine Eingabe vom Benutzer unseres Programmes verlangen und diese in eine Variable speicher. Das geht so:

```python
jahre = input("Wie alt bist du?")
```

Nun ist das Alter in der Variable ``alter`` gespeichert.

Dieses können wir jetzt auf den Bildschirm schreiben:

```python
print(f"Du bist {jahre} Jahre alt!")
```

#### Spiele!

- Frage den Benutzer etwas lustiges und schreibe einen Satz mit dieser Eingabe 10x auf den Bildschirm.

### Wir lernen eine Eingabe zu überprüfen

#### Lerne!

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

#### Spiele!

- Lass dir nun eine eigene Frage einfallen und lass diese von deinem Bruder oder deiner Schwester beantworten. Aber bitte nicht zu schwierig!

## Wir lernen etwas unendlich oft zu wiederholen

#### Lerne!

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

#### Spiele!

- Schaffst du es eine Variable ``i`` innerhalb der unendlichen Schleife immer um 1 zu erhöhen? Gib dabei die Variable auch jedes Mal auf dem Bildschirm aus.

## Raspberry Pi - Sense HAT

### Wir schreiben etwas

#### Lerne

Wir müssen zunächst dafür sorgen, dass wir mit dem Sense HAT kommunizieren ("sprechen") können. Dafür müssen immer die folgenden zwei Zeilen ganz oben stehen:

```python
from sense_hat import SenseHat
sense = SenseHat()
```

Nun können wir auf dem Sense HAT Text ausgeben:

```python
sense.show_message("Halli Hallo!")
```

#### Spiele

- Ändere den Text auf etwas aufregenderes.

### Wir ändern dir Form des Textes

#### Lerne

Wir können die Geschwindigkeit und die Farbe des Textes ändern:

```python
yellow = (255, 255, 0) # Gelb
blue = (0, 0, 255) # Blau
sense.show_message("Halli Hallo!", text_colou^r=yellow, back_colour = blue, scroll_speed = 0.1)
```

Du hast hierbei die Funktion ``show_messages`` mit drei zusätzlichen Parametern aufgerufen:

- ``text_colour``: Textfarbe
- ``back_colour``: Hintergrundfarbe
- ``scroll_speed``: Die Geschwindigkeit des Textes

Farben werden mit 3 Werten angeben: Rot, Grün und Blau. Jede dieser drei Farben hat einen Wert zwischen 0 und 255. Die finale Farbe ergibt sich durch "Mischen" dieser drei Farben.

#### Spiele

- Versuche einen roten Text auf blauem Hintergrund mit sehr hoher Geschwindigkeit zu schreiben.

### Wir lernen einen Text unendlich oft zu schreiben

#### Lerne

Du kannst dich sicher noch erinnern wie man eine unendliche Schleife erzeugt. Richtig! So:

```python
while True:
    sense.show_message("Bis in alle Ewigkeit!")
```

#### Spiele

- Welche Nachricht sollte jemand der dein Zimmer betritt lesen? Ändere den Text sowie gegebenenfalls auch seine Form (Farbe und Geschwindigkeit).

### Wir lernen nun einzelne Buchstaben nacheinander zu schreiben

#### Lerne

Einen einzelnen Buchstaben kannst du am Sense HAT so schreiben:

```python
sense.show_letter("J")
```

Du kannst nun mehrere Buchstaben hintereinander ausgeben, allerdings solltest du dazwischen immer eine kleine Pause einbauen:

```python
sense.show_letter("J")
sleep(1) # das Programm macht hier 1 Sekunde Pause
sense.show_letter("a")
sleep(1)
sense.show_letter("k")
sleep(1)
sense.show_letter("o")
sleep(1)
sense.show_letter("b")
```

#### Spiele

- Kannst du die Farben auch abwechselnd in zwei verschiedenen Farben schreiben? Du kannst diese Internetseite öffnen um Farben auszuwählen: https://www.w3schools.com/colors/colors_picker.asp


### Wir zeichnen ein Pixelbild

#### Lerne

Mit diesem Skript zeichnen wir ein Bild auf dem Sense HAT. Schau dir zur Erklärung die Kommentare an:

```python
from sense_hat import SenseHat

sense = SenseHat()

# Hier definieren wir zwei Farben
g = (0, 255, 0) # Grün
b = (0, 0, 0) # Scharz

# Jetzt definieren wir hier ein Bild
pixel_image = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

# Das Bild können wir nun mit diesem Befehl anzeigen
sense.set_pixels(pixel_image)
```

Was ist das denn? Etwa ein **creeper**? :-)

#### Spiele

- Ändere das Bild, z.B. zu einem Muster.
- Ändere dein gesamtes Skript auf folgenden Text (du musst diesen nicht abschreiben sondern kannst ihn einfach von hier kopieren):

```python
from sense_hat import SenseHat

sense = SenseHat()

B = (102, 51, 0)
b = (0, 0, 255)
S = (205,133,63)
W = (255, 255, 255)

pixel_image = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, W, b, S, S, b, W, S,
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S
]

sense.set_pixels(pixel_image)
```

Führe nun das Skript aus. Kennst du diesen Kerl von irgendwo? Verstehst du das Programm?

#### Referenzen

- https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat
- https://github.com/martinohanlon/AstroPiSnake
- https://github.com/AndrewCRichards/TetriPiSense
- https://nerdyteachers.com/PICO-8/

## Links

Nachfolgend einige Links zu interessanten Projekten die auch als Inpirationsquelle für eigene Projekte dienen können.

