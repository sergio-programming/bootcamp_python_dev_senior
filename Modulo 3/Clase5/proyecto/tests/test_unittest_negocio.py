import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from negocio import VendedorJunior, VendedorSenior
import unittest

class TestVendedor(unittest.TestCase):
    def setUp(self):
        self.vendedor_junior = VendedorJunior("Luisa", 85000000)
        self.vendedor_senior = VendedorSenior("Sergio", 120000000)
        
    def testCalcularComisionJunior(self):
        self.assertEqual(self.vendedor_junior.calcularComision(), 8500000)
        
    def testCalcularComisionSenior(self):
        self.assertEqual(self.vendedor_senior.calcularComision(), 18000000)
        
    
if __name__ == "__main__":
    unittest.main()
        