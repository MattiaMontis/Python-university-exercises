import random
import modules.images as images


def es2(path_immagine, save_path):
    """
    Si progetti una funzione che prende in input il percorso di un'immagine.

    Un pixel "valido" è un pixel di un determinato colore i cui vicini hanno
    TUTTI lo stesso colore. (Non considerare i pixel vicini in diagonale).
    Un pixel di colore NERO (0,0,0) è sempre NON valido.

    In particolare i pixel vicini sono quelli sopra, sotto, a destra e a
    sinistra.  Se un pixel si trova sul bordo, si considerino solo i pixel
    adiacenti che esistono. Questo vuol dire se un pixel si trova nell'angolo in
    alto a sinistra, allora basta che abbia lo stesso colore del pixel a destra
    e del pixel sotto per essere considerato valido.

    Si crei un dizionario in cui le chiavi sono i colori (la tupla r,g,b) dei
    pixel trovati sopra, e le chiavi una lista di coordinate del tipo (x,y) dei
    pixel validi di tale colore.  Ritornare gli items del dizionario ordinati a
    seconda della coordinata media dei pixel validi di un determinato colore, da
    sinistra a destra e, in caso di parità, dall'alto in basso.  Esempio: se il
    dizionario è {(10,1,12): [(10,0), (1,20)], (255,255,255): [(12,13), (1,9)]},

    la funzione ritorna [((255,255,255), [(1,9), (12,13)]), ((10,1,12): [(10,0),
    (1,20)])

    peché il punto medio del colore (255,255,255) è (6.5, 11) e il punto medio
    del colore (10,1,12) è (5.5, 10), quindi il secondo colore è più a sinistra
    del primo.

    - Salvare l'immagine colorando i pixel non validi di nero.
    """
    img = images.load(path_immagine)
    dizionario = {}
    valid_coords = []
    BLACK = (0, 0, 0)
    for y in range(len(img)):
        for x in range(len(img[0])):
            if img[y][x] != BLACK:
                color = img[y][x]
                neighbours = get_neighbours(img, x, y)
                for neighbour in neighbours:
                    xn, yn = neighbour
                    if img[yn][xn] != color:
                        break
                else:
                    valid_coords.append((x, y))
                    valid_coords.extend(neighbours)
                    if color not in dizionario:
                        dizionario[color] = [(x, y)]
                    else:
                        dizionario[color].append((x, y))

    items_ord = sorted(dizionario.items(), key=lambda x: (sum(
        [i[0] for i in x[1]])/len(x[1]), sum([i[1] for i in x[1]])/len(x[1])))

    for y in range(len(img)):
        for x in range(len(img[0])):
            if (x, y) not in valid_coords:
                img[y][x] = (0, 0, 0)
    images.save(img, save_path)

    return items_ord


def get_neighbours(img, x, y):
    """
    Funzione di utilità per ottenere i vicini di un pixel.
    """
    neighbours = []
    if y+1 < len(img):
        neighbours.append((x, y+1))
    if y-1 >= 0:
        neighbours.append((x, y-1))
    if x+1 < len(img[0]):
        neighbours.append((x+1, y))
    if x-1 >= 0:
        neighbours.append((x-1, y))
    return neighbours


def genera_immagine():
    """
    Funzione di utilità per generare le immagini di test. La lascio se sei curioso di vedere come funziona.
    """
    HEIGHT = 100
    WIDTH = 200
    BLACK = (0, 0, 0)
    img = [[BLACK for _ in range(WIDTH)] for _ in range(HEIGHT)]

    coord_pixel_validi = [(random.randint(
        0, HEIGHT - 1), random.randint(0, WIDTH - 1)) for _ in range(12)]

    pixel_noise = [(random.randint(0, HEIGHT - 1), random.randint(
        0, WIDTH - 1)) for _ in range(100)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (i, j) in coord_pixel_validi:
                img[i][j] = (random.randint(0, 255),
                             random.randint(0, 255), random.randint(0, 255))
            elif (i, j) in pixel_noise:
                img[i][j] = (random.randint(0, 255),
                             random.randint(0, 255), random.randint(0, 255))

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (i, j) in coord_pixel_validi:
                color = img[i][j]
                if i+1 < HEIGHT:
                    img[i+1][j] = color
                if i-1 >= 0:
                    img[i-1][j] = color
                if j+1 < WIDTH:
                    img[i][j+1] = color
                if j-1 >= 0:
                    img[i][j-1] = color

    images.save(img, "data/immagine_1.png")


def test_es2():
    risultato_corretto = [((249, 190, 65), [(6, 0)]), ((240, 250, 88), [(20, 56)]), ((246, 205, 41), [(28, 70)]), ((85, 27, 204), [(76, 60)]), ((123, 113, 156), [(82, 51)]), ((15, 122, 213), [(
        112, 32)]), ((79, 165, 162), [(118, 7)]), ((84, 5, 196), [(118, 56)]), ((90, 6, 6), [(120, 74)]), ((28, 32, 129), [(125, 91)]), ((146, 162, 128), [(163, 24)]), ((11, 3, 223), [(174, 88)])]
    risultato = es2("data/immagine_1.png", "data/immagine_1_validi.png")

    assert risultato == risultato_corretto, f"""
        Risultato corretto: {risultato_corretto}
        {"*" * 50}
        Risultato ottenuto: {risultato}

        IL RISULTATO NON È CORRETTO
        """

    img_prodotta = images.load("data/immagine_1_validi.png")
    img_corretta = images.load("data/immagine_1_validi_gt.png")

    assert img_prodotta == img_corretta, f"""
        L'immagine prodotta non è corretta.
        """

    print(f"La funzione è implementata correttamente.")


if __name__ == "__main__":
    test_es2()
