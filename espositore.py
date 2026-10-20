class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice=codice
        self.nome=nome
        self.cognome=cognome
        self.stand_assegnato=None

    def __str__(self):
        return f"{self.codice} {self.nome} {self.cognome}"

    def __repr__(self):
        return f"Espositore('{self.codice}', '{self.nome}', '{self.cognome}')"