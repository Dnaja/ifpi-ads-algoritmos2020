def calcula_s():
    numerador = 1
    denominador = 1
    resultado = 0

    while denominador <= 50:
        if (numerador % 2) != 0:
            fracao = numerador / denominador

            denominador += 1
        
        resultado += fracao
        numerador += 1

    print('resultado: {:.2f}'.format(resultado))


calcula_s()