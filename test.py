# import os
# import random
# import string

# def add_numbers(a, b):
#     """Addiert zwei Zahlen."""
#     return a + b

# def subtract_numbers(a, b):
#     """Subtrahiert zwei Zahlen."""
#     return a - b

# def multiply_numbers(a, b):
#     """Multipliziert zwei Zahlen."""
#     return a * b

# def divide_numbers(a, b):
#     """Dividiert zwei Zahlen, wenn der Nenner nicht Null ist."""
#     if b == 0:
#         return "Division durch Null ist nicht erlaubt!"
#     return a / b

# def reverse_string(s):
#     """Kehrt einen String um."""
#     return s[::-1]

# def count_vowels(s):
#     """Zählt die Vokale in einem String."""
#     vowels = 'aeiouAEIOU'
#     return sum(1 for char in s if char in vowels)

# def write_to_file(filename, content):
#     """Schreibt Inhalt in eine Datei."""
#     with open(filename, 'w') as file:
#         file.write(content)

# def read_from_file(filename):
#     """Liest den Inhalt einer Datei."""
#     if os.path.exists(filename):
#         with open(filename, 'r') as file:
#             return file.read()
#     return "Datei existiert nicht!"

# def generate_random_string(length):
#     """Generiert einen zufälligen String der angegebenen Länge."""
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# def guessing_game():
#     """Ein einfaches Zahlenschätzspiel."""
#     print("Willkommen beim Zahlenschätzspiel!")
#     number_to_guess = random.randint(1, 100)
#     attempts = 0

#     while True:
#         guess = int(input("Gib eine Zahl zwischen 1 und 100 ein: "))
#         attempts += 1

#         if guess < number_to_guess:
#             print("Zu niedrig!")
#         elif guess > number_to_guess:
#             print("Zu hoch!")
#         else:
#             print(f"Glückwunsch! Du hast die Zahl {number_to_guess} in {attempts} Versuchen erraten.")
#             break

# def factorial(n):
#     """Berechnet die Fakultät einer Zahl."""
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# def fibonacci(n):
#     """Gibt die Fibonacci-Folge bis zur n-ten Zahl zurück."""
#     sequence = [0, 1]
#     while len(sequence) < n:
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence[:n]

# def main():
#     """Hauptfunktion zum Testen aller anderen Funktionen."""
#     print("=== Mathematische Funktionen ===")
#     print(f"Addition: 3 + 5 = {add_numbers(3, 5)}")
#     print(f"Subtraktion: 10 - 4 = {subtract_numbers(10, 4)}")
#     print(f"Multiplikation: 6 * 7 = {multiply_numbers(6, 7)}")
#     print(f"Division: 8 / 2 = {divide_numbers(8, 2)}")

#     print("\n=== Textverarbeitung ===")
#     sample_text = "Hallo, Welt!"
#     print(f"Umgekehrter String: {reverse_string(sample_text)}")
#     print(f"Vokalanzahl: {count_vowels(sample_text)}")

#     print("\n=== Dateioperationen ===")
#     filename = "test.txt"
#     content = "Dies ist ein Test."
#     write_to_file(filename, content)
#     print(f"Dateiinhalt: {read_from_file(filename)}")

#     print("\n=== Zufällige Daten ===")
#     print(f"Zufälliger String: {generate_random_string(10)}")

#     print("\n=== Fakultät und Fibonacci ===")
#     print(f"Fakultät von 5: {factorial(5)}")
#     print(f"Fibonacci-Folge (10 Zahlen): {fibonacci(10)}")

#     print("\n=== Zahlenschätzspiel ===")
#     guessing_game()  # Kann aktiviert werden, um das Spiel zu spielen


import pyautogui
import time

# Funktion zum Öffnen eines Programms (z. B. Notepad unter Windows)
def open_notepad():
    pyautogui.press('win')  # Windows-Taste drücken
    time.sleep(1)  # Warten, bis das Startmenü erscheint
    pyautogui.write('notepad')  # "Notepad" eingeben
    pyautogui.press('enter')  # Enter drücken, um das Programm zu starten

def write_in_notepad():
    time.sleep(2)  # Warten, bis Notepad gestartet ist
    pyautogui.write("Hallo, das ist eine automatische Eingabe via PyAutoGUI!", interval=0.1)  # Text eingeben

def save_file():
    pyautogui.hotkey('ctrl', 's')  # Speichern-Shortcut drücken
    time.sleep(1)
    pyautogui.write('rpa_test.txt')  # Dateiname eingeben
    pyautogui.press('enter')  # Speichern bestätigen

def main():
    print("Automatisierung wird gestartet...")
    open_notepad()
    write_in_notepad()
    save_file()
    print("Automatisierung abgeschlossen!")

if __name__ == "__main__":
    main()
