nota1 = int(input('nota 1: '))
nota2 = int(input('nota 2: '))
cal = (nota1+nota2)/2
if (cal == 10):
    print('Aprovado com distinção')
elif(cal >= 7):
    print('Aprovado')

else: 
    print('Reprovado')