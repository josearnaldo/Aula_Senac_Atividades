senha = '1234'

historico = [];
historico.append('0');
senha1 = input('Digite sua senha:')
if senha == senha1:
    while decisao != '4':
        print('Escolha um item da lista');
        print('1-Extrato');
        print('2-Deposito');
        print('3-Saque');
        print('4-Sair');
        decisao = input();
        if(decisao == '1'):
            print('Extrato da conta: ', extrato)
        elif(decisao == '2'):
            deposito = float(input("Deposito de quanto: "))
            extrato = extrato + deposito
            escrito = '+'
            escrito += str(deposito)
            historico.append(escrito)
            historico.append(extrato)
            print(historico)
            print(extrato)
        elif(decisao == '3'): 
            saque = float(input("Saque em qual valor:"))
            if(deposito-saque < 0):
                print('Impossivel fazer a operação')
            else:
                extrato = extrato - saque
                escrito = '-'
                escrito += str(saque)
                historico.append(escrito)
                historico.append(extrato)
        elif(decisao == '4'): 
            decisao = '4'
            print("Saindo...")
        else:
            print('Decisao invalida')
else:
    print('Senha Invalida')