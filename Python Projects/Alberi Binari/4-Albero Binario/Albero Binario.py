class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.children = []

    def add_chidlren(self, *nodi):
        for nodo in nodi:
            self.children.append(nodo)

    def __repr__(self):
        return f"{self.valore}"


def costruisci_albero_esercizio():
    radice = Nodo(5)
    nodo_2 = Nodo(-10)
    nodo_3 = Nodo(2)
    nodo_4 = Nodo(-3)
    nodo_5 = Nodo(11)
    nodo_6 = Nodo(4)
    nodo_7 = Nodo(2)
    nodo_8 = Nodo(-1)
    nodo_9 = Nodo(-4)
    nodo_10 = Nodo(7)
    nodo_11 = Nodo(3)
    nodo_12 = Nodo(1)

    radice.add_chidlren(nodo_2, nodo_3, nodo_4)
    nodo_2.add_chidlren(nodo_5)
    nodo_3.add_chidlren(nodo_6, nodo_7, nodo_8, nodo_9, nodo_10)
    nodo_7.add_chidlren(nodo_11, nodo_12)

    return radice


def somma_nodi(tree, somma=0):
    """
    La funzione somma i valori positivi dei nodi nell'albero.
    """
    # Se il valore del nodo è positivo, aggiungilo alla somma
    if tree.valore > 0:
        somma += tree.valore
    
    # Per ogni nodo figlio, chiama ricorsivamente la funzione
    for child in tree.children:
        somma = somma_nodi(child, somma)
    
    return somma


if __name__ == "__main__":
    radice = costruisci_albero_esercizio()
    risultato = somma_nodi(radice)
    somma_corretta = 35
    assert risultato == somma_corretta, f"""
    Somma errata:
    La somma da te generata: {risultato}
    La somma corretta: {somma_corretta}
    """
    print(f"La somma dei nodi non negativi è {risultato}, il risultato è corretto")
")
