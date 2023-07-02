cpf = input ('Digite o CPF:')


lista_numeros_cpf = []

primeiro_digito = 0
segundo_digito = 0

try:
    for digito in cpf:
        if digito.isdigit():
            lista_numeros_cpf.append(int(digito))
    # Primeiro dígito
    contador_regresivo = 10
    soma_cpf = 0
    for num in lista_numeros_cpf[:9]:
        soma_cpf += num * contador_regresivo
        contador_regresivo -= 1
    
    primeiro_digito = \
    (soma_cpf * 10) % 11 if  (soma_cpf * 10) % 11 <= 9 else 0
    #segundo dígito
    contador_regresivo = 11
    soma_cpf = 0
    for num in lista_numeros_cpf[:10]:
        soma_cpf += num * contador_regresivo
        contador_regresivo -= 1
    
    segundo_digito = \
    (soma_cpf * 10) % 11 if (soma_cpf * 10) % 11 <= 9 else 0
    
except ValueError:
    print('Formato invalido de CPF')
except TypeError:
    print('Formato invalido de CPF')

if primeiro_digito == lista_numeros_cpf[-2] and \
    segundo_digito == lista_numeros_cpf[-1]:

    print('CPF válido')
else:
    print('CPF inválido')
