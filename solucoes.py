def sao_anagramas(string1, string2):
    caracteres_para_remover = string.punctuation + string.whitespace
    
    translator = str.maketrans('', '', caracteres_para_remover)
    
    s1_limpa = string1.lower().translate(translator)
    s2_limpa = string2.lower().translate(translator)
    
    if len(s1_limpa) != len(s2_limpa):
       return False
        
    return sorted(s1_limpa) == sorted(s2_limpa)


def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar lógica
    pass

def valida_cpf(cpf_string):
    # TODO: Implementar lógica
    pass