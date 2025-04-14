import threading
import time

def contar_numeros():
    for i in range(1, 11):
        print(f"Número: {i}")
        time.sleep(0.5)

def imprimir_letras():
    for letra in "ABCDEFGHIJ":
        print(f"Letra: {letra}")
        time.sleep(0.5)

# Criando as threads
thread1 = threading.Thread(target=contar_numeros)
thread2 = threading.Thread(target=imprimir_letras)

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando a finalização das threads
thread1.join()
thread2.join()

print("Fim do programa.")

# Modificando para inserir mais duas
import threading
import time

def contar_numeros():
    for i in range(1, 11):
        print(f"Número: {i}")
        time.sleep(0.5)

def imprimir_letras():
    for letra in "ABCDEFGHIJ":
        print(f"Letra: {letra}")
        time.sleep(0.5)

def contar_pares():
    for i in range(2, 21, 2):
        print(f"Par: {i}")
        time.sleep(0.5)

def imprimir_simbolos():
    for simbolo in "!@#$%^&*()":
        print(f"Símbolo: {simbolo}")
        time.sleep(0.5)

# Criando as threads
thread1 = threading.Thread(target=contar_numeros)
thread2 = threading.Thread(target=imprimir_letras)
thread3 = threading.Thread(target=contar_pares)
thread4 = threading.Thread(target=imprimir_simbolos)

# Iniciando as threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Aguardando a finalização das threads
thread1.join()
thread2.join()
thread3.join()
thread4.join()

print("Fim do programa.")