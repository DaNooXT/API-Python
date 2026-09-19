from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests

def trabalhar(numero):
    max_tentatives = 5

    print(f"Iniciando tarefa {numero}")

    for tentative in range(max_tentatives):
        try:
            pass

            if numero == 3:
                    raise ValueError("Erro na tarefa 3")
            
        except requests.Timeout:
            pass

    time.sleep(2)

    return f"Tarefa {numero} concluída"


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []

    for numero in range(1, 6):
        future = executor.submit(trabalhar, numero)
        futures.append(future)

    for future in as_completed(futures):
        try:
            resultado = future.result()
            print(resultado)
            
        except Exception as e:
            print(f"Erro: {e}")