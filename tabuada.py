

def Multiplicar(numero):
    def Multiplo(multip):
        return int(numero) * multip
    return Multiplo

num_input = input()
num = Multiplicar(num_input)

for i in range(1,11):
    print(f'O Número {num_input} multiplo de {i} é ',num(i))
