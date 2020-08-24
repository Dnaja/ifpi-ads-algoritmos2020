def main():
    numero = int(input('Digite um número: '))
    calcula_s(numero)


def calcula_s(numero):
    numerador = 1
    denominador = numero
    resultado = 0

    while numerador <= numero:
        if denominador == 1:
            resultado += numero / 1
            break

        fracao = numerador / denominador

        resultado += fracao 
        numerador += 1
        denominador -= 1

    print('resultado: {:.2f}'.format(resultado))


main()