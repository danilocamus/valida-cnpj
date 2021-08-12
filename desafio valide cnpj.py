# 042520110001
# 04252011000110
# 40688134000161
# transformando uma string em uma lista

# recebe o cnpj e forma de string e retorna ele como int
# def recebe_cnpj():
#     num = input('Digite o cnpj: ')
#     cnpj_list = list(num) # transforma uma string em uma lista de string
#     return transforma_lista(cnpj_list) # manda o cnpj em forma de string, transforma em int e retorna pra função


# transforma uma list de string em uma lista de int
def transforma_lista(cnpj):
    cnpj_list = list(map(int, cnpj))
    return cnpj_list


def remove_caracteres(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('.', '')
    return cnpj


def aplica_formula(num):
    if len(num) == 12:
        num_list1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        result = [a * b for a, b in zip(num, num_list1)]
        return result
    else:
        num_list2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        result = [a * b for a, b in zip(num, num_list2)]
        return result


def valida_digito(n):
    if n <= 9:
        return n
    else:
        return 0




# transformando a lista de strings em uma lista int

# cnpj_list = [int(i) for i in cnpj_list]
# for i in range(0, len(cnpj_list)):
#     cnpj_list[i] = int(cnpj_list[i])

# cnpj_list = list(map(int, cnpj_list))


# resul = sum([a * b for a, b in zip(cnpj_list, num_list)])
# print(resul)




cnpj = list(input('Digite o cnpj: '))

cnpj_copia = cnpj[:-2]
# print(f'sem os 2 ultimos caracteres {cnpj_copia}')
cnpj_list = (transforma_lista(cnpj)) # transforma a lista de string em uma lista int

copia_cnpj_list = cnpj_list[:-2]
print(f'esta é a copia {copia_cnpj_list}')
# print(sum(aplica_formula(cnpj_list)))

primeiro_digito = valida_digito(11 - (sum(aplica_formula(copia_cnpj_list)) % 11))



print(f'este é o primeiro digito {primeiro_digito}')

copia_cnpj_list.append(primeiro_digito)



segundo_digito = valida_digito(11 - (sum(aplica_formula(copia_cnpj_list)) % 11))



print(f'este é o segundo digito {segundo_digito}')
segundo_digito = valida_digito(segundo_digito)

copia_cnpj_list.append(segundo_digito)
print(f'este é o resultado {copia_cnpj_list}')
print(f'esse é o cnpj_list {cnpj_list}')
if cnpj_list == copia_cnpj_list:
    print('Cnpj válido')
else:
    print('cnpj invalido')
