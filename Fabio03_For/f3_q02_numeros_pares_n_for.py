def main():
    numero = int(input('Digite um número: '))
    mostra_pares(numero)


def mostra_pares(numero):
    for i in range(1, numero + 1):
        if i % 2 == 0:
            print(i)


main()