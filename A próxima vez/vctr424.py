x = int(input("placa largura"))
y = int(input("Placa comprimento"))
m = int(input("Pedidos"))
for linhas in range (0, m):
    xi = int(input("Largura do pedal"))
yi = int(input("Comprimento do pedal"))
cabe = 1
if (xi > x and xi > y):
    cabe = 2 
if (yi > y and yi > x):
    cabe = 2
if cabe == 1:
    print ("Cabe na placa")
else:
    print("Não cabe na placa")