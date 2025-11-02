import pylrc
import time
import sys


def mostrar_lyrics_sincronizadas(archivo_lrc):
    # Leer el archivo .lrc
    try:
        with open(archivo_lrc, 'r', encoding='utf-8') as f:
            lrc_string = f.read()
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo_lrc}' no encontrado.")
        return
    except Exception as e:
        print(f"Error al leer: {e}")
        return

    # Parsear
    lyrics = pylrc.parse(lrc_string)
    if not lyrics:
        print("Archivo .lrc vacío.")
        return

    print("¡Iniciando Cancion! Ctrl+C para parar.\n")
    time.sleep(1)

    prev_time = 0.0
    for line in lyrics:
        current_time = line.time
        sleep_time = current_time - prev_time
        if sleep_time > 0:
            time.sleep(sleep_time)

        sys.stdout.write("\r" + " " * 80)
        sys.stdout.write("\r" + line.text)
        sys.stdout.flush()
        print()

        prev_time = current_time

    print("\nFin canción!")


if __name__ == "__main__":
    archivo = 'on_melancholy_hill.lrc'
    mostrar_lyrics_sincronizadas(archivo)


