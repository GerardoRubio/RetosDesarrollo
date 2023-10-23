# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

def anagrama(texto1, texto2):

    if len(texto1) == len(texto2):
        lista1 = list(texto1)
        lista2 = list(texto2)

        print(lista1, lista2)
        lista1.sort()
        lista2.sort()
        print(lista1, lista2)

        if lista1 != lista2:
            return False
    else:
        return False
    return True


palabra1 = input("Palabra 1: ")
palabra2 = input("Palabra 2: ")

palabra1 = palabra1.lower()
palabra2 = palabra2.lower()

resultado = anagrama(palabra1, palabra2)
print(f"¿Es un anagrama? {resultado}")
