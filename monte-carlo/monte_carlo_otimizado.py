import random
import time
import multiprocessing as mp

def calcular_pi():
    ini = time.time()
    rep = 10000000
    acertos = 0
    for _ in range(rep):
        x = random.random()
        y = random.random()
        
        if (x * x) + (y * y) <= 1.0:
            acertos += 1
        
    fim = time.time()
    print(4 * acertos / rep)
    print(fim-ini)

if __name__ == "__main__":
    proc = mp.Process(target=calcular_pi,)
    proc.start()
    proc.join()

