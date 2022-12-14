import copy
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product

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
        
        desired_response = copy.deepcopy(self.default_product)
        desired_response['images'] = []

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), desired_response)
    
    def test_list_products(self):
        self.create_product()

        response = self.client.get(self.api_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
    
    def test_get_product(self):
        response_product = self.create_product()

        response = self.client.get(f'{self.api_url}{response_product.json()["id"]}/', format='json')

        desired_response = copy.deepcopy(self.default_product)
        desired_response['images'] = []

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), desired_response)
        
    def test_update_product(self):
        response_product = self.create_product()
        data = copy.deepcopy(self.default_product)
        data['category'] = '30'

        response = self.client.put(f'{self.api_url}{response_product.json()["id"]}/', data, format='json')

        desired_response = copy.deepcopy(self.default_product)
        desired_response['images'] = []

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), desired_response)
    
    def test_partially_update_product(self):
        response_product = self.create_product()

        data = {
            "price": 25.0
        }

        response = self.client.patch(f'{self.api_url}{response_product.json()["id"]}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], data['price'])
    
    def test_delete_product(self):
        response_product = self.create_product()

        response = self.client.delete(f'{self.api_url}{response_product.json()["id"]}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
    
    def test_create_image(self):
        response_product = self.create_product()
        response = self.create_image(response_product.json()['id'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def create_product(self):
        data = copy.deepcopy(self.default_product)
        data['category'] = '30'

        response = self.client.post(self.api_url, data, format='json')
        return response
    
    def create_image(self, product_id):
        payload = {
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/220px-Google_2015_logo.svg.png"
        }
        url = f'{self.api_url}{product_id}/add_image/'
        response = self.client.post(url, data=payload, format='json')
        return response