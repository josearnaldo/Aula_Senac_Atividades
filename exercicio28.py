salario = float(input('Digite o seu salario'))

if(salario <=280):
    print('Salario antes do Reajuste:', salario)
    print('Foi aumentado 20%')
    print('Aumento foi de ( fora o salario): ',salario*0.2)
    print('Novo salario é de: ', salario*0.2+salario)
elif(salario > 280 and salario <700):
    print('Salario antes do Reajuste:', salario)
    print('Foi aumentado 15%')
    print('Aumento foi de ( fora o salario): ',salario*0.15)
    print('Novo salario é de: ', salario*0.15+salario)
elif(salario >= 700 and salario <1500):
    print('Salario antes do Reajuste:', salario)
    print('Foi aumentado 10%')
    print('Aumento foi de ( fora o salario): ',salario*0.10)
    print('Novo salario é de: ', salario*0.10+salario)
else:
    print('Salario antes do Reajuste:', salario)
    print('Foi aumentado 5%')
    print('Aumento foi de ( fora o salario): ',salario*0.05)
    print('Novo salario é de: ', salario*0.05+salario)

    