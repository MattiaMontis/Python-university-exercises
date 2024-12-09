class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.children = []

    def lista_nodi(self) -> str:
        def _crea_lista_nodi(radice, nodi=[]):
            nodi.append(radice.valore)
            for child in radice.children:
                _crea_lista_nodi(child, nodi)
            return nodi
        nodi = _crea_lista_nodi(self)
        return nodi

    def __repr__(self):
        return f"{self.valore}"

    def __str__(self):
        return self.__repr__()

    def add_chidlren(self, *nodi):
        for nodo in nodi:
            self.children.append(nodo)


def costruisci_albero_esercizio():
    radice = Nodo(5)
    nodo_2 = Nodo(-10)
    nodo_3 = Nodo(2)
    nodo_4 = Nodo(-3)
    nodo_5 = Nodo(11)
    nodo_6 = Nodo(4)
    nodo_7 = Nodo(3)
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


def rimuovi_nodo(radice, valore):
    """
    Si implementi una funzione rimuovi_nodo(tree, valore) che prende in input
    l'albero ed il valore di un nodo. Modifica l'albero in maniera distruttiva
    in modo da rimuovere tutti i nodi che hanno il valore valore, rimuovendo
    anche i rispettivi figli.

    Esempio:

    L'abero costruito da costruisci_albero_esercizio() è il seguente:
              5                       
      ________|_____________         
     |          |           |       
    -10         2           -3      
     |     _____|______           
     11   |   |  |  |  |         
          4   3 -1 -4  7        
            __|__              
           |     |            
           3     1           

    La funzione rimuovi_nodo(tree, 2) modifica l'albero in maniera distruttiva
    in modo da ottenere

              5                       
      ________|_____________         
     |                     |       
    -10                    -3      
     |                
     11   

    ---------------------------------------

    Mentre La funzione rimuovi_nodo(tree, 3) modifica l'albero in maniera distruttiva
    in modo da ottenere

              5                       
      ________|_____________         
     |          |           |       
    -10         2           -3      
     |     _____|______           
     11   |     |  |  |         
          4    -1 -4  7        

    """
    # Implementa la funzione
    pass


if __name__ == "__main__":
    albero = costruisci_albero_esercizio()
    rimuovi_nodo(albero, 2)

    nodi_corretti = [5, -10, 11, -3]
    if albero.lista_nodi() != nodi_corretti:
        print(
            f'RIMOZIONE NODO 2: La lista dei nodi è errata. \n La lista corretta è {nodi_corretti} \n La lista generata è {albero.lista_nodi()}')
    else:
        print("La lista dei nodi dopo aver rimosso il nodo 2 è corretta")

    albero = costruisci_albero_esercizio()
    rimuovi_nodo(albero, 3)

    nodi_corretti = [5, -10, 11, 2, 4, -1, -4, 7, -3]
    if albero.lista_nodi() != nodi_corretti:
        print(
            f'RIMOZIONE NODO 3: La lista dei nodi è errata. \n La lista corretta è {nodi_corretti} \n La lista generata è {albero.lista_nodi()}')
    else:
        print("La lista dei nodi dopo aver rimosso il nodo 3 è corretta")
