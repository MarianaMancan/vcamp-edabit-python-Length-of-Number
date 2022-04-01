//criação da função
def Tamanho(x):
    a = str(x)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
        else:
            return len(a)
    return len(a)

//pedir número
num = int(input("Digite um número: "))
print(Tamanho(num))
