class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return "Opis ksiazki"

    def __str__(self):
        return f"Autor: {self.autor}, rok wydania: {self.rok_wydania}, tytul: {self.tytul}"

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return f"Rozmiar pliku: {self.rozmiar_pliku}MB"

class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania

    def opis(self):
        return f"Czas trwania: {self.czas_trwania} minut"

a1 = Audiobook("Audiobook 1", "Jan Kowalski", 2015, 15)
a2 = Audiobook("Audiobook 2", "Jan Rzepecki", 2022, 45)

e1 = Ebook("Ebook 1", "Andrzej Grosicki", 2000, 10)
e2 = Audiobook("Ebook 2", "Robert Lewandowski", 1931, 159)

print(a1)
print(a1.opis())
print(a2)
print(a2.opis())
print(e1)
print(e1.opis())
print(e2)
print(e2.opis())