#  * Crea un programa que realize el cifrado César de un texto y lo imprima.
#  * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#  *
#  * Te recomiendo que busques información para conocer en profundidad cómo
#  * realizar el cifrado. Esto también forma parte del reto.

def indice_positivo(indice: int):
    if indice == 26:
        return 1
    elif indice == 27:
        return 2
    else:
        return 3


def indice_negativo(indice: int):
    if indice == 3:
        return 28
    elif indice == 2:
        return 27
    else:
        return 26


def cifrar(texto: str):
    diccionario = {"1": "a", "2": "b", "3": "c", "4": "d",
                   "5": "e", "6": "f", "7": "g", "8": "h",
                   "9": "i", "10": "j", "11": "k", "12": "l",
                   "13": "ll", "14": "m", "15": "n", "16": "ñ",
                   "17": "o", "18": "p", "19": "q", "20": "r",
                   "21": "s", "22": "t", "23": "u", "24": "v",
                   "25": "w", "26": "x", "27": "y", "28": "z"}
    palabra_cifrada = ""
    llave_int = 0
    llave_str = ""

    for letra in texto:
        for llave, valor in diccionario.items():

            if valor == letra:
                llave_int = int(llave)

                if llave_int >= 26 and llave_int <= 28:
                    llave_int = indice_positivo(llave_int)
                    llave_str = str(llave_int)
                    palabra_cifrada = palabra_cifrada + diccionario[llave_str]
                else:
                    llave_int = llave_int + 3
                    llave_str = str(llave_int)
                    palabra_cifrada = palabra_cifrada + diccionario[llave_str]
    return palabra_cifrada


def descifrar(texto: str):
    diccionario = {"1": "a", "2": "b", "3": "c", "4": "d",
                   "5": "e", "6": "f", "7": "g", "8": "h",
                   "9": "i", "10": "j", "11": "k", "12": "l",
                   "13": "ll", "14": "m", "15": "n", "16": "ñ",
                   "17": "o", "18": "p", "19": "q", "20": "r",
                   "21": "s", "22": "t", "23": "u", "24": "v",
                   "25": "w", "26": "x", "27": "y", "28": "z"}
    palabra_descifrada = ""
    llave_int = 0
    llave_str = ""

    for letra in texto:
        for llave, valor in diccionario.items():

            if valor == letra:
                llave_int = int(llave)

                if llave_int >= 1 and llave_int <= 3:
                    llave_int = indice_negativo(llave_int)
                    llave_str = str(llave_int)
                    palabra_descifrada = palabra_descifrada + \
                        diccionario[llave_str]
                else:
                    llave_int = llave_int - 3
                    llave_str = str(llave_int)
                    palabra_descifrada = palabra_descifrada + \
                        diccionario[llave_str]
    return palabra_descifrada


palabra = "zorra"
resultado = ""
palabra = palabra.lower()

resultado = cifrar(palabra)
print(resultado)

resultado = descifrar(resultado)
print(resultado)
