import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from negocio import VendedorJunior, VendedorSenior

import pytest

def testCalcularComisionJunior():
    vendedor = VendedorJunior("Pedro", 230000000)
    assert vendedor.calcularComision() == 23000000
    
def testCalcularComisionSenior():
    vendedor = VendedorSenior("Andrea", 300000000)
    assert vendedor.calcularComision() == 45000000