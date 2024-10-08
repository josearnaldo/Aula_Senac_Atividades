li = [[1,2],[3],[4,5,6]]
print(type(li))
li = (tuple(li))
print(type(li))
print(li)


tu = (1,2,3,4,5,6)
print(type(tu))
tu = (list(tu))
print(type(tu))

idade = 10
if (idade ==  16):
    print("Pode votar")
else:
    if idade>=16:
        print("Pode Dirigir")
    else:
        if(idade <16):
            print("Apenas Estude")
