 import random

def dibujar_golosa(intentos):
    golosa = [
        "   -----   ",
        " /       \\ ",
        " |       | ",
        " \\       / ",
        "   -----   "
    ]
    
    if intentos == 0:
        golosa[2] = " |       O "
    elif intentos == 1:
        golosa[1] = " |       | "
    elif intentos == 2:
        golosa[1] = " |      /| "
    elif intentos == 3:
        golosa[1] = " |      /|\\"
    elif intentos == 4:
        golosa[3] = " \\       | "
    elif intentos == 5:
        golosa[3] = " \\      /| "
    elif intentos == 6:
        golosa[3] = " \\      /|\\"
    
    for linea in golosa:
        print(linea)

def dibujar_cara_feliz():
    cara_feliz = [
        "   \\ˆˆˆˆˆˆˆ/",
        "  |  O O  |",
        "  |   ∆   |",
        "   \\___/"
    ]
    
    for linea in cara_feliz:
        print(linea)


def dibujar_calavera():
    calavera = [
        "    .-''-.",
        "   /       \\",
        "  |         |",
        "  |  R.I.P.  |",
        "  |         |",
        "   \\       /",
        "    `'---'`"
    ]
    
    for linea in calavera:
        print(linea)

def jugar_golosa():
    objetivo = random.randint(1, 25)
    intentos = 0
    
    