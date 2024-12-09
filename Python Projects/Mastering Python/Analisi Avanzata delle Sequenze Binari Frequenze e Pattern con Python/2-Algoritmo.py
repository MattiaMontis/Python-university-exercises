# -*- coding: utf-8 -*-

def count_binary_sequences(sequence, min_len, max_len):
    sequences = {}
    seq_len = len(sequence)
    # Itero su tutte le lunghezze di sottosequenze
    for step in range(min_len, max_len + 1):
        # Itero su tutti gli indici da dove iniziare a prendere la sottosequenza
        for i in range(seq_len):
            # Se la sottosequenza esce fuori dalla sequenza, la ignoro e finisco il ciclo
            if i + step > seq_len:
                break
            # La sottosequenza è la sottostringa che va dall'indice i all'indice i + step
            subseq = sequence[i: i + step]
            # Se è la prima volta che vedo la sottosequenza, la aggiungo al dizionario
            if subseq not in sequences:
                sequences[subseq] = 1
            # Altrimenti incremento il contatore
            else:
                sequences[subseq] += 1
    return sequences


def ex1(ftesto, a, b, n):
    with open(ftesto,  "r") as f:
        sequence = f.read().replace('\n', '')

    sequences = count_binary_sequences(sequence, a, b)

    max_count = max(sequences.values())

    # Inverto il dizionario, in modo da avere come chiave la frequenza e come valore la lista di sottosequenze
    inverted_sequence_count = {}
    for i in range(1, max_count+1):
        for key, value in sequences.items():
            if value == i:
                if value not in inverted_sequence_count:
                    inverted_sequence_count[value] = []
                inverted_sequence_count[value].append(key)

    # Ordino in maniera lessicografica le liste di sottosequenze
    for key, value in inverted_sequence_count.items():
        inverted_sequence_count[key] = sorted(value)

    # Ordino gli elementi del dizionario in base alla chiave
    seq_count_items = sorted(
        inverted_sequence_count.items(), key=lambda x: x[0])

    # Prendo solamente gli n elementi con frequenza maggiore
    top_n_items = seq_count_items[-n:]

    return top_n_items


if __name__ == '__main__':
    pass
