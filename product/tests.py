import copy
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product

# Create your tests here.
class ProductTests(APITestCase):
    def setUp(self):
        self.api_url = '/api/products/'
        self.super_user = self.create_superuser()
        self.client.force_authenticate(user=self.super_user)
        self.default_product = {
            "id": 1,
            "ean": "7223820",
            "description": "Chocolate Dark Hazelnut Silver 300g",
            "category": "Foods",
            "price": 14.0
        }

    def create_superuser(self):
        return User.objects.create_superuser(username='daniel', password='123', email='')

    def test_create_product(self):
        response = self.create_product()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), self.default_product)
    
    def test_list_products(self):
        self.create_product()

        response = self.client.get(self.api_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
    
    def test_get_product(self):
        self.create_product()

        response = self.client.get(f'{self.api_url}1/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.default_product)
        
    def test_update_product(self):
        self.create_product()
        data = copy.deepcopy(self.default_product)
        data['category'] = '30'

        response = self.client.put(f'{self.api_url}1/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.default_product)
    
    def test_partially_update_product(self):
        self.create_product()

        data = {
            "price": 25.0
        }

        response = self.client.patch(f'{self.api_url}1/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], data['price'])
    
    def test_delete_product(self):
        self.create_product()

        response = self.client.delete(f'{self.api_url}1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
    
    def create_product(self):
        data = copy.deepcopy(self.default_product)
        data['category'] = '30'

        response = self.client.post(self.api_url, data, format='json')
        return response
        