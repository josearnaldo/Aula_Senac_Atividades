v1 = int(input("Digite o primeiro valor"))
v2 = int(input("Digite o segundo valor"))
v3 = int(input("Digite o terceiro valor"))

if(v1> v2 and v1>v3) :
    if(v1>v3 and v2>v3):
        print(v3, ",",v2,",",v1)
    elif(v3>v2):
        print(v2, ",",v3,",",v1)
elif(v2>v1 and v2>v3):
    if(v1>v3):
        print(v3, ",",v1,",",v2)
    else:
        print(v1, ",",v3,",",v2)
elif(v3>v1):
    if(v2>v1):
        print(v1, ",",v2,",",v3)
    else:
        print(v2, ",",v1,",",v3)
