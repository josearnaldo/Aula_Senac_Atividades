# print("Digite o seu nome")
# nome = input()
# print(nome)
# idade = input("Digite sua idade")
# print(type(idade))
# salario = int (input('Salario?='))
# print(type(salario))
# imposto = float(input("Digite o imposto ="))
# print(type(imposto))
# Sal = float(input("Digite o seu salario"))
# print(Sal)
# filho =2 
# idade = 3
# reais  = 2.0541
# print("Tenho %d , de %d idade com %.2f reais" % (filho, idade, reais))
# print("%d , %2.f , " % (2.00, 1))
# a = "José"
# b = "Arnaldo"
# print("Nome"+a+" "+b)

#print(10*"L\n")
#print("+" + 10 * "-" + "+")
#print(("|" + " "*10 + "|\n")* 5, end="")
#print("+" + 10* "-" + "+")

print(5*" " + "/\\" + 5* " ")
print(4*" " + "/" + " "*2 + "\\"+ 5*" ")
print(3*" " + "/" + " "*4 + "\\"+ 3*" ")
print(2*" " + "/" + " "*6 + "\\"+ 3*" ")
print(1*" " + "/" + "_"*8 + "\\"+ 3*" ")
p = 100
g = 0

for i in range(p):
    print(p *" " + "/" + " "*g + "\\"+ 5*" ")
    g+=2
    p-=1
print("/" + "_"*g + "\\"+ 3*" ")


print("Um triângulo de base igual a {0}, {1}, {2}".format(3,4,12))

Linguagem = "Python"

print(f"PRogrqamando em {Linguagem}")


x = 2/3
print(f"printando{x}")
print(f"printando o {x:.2f}")