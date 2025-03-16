import json

class AplikacjaMobilna:
    liczba_pobran = 0

    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

    def nowe_pobranie(self):
        AplikacjaMobilna.liczba_pobran += 1

    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran

    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as f:
            dane = json.load(f)
        return cls(dane['nazwa'], dane['wersja'])


app1 = AplikacjaMobilna.z_json('app1.json')
app2 = AplikacjaMobilna.z_json('app2.json')

app1.nowe_pobranie()
app1.nowe_pobranie()
app1.nowe_pobranie()
app1.nowe_pobranie()

app2.nowe_pobranie()
app2.nowe_pobranie()

print(AplikacjaMobilna.ile_pobran())