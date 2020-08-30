def main():
    numero = int(input('Digite um número: '))
    calcula_s(numero)


def calcula_s(numero):
    numerador = 1
    denominador = 1
    resultado = 0

    for i in range(1, numero + 1):
        fracao = numerador / denominador

        if (denominador % 2) == 0:
            resultado -= fracao
        else:
            resultado += fracao

        denominador += 1

    print('resultado: {:.2f}'.format(resultado))


main()