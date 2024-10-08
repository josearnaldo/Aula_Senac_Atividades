data = int(input("Escreva a sua data de nascimento."))
datanascimento = 2024 - data;
if(datanascimento>=16):
    print("Pode votar, sua idade  é:", datanascimento)
else:
    print("Não pode votar sua idade é:", datanascimento)
