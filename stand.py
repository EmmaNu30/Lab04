class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice=codice
        self.superficie=int(superficie)
        self.padiglione=int(padiglione)
        self.prezzo_base=float(prezzo_base)
        self.espositore=None
        self.disponibile=True

    def calcola_prezzo(self):
        return self.prezzo_base

    def __lt__(self, other):
        return self.calcola_prezzo() < other.calcola_prezzo()

    def __str__(self):
        if self.disponibile:
            stato="Disponibile"
        else:
            stato=f"Assegnato a {self.espositore.codice}"
        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"


class StandPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.numero_prese=int(numero_prese)

    def calcola_prezzo(self):
        return self.prezzo_base * (1 + 0.07 * self.numero_prese)

    def __str__(self):
        if self.disponibile:
            stato="Disponibile"
        else:
            stato=f"Assegnato a {self.espositore.codice}"
        return f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive: {self.numero_prese} - {stato}"


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione=posizione

    def calcola_prezzo(self):
        return self.prezzo_base * 1.30

    def __str__(self):
        if self.disponibile:
            stato="Disponibile"
        else:
            stato=f"Assegnato a {self.espositore.codice}"
        return f"{self.codice}: Premium ({self.posizione}) | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"