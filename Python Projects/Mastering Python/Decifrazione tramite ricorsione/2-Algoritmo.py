# -*- coding: utf-8 -*-

def is_quasi_anagram(original_word, other_word):
    # Verifica se 'other_word' è un "quasi-anagramma" di 'original_word'.
    # Un quasi-anagramma è una parola che può essere formata da un anagramma di 'original_word'
    # con un solo carattere extra.
    if len(original_word) + 1 != len(other_word):  # La lunghezza deve essere +1
        return False
    for letter in original_word:
        if letter not in other_word:  # Verifica che ogni lettera di 'original_word' sia in 'other_word'
            return False
        other_word = other_word.replace(letter, '', 1)  # Rimuove una copia della lettera trovata
    if len(other_word) == 1:  # Se rimane un solo carattere extra, è un quasi-anagramma
        return True
    return False


def find_quasi_anagrams(encrypted_text, original_word):
    # Trova tutte le occorrenze di "quasi-anagrammi" di 'original_word' nel testo
    indexes = []
    for i in range(len(encrypted_text)):
        for j in range(i + 1, len(encrypted_text) + 1):  # Itera su tutte le sottosequenze
            current_word = encrypted_text[i:j]
            if is_quasi_anagram(original_word, current_word):  # Verifica se è un quasi-anagramma
                indexes.append((i, j))  # Memorizza gli indici dove si trova la sottosequenza
    return indexes


def recursive_step(encrypted_text, pharaohs_cypher, current_set):
    # Applica ricorsivamente il cifrario a tutte le possibili trasformazioni
    for key, value in pharaohs_cypher.items():
        # Trova tutte le posizioni in cui il "quasi-anagramma" di 'key' è presente nel testo
        indexes = find_quasi_anagrams(encrypted_text, key)

        for index in indexes:
            i, j = index

            new_string = encrypted_text[:i] + value + encrypted_text[j:]  # Sostituisce con il valore

            new_set = recursive_step(new_string, pharaohs_cypher, set())  # Chiamata ricorsiva

            current_set.add(new_string)  # Aggiunge la nuova stringa al set di risultati

            current_set = current_set.union(new_set)  # Unisce i risultati ottenuti ricorsivamente

    return current_set


def pharaohs_revenge(encrypted_text: str, pharaohs_cypher: dict[str, str]) -> set[str]:
    # Avvia il processo ricorsivo per ottenere tutte le sequenze finali
    final_set = recursive_step(encrypted_text, pharaohs_cypher, set())
    
    # Trova la lunghezza minima tra tutte le sequenze finali
    min_length = min([len(word) for word in final_set])
    
    # Filtra per mantenere solo le sequenze più corte
    final_set = set([word for word in final_set if len(word) == min_length])
    
    return final_set


if __name__ == '__main__':

    # Test del programma con un esempio
    encrypted_text = 'astronaut-flying-cyrcus'
    pharaohs_cypher = {'tuar': 'me', 'cniy': 'op',
                       'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}
    result = pharaohs_revenge(encrypted_text, pharaohs_cypher)

    print(f"Result is {result}")  # Stampa il risultato
