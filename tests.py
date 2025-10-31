import unittest
from solucoes import valida_cpf

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

if __name__ == "__main__":
    unittest.main()
