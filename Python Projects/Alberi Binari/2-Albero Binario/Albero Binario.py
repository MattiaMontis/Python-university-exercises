import albero

def es1(tree):
    """
    Data la radice "tree" di un albero binario, ritorna una lista in cui
    ogni elemento corrisponde alla somma dei valori all'i-esimo livello
    dell'albero.
    """
    if not tree:
        return []

    # Coda per la BFS, inizializzata con la radice
    queue = [tree]
    result = []

    while queue:
        # Per ogni livello, sommiamo i valori
        level_sum = 0
        level_size = len(queue)  # Numero di nodi nel livello corrente
        
        # Esploriamo tutti i nodi al livello corrente
        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.id  # Somma il valore del nodo
            queue.extend(node.f)  # Aggiungi i figli alla coda

        # Aggiungi la somma del livello corrente al risultato
        result.append(level_sum)

    return result
