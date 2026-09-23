import random

def sat_nop():
    return random.randint(1, 6)


noppa = 0

while noppa != 6:
    noppa = sat_nop()
    print(noppa)


