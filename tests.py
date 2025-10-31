import unittest
from solucoes import valida_cpf, encontrar_maior_palavra

class TestValidaCPF(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(valida_cpf("111.444.777-35"))
        self.assertTrue(valida_cpf("529.982.247-25"))
        self.assertTrue(valida_cpf("168.995.350-09"))

    def test_cpf_invalido(self):
        self.assertFalse(valida_cpf("123.456.789-00"))
        self.assertFalse(valida_cpf("111.111.111-11"))
        self.assertFalse(valida_cpf("000.000.000-00"))
        self.assertFalse(valida_cpf("52998224724"))
        self.assertFalse(valida_cpf("5299822472"))

    def test_entradas_invalidas(self):
        self.assertFalse(valida_cpf(""))
        self.assertFalse(valida_cpf("abc.def.ghi-jk"))
        self.assertFalse(valida_cpf(None))
        
class TestEncontrarMaiorPalavra(unittest.TestCase):
    def test_frase_comum(self):
        self.assertEqual(encontrar_maior_palavra("O rato roeu a roupa do rei de Roma"), "roupa")

    def test_frase_com_pontuacao(self):
        self.assertEqual(encontrar_maior_palavra("A jornada de mil milhas começa com um único passo."), "jornada")

    def test_palavras_mesmo_tamanho(self):
        self.assertEqual(encontrar_maior_palavra("Seja forte e corajoso"), "corajoso")

    def test_frase_vazia(self):
        self.assertEqual(encontrar_maior_palavra(""), "")

    def test_todas_palavras_mesmo_tamanho(self):
        self.assertEqual(encontrar_maior_palavra("sol mar luz"), "sol")

    def test_com_pontuacao_em_todas(self):
        self.assertEqual(encontrar_maior_palavra("!vida, amor... paz."), "vida")

if __name__ == "__main__":
    unittest.main()
