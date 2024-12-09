# -*- coding: utf-8 -*-

import images


def take_tile(image, tile_size, row, col):
    '''
    Restituisce il tassello di dimensione tile_size
    in posizione row, col dell'immagine image
    '''
    tile = []
    row = row * tile_size  # Calcola la posizione di inizio riga del tassello
    col = col * tile_size  # Calcola la posizione di inizio colonna del tassello
    for i in range(row, row+tile_size):  # Scorre le righe del tassello
        tile.append(image[i][col:col+tile_size])  # Aggiunge i pixel del tassello
    return tile


def rotate_tile(tile):
    """
    Ritorna l'immagine ruotata di 90 gradi in senso orario
    """
    heigth = len(tile)  # Ottiene l'altezza del tassello
    width = len(tile[0])  # Ottiene la larghezza del tassello
    # Crea una nuova immagine di dimensioni invertite
    new_image = [[0 for _ in range(heigth)] for _ in range(width)]
    for y in range(heigth):  # Scorre le righe del tassello
        for x in range(width):  # Scorre le colonne del tassello
            # Esegue la rotazione 90° in senso orario
            new_image[y][width - 1 - x] = tile[x][y]  # Mappa i pixel ruotati
    return new_image


def compute_key(puzzle_image, plain_image, tile_size):
    '''
    Confronta le immagini dei tasselli ruotati con quelli originali
    e restituisce la chiave di cifratura sotto forma di rotazioni.
    '''
    rotations = ["N", "R", "F", "L"]  # Le rotazioni possibili: nessuna, 90° a destra, flip, 90° a sinistra
    tile_in_row = len(puzzle_image) // tile_size  # Calcola il numero di tasselli per riga
    tile_in_col = len(puzzle_image[0]) // tile_size  # Calcola il numero di tasselli per colonna
    key = []  # Lista per memorizzare la chiave

    for row in range(tile_in_row):  # Scorre le righe dei tasselli
        for col in range(tile_in_col):  # Scorre le colonne dei tasselli
            # Estrae i tasselli dalle immagini originale e cifrata
            plain_tile = take_tile(plain_image, tile_size, row, col)
            puzzle_tile = take_tile(puzzle_image, tile_size, row, col)
            for rotation in rotations:  # Prova le diverse rotazioni
                if plain_tile == puzzle_tile:  # Se il tassello corrisponde senza rotazioni
                    key.append(rotation)  # Aggiungi la rotazione alla chiave
                    break  # Esci dal ciclo delle rotazioni
                puzzle_tile = rotate_tile(puzzle_tile)  # Ruota il tassello di 90° a destra

    clean_key = []  # Lista per la chiave pulita organizzata in righe
    row = ""  # Variabile temporanea per costruire le righe della chiave
    # Organizza la chiave in righe
    for char in key:
        row += char  # Aggiungi la rotazione alla riga corrente
        if len(row) % tile_in_col == 0:  # Se la riga è completa
            clean_key.append(row)  # Aggiungi la riga alla chiave finale
            row = ""  # Resetta la riga per la successiva
    return key, clean_key  # Restituisce la chiave completa e la chiave formattata


def decrypt(sentence, key):
    '''
    Decifra il testo utilizzando la chiave di cifratura.
    '''
    for i, char in enumerate(sentence):  # Scorre ogni carattere nel testo cifrato
        key_char = key[i % len(key)]  # Ottiene il carattere corrispondente della chiave
        if key_char != "F":  # Se la rotazione non è un flip
            sentence[i] = apply_key(char, key_char)  # Applica la rotazione al carattere
        else:  # Se la rotazione è un flip
            if i == len(sentence) - 1:  # Se siamo all'ultimo carattere
                sentence[i] = sentence[0]  # Scambia con il primo carattere
                sentence[0] = char  # Mette il carattere corrente al primo
            else:  # Se non siamo all'ultimo carattere
                sentence[i] = sentence[i+1]  # Scambia il carattere con il successivo
                sentence[i+1] = char  # Mette il carattere corrente nel successivo
    return sentence


def apply_key(char, key_char):
    '''
    Applica la rotazione al singolo carattere in base alla chiave.
    '''
    if key_char == "N":  # Nessuna rotazione
        return char
    elif key_char == "R":  # Rotazione a destra (incremento del carattere)
        return chr(ord(char) + 1)
    elif key_char == "L":  # Rotazione a sinistra (decremento del carattere)
        return chr(ord(char) - 1)


def jigsaw(puzzle_image: str, plain_image: str, tile_size: int, encrypted_file: str, plain_file: str) -> list[str]:
    '''
    Funzione principale che carica le immagini, calcola la chiave e decifra il file.
    '''
    # Carica le immagini da file
    plain_image = images.load(plain_image)
    puzzle_image = images.load(puzzle_image)
    
    # Calcola la chiave di cifratura confrontando le immagini
    key, clean_key = compute_key(puzzle_image, plain_image, tile_size)

    # Carica il file cifrato e lo decifra
    with open(encrypted_file, "r") as f:
        sentence = list(f.read())  # Legge il file come una lista di caratteri
    sentence = decrypt(sentence, key)  # Decifra la lista di caratteri
    sentence = "".join(sentence)  # Converte la lista in una stringa

    # Salva il file decifrato
    with open(plain_file, "w") as f:
        f.write(sentence)
    
    return clean_key  # Restituisce la chiave pulita
  

if __name__ == '__main__':
   pass