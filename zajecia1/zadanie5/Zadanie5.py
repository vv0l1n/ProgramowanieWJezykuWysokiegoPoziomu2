from abc import abstractmethod, ABC


class Komunikacja:
    @abstractmethod
    def wyslij_wiadomosc(self, odbiorca, tresc):
        pass

class Rozrywka:
    @abstractmethod
    def odtworz_muzyke(self, utwor):
        pass

class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent


class Smartphone(Telefon, Rozrywka, Komunikacja, ABC):
    def __init__(self, model, producent):
        super().__init__(model, producent)

    def wyslij_wiadomosc(self, odbiorca, tresc):
        print(f"Wiadomość '{tresc}' wysłana do: {odbiorca}")

    def odtworz_muzyke(self, utwor):
        print(f"Odtwarzam utwór: {utwor}")

phone = Smartphone("iPhone 16 Pro", "Apple")

phone.odtworz_muzyke("Nokia ringtone")
phone.wyslij_wiadomosc("Kurier", "Proszę zostawić paczkę pod drzwiami")