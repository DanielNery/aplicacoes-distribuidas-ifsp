import random
import time
ini = time.time()

rep = 10000000
acertos = 0
i = 0
while(i < rep):
    x = random.random()
    y = random.random()
    
    if (x * x) + (y * y) <= 1.0:
        acertos += 1
        
    i += 1

print(4 * acertos / rep)
fim = time.time()
print(fim-ini)