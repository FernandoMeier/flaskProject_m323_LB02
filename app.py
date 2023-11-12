from flask import Flask, render_template
from random import random
from functools import reduce

# Flask App initialisieren und TodoDao-Objekt erstellen
app = Flask(__name__)

"""
ideas: code snippets repo, 
"""


@app.route("/")
def add_todo():
    return "Endpoints: " + render_template("index.html")


@app.route("/doc")
def documentation():
    return render_template("doc.html")


@app.route("/A1G")
def A1G():
    """
    Ich kann die Eigenschaften von Funktionen beschreiben (z.Bsp. pure function) und den Unterschied zu anderen
    Programmierstrukturen erläutern (z.Bsp. zu Prozedur).
    """

    def pure_function(value):
        return str(value)

    def impure_function(value):
        return str(random() * 16 * value)

    return f"input = 5<br>pure function (no  side effects): {pure_function(5)}<br>impure function (side effects possible): {impure_function(5)}"


@app.route("/A1F")
def A1F():
    """
    Ich kann das Konzept von *immutable values* erläutern und dazu Beispiele anwenden. Somit kann ich dieses Konzept
    funktionaler Programmierung im Unterschied zu anderen Programmiersprachen erklären
    (z.Bsp. im Vergleich zu referenzierten Objekten)
    """

    def immutable_function(new_list):
        if not new_list:
            return 0
        for i in new_list:
            updated = new_list[1:]
            return i + immutable_function(updated)

    result = immutable_function([1, 2, 3, 4, 5])
    return str(result)


@app.route("/A1E")
def A1E():
    """
    Ich kann aufzeigen wie Probleme in den verschiedenen Konzepten (OO, prozedural und funktional) gelöst werden und
    diese miteinander vergleichen.
    """
    return "<a href='/A1E/OOP'><button>Go to OOP solution</button></a><br>" \
           "<a href='/A1E/procedural'><button>Go to procedural solution</button></a><br>" \
           "<a href='/A1E/functional'><button>Go to functional solution</button></a><br>"


@app.route("/A1E/OOP")
def OOP():
    class Car:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def display_info(self):
            return f"Brand: {self.brand}, Model: {self.model}"

    my_car = Car("Toyota", "Corolla")
    return my_car.display_info()


@app.route("/A1E/procedural")
def procedural():
    def add_and_multiply(val):
        added = val + 3
        multiplied = val * 3
        return f"3 and 10... added: {added}, multiplied: {multiplied}"

    value = 10
    return str(add_and_multiply(value))


@app.route("/A1E/functional")
def functional():
    def multiply_numbers(a, b):
        return a * b

    def add_numbers(a, b):
        return a + b

    return f"3 and 5:<br><br>added = {add_numbers(3, 5)}<br><br>multiplied = {multiply_numbers(3, 5)}"


@app.route("/B1G")
def B1G():
    """
    Ich kann ein Algorithmus erklären
    """

    def einfacher_algorithmus(zahl):
        ergebnis = zahl * 3
        return ergebnis

    ergebnis_einfach = einfacher_algorithmus(5)
    return str(ergebnis_einfach)


@app.route("/B1F")
def B1F():
    """
    Ich kann Algorithmen in funktionale Teilstücke aufteilen
    """

    def multipliziere_mit_drei(zahl):
        return zahl * 3

    def fuege_zusammen(ergebnis):
        ergebnis = f"ergebnis: {ergebnis}"
        return ergebnis

    ergebnis_funktional = fuege_zusammen(multipliziere_mit_drei(5))
    return ergebnis_funktional


@app.route("/B1E")
def B1E():
    """
    Ich kann Funktionen in zusammenhängende Algorithmen implementieren
    :return:
    """

    def multipliziere_mit_drei(zahl):
        return zahl * 3

    def fuege_zusammen(ergebnis):
        ergebnis = f"ergebnis: {ergebnis}"
        return ergebnis

    def zusammenhaengender_algorithmus(zahl):
        ergebnis = multipliziere_mit_drei(zahl)
        ergebnis = fuege_zusammen(ergebnis)

        ergebnis *= 2

        return ergebnis


    return zusammenhaengender_algorithmus(5)


@app.route("/B2G")
def B2G():
    """
    Ich kann Funktionen als Objekte behandeln und diese in Variablen speichern und weitergeben.
    """

    def greet_person(name):
        return f"Hello, {name}!"

    my_greeting = greet_person

    return my_greeting("Visitor")


@app.route("/B2F")
def B2F():
    """
    Ich kann Funktionen als Argumente für andere Funktionen verwenden und dadurch höherwertige Funktionen erstellen.
    :return:
    """

    def higher_order(function_name, value1, value2):
        return function_name(value1, value2)

    def add_values(val1, val2):
        return val1 + val2

    def subtract_values(val1, val2):
        return val1 - val2

    return f"5 and 8: added: {higher_order(add_values, 5, 8)}, subtracted: {higher_order(subtract_values, 5, 8)}"


@app.route("/B2E")
def B2E():
    """
    Ich kann Funktionen als Objekte und Argumente verwenden, um komplexe Aufgaben. (Anwenden von Closures)
    """

    def multiplication(factor):
        def multiply(num):
            return num * factor

        return multiply

    double_value = multiplication(2)
    tripple_value = multiplication(3)

    return f"Value 5: doubled: {double_value(5)}, tripled: {tripple_value(5)}"


@app.route("/B3G")
def B3G():
    """
    Ich kann einfache Lambda-Ausdrücke schreiben, die eine einzelne Operation durchführen, z.B. das
    Quadrieren einer Zahl oder das Konvertieren eines Strings in Großbuchstaben.
    """
    square_root = lambda x: x ** 0.5
    return f"The square root of 56: {square_root(56)}"


@app.route("/B3F")
def B3F():
    """
    Ich kann Lambda-Ausdrücke schreiben, die mehrere Argumente verarbeiten können.
    """
    multiply = lambda a, b, c: a * b * c
    return f"multipliziere 5, 7 und 12 zusammen: {multiply(5, 7, 12)}"


@app.route("/B3E")
def B3E():
    """
    Ich kann Lambda-Ausdrücke verwenden, um den Programmfluss zu steuern, z.B. durch Sortieren von Listen basierend auf
    benutzerdefinierten Kriterien.
    """
    sort_by_length = lambda word: len(word)

    list_of_words = ["short", "ThisIsAVeryLongWordWithManyLetters", "NormalWord", "WordButLonger", "E"]

    sort_list = sorted(list_of_words, key=sort_by_length)

    return f"sorted list: {sort_list}<br>original list: {list_of_words}"


@app.route("/B4G")
def B4G():
    """
    Ich kann die Funktionen Map, Filter und Reduce einzeln auf Listen anwenden.
    """
    numbers = [1, 2, 3, 4, 5, 6]

    square_list = list(map(lambda x: x ** 2, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    sum_of_list = reduce(lambda x, y: x + y, numbers)

    return f"list of numbers = {numbers}<br>square each value with a map function: {square_list}<br>only a list of even numbers with filter: {even_numbers}<br>sum of all list elements with reduce function {sum_of_list}"


@app.route("/B4F")
def B4F():
    """
    Ich kann Map, Filter und Reduce kombiniert verwenden, um Daten zu verarbeiten und zu manipulieren, die komplexere
    Transformationen erfordern.
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    result = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))

    return f"List of numbers: {numbers}<br>Combined function (sum of the square of all odd numbers): {result}"


@app.route("/B4E")
def B4E():
    """
    Ich kann Map, Filter und Reduce verwenden, um komplexe Datenverarbeitungsaufgaben zu lösen, wie z.B. die Aggregation
    von Daten oder die Transformation von Datenstrukturen.
    """
    students = [
        ("Bucac", 18, 4.7),
        ("Bobin", 19, 5),
        ("AⱯA", 18, 4.25),
        ("Ferrari", 18, 5.1),
        ("Nichtola", 17, 6.0)
    ]

    avg_grade = reduce(lambda x, y: x + y, map(lambda student: student[2], filter(lambda student: student[1] >= 18, students))) / len(students)

    return f"List of students: {students}<br>Average grade of the adult students: {avg_grade}"


@app.route("/C1G")
def C1G():
    """
    Ich kann einige Refactoring-Techniken aufzählen, die einen Code lesbarer und verständlicher machen.
    """
    return "For this part of the competences I don't not think a code example is possible, therefore I kindly ask of " \
           "you to follow <a href='/doc'>this link</a> which will redirect you to the documentation (Lernnachweis) " \
           "of this project"


@app.route("/C1F")
def C1F():
    """
    Ich kann mit Refactoring-Techniken einen Code lesbarer und verständlicher machen.
    """
    return "For this part of the competences I don't not think a code example is possible, therefore I kindly ask of " \
           "you to follow <a href='/doc'>this link</a> which will redirect you to the documentation (Lernnachweis) " \
           "of this project"


@app.route("/C1E")
def C1E():
    """
    Ich kann die Auswirkungen des Refactorings auf das Verhalten des Codes einschätzen und sicherstellen, dass das
    Refactoring keine unerwünschten Nebeneffekte hat.
    """
    return "For this part of the competences I don't not think a code example is possible, therefore I kindly ask of " \
           "you to follow <a href='/doc'>this link</a> which will redirect you to the documentation (Lernnachweis) " \
           "of this project"


if __name__ == '__main__':
    app.run(debug=True)
