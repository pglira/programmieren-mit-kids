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

## Wir lernen "Schleifen"

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

## Wir kann man den Benutzer etwas fragen?

### Lerne!

Wir können eine Eingabe vom Benutzer unseres Programmes verlangen und diese in eine Variable speicher. Das geht so:

```python
jahre = input("Wie alt bist du:")
```

Nun ist das Alter in der Variable ``alter`` gespeichert.

Dieses können wir jetzt auf den Bildschirm schreiben:

```python
print(f"Du bist {jahre} alt!")
```

### Spiele!

- Frage den Benutzer etwas lustiges und schreibe einen Satz mit dieser Eingabe 10x auf den Bildschirm.

## Wir lernen eine Eingabe zu überprüfen

### Lerne!

Wir haben gerade gelernt wie man den Benutzer etwas frägt:

```python
antwort = input("Wieviele Bundesländer gibt es in Österreich?")
```

Nun kannst du überprüfen ob die Antwort richtig ist:

```python
if antwort == 9:
    print("Das ist richtig!")
else:
    print("Das ist falsch!")
```

Merke: ``if`` bedeuted ``wenn`` und ``else`` bedeuted ``sonst``.

### Spiele!

- Lass dir nun eine eigene Frage einfallen und lass diese von deinem Bruder oder deiner Schwester beantworten. Aber bitte nicht zu schwierig!