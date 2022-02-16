import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class FeatureTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make('Feature')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.feature)


class Profissao_ClienteTestCase(TestCase):

    def setUp(self):
        self.profissao_cliente = mommy.make('Profissao_Cliente')

    def test_str(self):
        self.assertEquals(str(self.profissao_cliente), self.profissao_cliente.profissao_cliente)


class ClienteTestCase(TestCase):

    def setUp(self):
        self.cliente = mommy.make('Cliente')

    def test_str(self):
        self.assertEquals(str(self.cliente), self.cliente.nome)



