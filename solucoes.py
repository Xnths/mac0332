import string

def sao_anagramas(string1, string2):
    # TODO: Implementar lógica
    pass

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar lógica
    pass

def encontrar_maior_palavra(frase):
    palavras = frase.split()
    maior_palavra = ""
    maior_tamanho = 0

    for palavra in palavras:
        limpa = palavra.strip(string.punctuation)
        if len(limpa) > maior_tamanho:
            maior_tamanho = len(limpa)
            maior_palavra = limpa

    return maior_palavra


def valida_cpf(cpf_string):
    if (cpf_string == None):
        return False
    
    cpf = ''.join([c for c in cpf_string if c.isdigit()])

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"