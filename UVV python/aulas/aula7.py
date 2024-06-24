#FUNCIONAMENTO DO in range

#in range(s,s,s) ou seja ==> (start, stop, step) ==> Começo, fim, passo.

"""

for x in range(0, 30, 2):
    print(x) # Vai contar de 0 a 30, pulando sempre dois números

"""

x = 0

while x < 10:
    x += 1
    if x % 2 == 0:
        continue #o "continue" pula o número que se enquadrar do if
    print(x)