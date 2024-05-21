import unittest
import sys
sys.path.append(r'C:\Users\marcusthomazetti-ieg\OneDrive - Instituto Germinare\AulasAnotações2°\Desenvolvimento e Operações Ágeis\Exerc\Flas_Test')  # Substitua pelo caminho real para o diretório raiz do projeto
from app.app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_devops(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Germinare',response.data)
if __name__ == '__main__':
    unittest.main()