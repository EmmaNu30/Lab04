import csv
from stand import Stand, StandPrese, StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome=nome
        self.stand={}
        self.espositori={}

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome=nuovo_nome.strip()

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader=csv.reader(file)
                for riga in reader:
                    if not riga:
                        continue

                    codice=riga[0].strip()

                    if codice.startswith("ST"):
                        superficie=riga[1].strip()
                        padiglione=riga[2].strip()
                        prezzo_base=riga[3].strip()

                        if len(riga) == 4:
                            nuovo_stand=Stand(codice, superficie, padiglione, prezzo_base)
                        elif len(riga) == 5:
                            campo_extra=riga[4].strip()

                            if campo_extra.isdigit():
                                nuovo_stand=StandPrese(codice, superficie, padiglione, prezzo_base, campo_extra)
                            else:
                                nuovo_stand=StandPremium(codice, superficie, padiglione, prezzo_base, campo_extra)

                        self.stand[codice]=nuovo_stand

                    elif codice.startswith("ES"):
                        nome=riga[1].strip()
                        cognome=riga[2].strip()
                        nuovo_espositore=Espositore(codice, nome, cognome)
                        self.espositori[codice]=nuovo_espositore

        except FileNotFoundError:
            raise FileNotFoundError(f"Il file '{file_path}' non esiste")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.stand:
            raise Exception(f"Lo stand '{codice_stand}' non esiste nel sistema")

        if codice_espositore not in self.espositori:
            raise Exception(f"L'espositore '{codice_espositore}' non esiste nel sistema")

        stand_obj=self.stand[codice_stand]
        espositore_obj=self.espositori[codice_espositore]

        if not stand_obj.disponibile:
            raise Exception(f"Lo stand '{codice_stand}' è già stato assegnato")

        if espositore_obj.stand_assegnato is not None:
            raise Exception(f"L'espositore '{codice_espositore}' ha già uno stand assegnato")

        stand_obj.disponibile=False
        stand_obj.espositore=espositore_obj
        espositore_obj.stand_assegnato=stand_obj

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for esp in self.espositori.values():
            if esp.stand_assegnato:
                print(f"{esp} Stand assegnato: {esp.stand_assegnato.codice}")
            else:
                print(f"{esp} Nessuno stand assegnato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        lista_stand = list(self.stand.values())
        return sorted(lista_stand)
