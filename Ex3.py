
product_name = input("Escreva o nome do Produto:");
price_unit = float(input("Escreva o preço unitario do um produto:"));
quant = int(input("Escreva o quantidade comprada:"));
desconto = float(input("Porcentagem do desconto:"));

desconto = desconto/100;
price = price_unit*quant;
price = price - (price * desconto)
print(f"O produto comprado é:{product_name}")
print(f"O valor total: {price}")