from insert_data import inf_init, inf_idade, inf_contato
from insert_imc import insert_value

nome, idade = inf_init()
tel, email, endereco = inf_contato()


while True:

    if 0 <= idade < 17:
        print(f'{nome},Você ainda não tem idade suficiente para beber')
        quit()
    elif 18 <= idade < 100:
        print(f'{nome},fique a vontade e venha beber conosco!')
        q = input(f"{nome}, aceita participar de uma pesquisa de saúde? Responda S / N: ").lower()
        if q == 'n':
            print(f'{nome}, muito obrigado e tenha uma ótima noite!')
            quit()
        elif q == 's':
            print(f'Muito obrigadop,{nome} , vamos iniciar.')
            q = insert_value(nome,idade)
        else:
            break

    else:
        print('Idade invalida!')
        idade = inf_idade()














#   peso = float(input("Qual seu Peso? "))
# altura = float(input("Qual sua altura?"))
# imc = peso / (altura * altura)

# print(f'{nome} tem {idade} anos e seu imc {imc:.2f}.')
# if imc <= 18.9:
#     print(f'{nome}, você esta abaixo do peso, Beba muito, você precisa engordar!!! .')

# elif 19 <= imc < 24.9:
#     print(f'{nome} , você esta dentro do peso ideal. Beba, beba, beba, mas cuidado para não cair!!!')

# elif 25 <= imc < 30:
#     print(f'{nome} ,você deve beber com moderação, já esta acima do peso.')

# elif 31 <= imc <= 40:
#     print(f'{nome}, você esta com obesidade cuidado!')

# elif imc > 41:
#     print(f'Você não deveria beber, você esta com obesidade morbida, procure um médico o quanto antes!')

# else:
#     print(f'{nome} Muito obrigado por estar conosco.')
