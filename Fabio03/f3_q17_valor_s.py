def main():
    numero = int(input('Digite um número: '))
    calcula_s(numero)


def calcula_s(numero):
    numerador = 1
    denominador = 1
    resultado = 0

    while denominador <= numero:
        fracao = numerador / denominador

        resultado += fracao
        denominador += 1

    print('resultado: {:.2f}'.format(resultado))


main()