from rest_framework import status
from rest_framework.test import APITestCase


class CreateCustomerTestCase(APITestCase):

    def setUp(self):
        self.create_customer_url = '/api/v1/customers/'

    def test_create_customer_success(self):
        """ Ensure return status code 201 when send correct user data """
        success_data = {
            'cpf': '68328441071',
            'nome': 'João da Silva',
            'email': 'joaoemail@email.com',
            'dataDeNascimento': '1992-10-20',
            'sexo': 'M',
            'rendaMensal': 120490
        }
        response = self.client.post(self.create_customer_url, success_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get('id', False))

    def test_create_customer_error(self):
        """ Ensure return status code 400 when send error user data """
        error_data = {
            'cpf': '6832844107133123123',
            'nome': 'João da Silva',
            'email': 'joaoemail@email.com',
            'dataDeNascimento': '1992-10-20',
            'sexo': 'M',
            'rendaMensal': 120490
        }
        response = self.client.post(self.create_customer_url, error_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
