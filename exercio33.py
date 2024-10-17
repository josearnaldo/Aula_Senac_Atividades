controlador = 's'
while controlador == 's' or 'S' == controlador:
    print('----------Calculadora----------')
    print('1 - Adicao')
    print('2 - Subtracao')
    print('3 - Multiplacacao')
    print('4 - Divisão')
    print('Digite 5 ou digite qualquer letra para sair Sair')
    numero=0
    decisao = int(input())
    if(decisao == 1):
        numero1 = int(input('Digite o primeiro número  para adicao'))
        numero2 = int(input('Digite o segundo número  para adicao'))
        numero1 = numero1 + numero2
        print(numero1)
    elif(decisao == 2):
        numero1 = int(input('Digite o primeiro número  para subtracao'))
        numero2 = int(input('Digite o segundo número  para subtracao'))
        numero1 = numero1 - numero2
        print(numero1)
    elif(decisao == 3):
        numero1 = int(input('Digite o primeiro número  para multiplicacao'))
        numero2 = int(input('Digite o segundo número  para multiplacacao'))
        numero1 = numero1 * numero2
        print(numero1)
    elif(decisao == 4):
        numero1 = int(input('Digite o primeiro número  para divisao'))
        numero2 = int(input('Digite o segundo número  para divisao'))
        numero1 = numero1 / numero2
        print(numero1)
    else:
        controlador = ''

