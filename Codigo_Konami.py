#  * Crea un programa que detecte cuando el famoso "Código Konami" se ha
#  * introducido correctamente desde el teclado.
#  * Si sucede esto, debe notificarse mostrando un mensaje en la terminal.

from pynput import keyboard as kb


def detectar_tecla(tecla):
    print(f"Tecla: {str(tecla)}")


def soltar_tecla(tecla):
    if tecla == kb.KeyCode.from_char("+"):
        print("Finalizado.")
        return False


kb.Listener(detectar_tecla, soltar_tecla).run()
