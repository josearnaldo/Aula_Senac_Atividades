nome = input("Escreva o nome do usuario:") 
idade = int(input("Escreva a idade do usuario:"))
sexo  = input("Sexo:")
nota1 = float(input("Escreva a primeira nota do usuario:"))
nota2 = float(input("EScreva a segunda nota do usuario:"))

nota = (nota1+nota2)/2

print(f"O nome do usuario é : {nome}")
print(f"A idade do usuario é: {idade}")
print(f"A media das notas é: {nota}")