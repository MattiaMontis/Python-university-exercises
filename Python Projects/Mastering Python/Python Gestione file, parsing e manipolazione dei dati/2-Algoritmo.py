import os

# Funzione per tradurre le note Tarahumara in notazione Umkansaniana
def translate_song(song_lines):
    translation_dict = {
        "0": "A",  # A Tarahumara note
        "1": "B",  # B Tarahumara note
        "2": "C",  # C Tarahumara note
        "3": "D",  # D Tarahumara note
        "4": "E",  # E Tarahumara note
        "5": "F",  # F Tarahumara note
        "6": "G",  # G Tarahumara note
        "7": "H",  # H Tarahumara note
        "-": "b",  # Flat note
        "+": "#",  # Sharp note
        " ": "P",  # Pause
    }

    translated_song = ""
    for line in song_lines:
        # Itero sulla partitura, partendo dalla fine di ogni riga
        for i in range(len(line)-1, -1, -1):
            translated_song += translation_dict[line[i]]
    return translated_song


# Funzione per aggiungere la durata delle note nella traduzione
def insert_durations(translated_song):
    list_notes = []
    curr_note = ""
    for i in range(len(translated_song)):
        curr_note = translated_song[i]
        if curr_note in ["b", "#"]:  # Ignoro il carattere di alterazione
            continue
        if i + 1 < len(translated_song) and translated_song[i + 1] in ["b", "#"]:
            curr_note += translated_song[i + 1]  # Aggiungo il bemolle o diesis alla nota
        list_notes.append(curr_note)

    correct = ""
    list_notes = list_notes[::-1]  # Invertiamo la lista per trattare la partitura da destra a sinistra
    curr_char = list_notes.pop()
    count = 1
    while len(list_notes) > 0:
        if curr_char == list_notes[-1]:  # Se la nota è uguale alla precedente, incremento la durata
            count += 1
            curr_char = list_notes.pop()
        else:
            correct += curr_char + str(count)  # Altrimenti aggiungo la nota con la durata
            count = 1
            curr_char = list_notes.pop()
    return correct + curr_char + str(count)


# Funzione per calcolare la durata totale del brano
def get_song_duration(song):
    total_sum = 0
    current_number = ""

    for char in song:
        if char.isalpha():  # Se è una nota
            if current_number:
                total_sum += int(current_number)  # Aggiungo la durata accumulata
                current_number = ""
        elif char.isdigit():  # Se è un numero (la durata)
            current_number += char

    if current_number:
        total_sum += int(current_number)  # Aggiungo l'ultima durata

    return total_sum


# Funzione principale per tradurre e organizzare i brani musicali
def Umkansanize(source_root: str, target_root: str) -> dict[str, int]:
    # Leggo l'indice dei brani da tradurre
    index_path = os.path.join(source_root, "index.txt")
    with open(index_path, "r") as f:
        songs = f.read().split("\n")

    # Itero sui brani da tradurre
    final_index = {}
    for song_info in songs:
        if song_info == "":
            continue
        song_name, song_path = song_info.split('" "')
        song_name = song_name.replace('"', '')
        song_path = song_path.replace('"', '')

        # Leggo il contenuto della canzone
        absolute_song_path = os.path.join(source_root, song_path)
        with open(absolute_song_path, "r") as f:
            song = f.read()
        song_lines = song.split("\n")
        translated_song = translate_song(song_lines)

        # Aggiungo le durate alle note
        translated_song = insert_durations(translated_song)

        # Calcolo la durata totale del brano
        song_duration = get_song_duration(translated_song)

        final_index[song_name] = song_duration

        # Creo le directories necessarie per salvare il brano tradotto
        target_song_path = os.path.join(target_root, song_path)
        target_song_dir = os.path.dirname(target_song_path)
        os.makedirs(target_song_dir, exist_ok=True)

        # Salvo il brano tradotto nella cartella corretta
        with open(os.path.join(target_song_dir, f"{song_name}.txt"), "w+") as f:
            f.write(translated_song)

    # Ordino l'indice in base alla durata e al nome
    final_index_items = sorted(
        final_index.items(), key=lambda x: (-x[1], x[0]))

    # Salvo l'indice ordinato
    with open(os.path.join(target_root, "index.txt"), "w") as f:
        for song_name, song_duration in final_index_items:
            f.write(f'"{song_name}" {song_duration}\n')

    return final_index
