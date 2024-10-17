while True:
    while True : 
        nome = input('Digite o seu nome')
        if(len(nome) > 3):
            break
      
    
    while True : 
        idade = int(input('Digite a sua idade'))
        if(idade > 0 or idade < 150):
            break
    while True : 
        
        salario = float(input('Digite o seu salario'))
        if(salario > 0):
            break
    while True : 
        sexo = input('Digite f ou m (o)')
        if(sexo == 'f' or sexo == 'm' or sexo == 'o'):
            break
    while True: 
        estado = input('Digite o estado civil s c v d')
        if estado == 's' or estado == 'c'or estado == 'v' or estado == 'd':
            break

            

    # if(len(nome) < 3):
    #     print('Seu nome está com erro precisa ter mais de 3 caracteres')
    # if(idade < 0 or idade > 150):
    #     print('Sua idade está errada deve estar entre 0 e 150')
    # if(salario > 0):
    #     print('Seu salario precisa ser maior que 0')
    # if(sexo == 'f' or sexo == 'm' or sexo == 'o'):
    #     print('Seu sexo precisa etar entre f m ou o')
    # if(estado == 's' or estado == 'c'estado == 'v'estado == 'd'):
    #     print('Estado errado, dgite novamente')
    # if(len(nome) <3 or idade <0 or idade > 150 or salario<0 or estado != 's' or estado != 'c' or estado != 'v'or estado != 'd'or sexo != 'f' or sexo != 'm' or sexo != 'o'):
    #     print('Suas informaç~eos estão erradas: Digite novamente suas informações')
    #     continue
