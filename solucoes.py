import string

def sao_anagramas(string1, string2):
    caracteres_para_remover = string.punctuation + string.whitespace
    
    translator = str.maketrans('', '', caracteres_para_remover)
    
    s1_limpa = string1.lower().translate(translator)
    s2_limpa = string2.lower().translate(translator)
    
    if len(s1_limpa) != len(s2_limpa):
       return False
        
    return sorted(s1_limpa) == sorted(s2_limpa)


def cifra_de_cesar(texto, deslocamento):
    def cifra_de_cesar(texto, deslocamento):
    """
    Criptografa ou descriptografa um texto usando a Cifra de César.

    Argumentos:
    texto (str): A string de entrada a ser cifrada.
    deslocamento (int): O número de posições para deslocar cada letra.
                       Pode ser positivo (para frente) ou negativo (para trás).

    Retorna:
    str: O texto cifrado ou descriptografado.
    """
    resultado = ""

    # Itera sobre cada caractere no texto de entrada
    for char in texto:
        # Verifica se o caractere é uma letra maiúscula
        if 'A' <= char <= 'Z':
            # Calcula o novo código ASCII com base no deslocamento
            # ord('A') é 65.
            # 1. (ord(char) - ord('A')) -> Posição da letra no alfabeto (0-25)
            # 2. (... + deslocamento) -> Aplica o deslocamento
            # 3. (... % 26) -> Garante que o valor "dê a volta" no alfabeto
            # 4. (... + ord('A')) -> Converte de volta para o código ASCII
            novo_codigo = (ord(char) - ord('A') + deslocamento) % 26 + ord('A')
            resultado += chr(novo_codigo)
            
        # Verifica se o caractere é uma letra minúscula
        elif 'a' <= char <= 'z':
            # Lógica idêntica, mas usando a base 'a' (ASCII 97)
            novo_codigo = (ord(char) - ord('a') + deslocamento) % 26 + ord('a')
            resultado += chr(novo_codigo)
            
        # Se não for uma letra (número, espaço, pontuação), mantém o original
        else:
            resultado += char
            
    return resultado

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