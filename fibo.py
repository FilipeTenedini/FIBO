n = int(input('Digite um número: '))

pnumero = 0
snumero = 1
fibo = []
for x in range (1, n+1, 1):
    auxnumero = pnumero + snumero
    pnumero = snumero
    snumero = auxnumero
    fibo.append(auxnumero)
print(f'Sequência com {n} números: {fibo}')
if n in fibo:
    print('O número faz parte da sequência')
else:
    print('Seu número não faz parte da sequência.')
