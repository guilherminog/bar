def insert_value(nome,idade):

    peso = float(input("Qual seu Peso? "))
    altura = float(input("Qual sua altura?"))
    imc = (peso / (altura ** 2))

    print(f'{nome} tem {idade} anos e seu imc {imc:.2f}.')

    if imc <= 18.9:
        print(f'{nome}, você esta abaixo do peso, Beba muito, você precisa engordar!!! .')

    elif 19 <= imc < 24.9:
        print(f'{nome} , você esta dentro do peso ideal. Beba, beba, beba, mas cuidado para não cair!!!')

    elif 25 <= imc < 30:
        print(f'{nome} ,você deve beber com moderação, já esta acima do peso.')

    elif 31 <= imc <= 40:
        print(f'{nome}, você esta com obesidade cuidado!')

    elif imc > 41:
        print(f'Você não deveria beber, você esta com obesidade morbida, procure um médico o quanto antes!')

    else:
        print(f'{nome} Muito obrigado por estar conosco.')
    quit()
    