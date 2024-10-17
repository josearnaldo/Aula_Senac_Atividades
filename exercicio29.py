nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a primeira nota'))
nota = ''
situacao = ''
media = (nota1+nota2)/2
if media <= 10 and media >= 9.1:
    nota = 'A'
    situacao = 'Aprovado'
elif media >= 7.6 and media <= 9.0:
    nota = 'B'
    situacao = 'Aprovado'
elif media >=6 and media <= 7.5:
    nota = 'C'
    situacao = 'Aprovado '
elif media >= 4.1 and media<=5.9:
    nota = 'D'
    situacao = 'Reprovado'
elif media <=4.0 and media>=0:
    nota = 'E'
    situacao= 'reprovado'
else:
    print('nota não existe')
print('A primeira nota é ', nota1)
print('A segunda nota é ', nota2)
print('A media é:', media)
print('A nota correspondente: ', nota)
print('A nota é situacao do aluno: ', situacao)