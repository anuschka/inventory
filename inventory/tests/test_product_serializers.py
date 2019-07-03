from rest_framework import serializers
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json

from inventory.models import Product, Batch, Order
from inventory.serializers import ProductSerializer, BatchSerializer

# initialize the APIClient app
client = Client()

class GetAllProductsTest(TestCase):
    """ Test module for GET all products """

    def setUp(self):
        Product.objects.create(
            name='pasta', manufacturer='Black')
        Product.objects.create(
            name='spagetti', manufacturer='Brown')
        Product.objects.create(
            name='zucchini', manufacturer='Black')
        Product.objects.create(
            name='cucambers', manufacturer='Brown')

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('product_list'))
        # get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleProductTest(TestCase):
    """ Test module for GET single product """

    def setUp(self):
        self.pasta = Product.objects.create(
            name='pasta', manufacturer='Black')
        self.spagetti = Product.objects.create(
            name='spagetti', manufacturer='Brown')
        self.zucchini = Product.objects.create(
            name='zucchini', manufacturer='Black')
        self.zucchini = Product.objects.create(
            name='cucambers', manufacturer='Brown')

    def test_get_valid_single_product(self):
        response = client.get(
            reverse('product_detail', kwargs={'pk': self.zucchini.pk}))
        product = Product.objects.get(pk=self.zucchini.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('product_detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):
    """ Test module for inserting a new product """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'manufacturer': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'manufacturer': 'Black'
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('product_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('product_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleProductTest(TestCase):
    """ Test module for updating an existing product record """

    def setUp(self):
        self.pasta = Product.objects.create(
            name='pasta', manufacturer='Black')
        self.spagetti = Product.objects.create(
            name='spagetti', manufacturer='Brown')
        self.valid_payload = {
            'name': 'muffin',
            'manufacturer' : 'white'
        }
        self.invalid_payload = {
            'name': 'muffin',
            'manufacturer' : ''
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('product_detail', kwargs={'pk': self.pasta.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('product_detail', kwargs={'pk': self.pasta.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleProductTest(TestCase):
    """ Test module for deleting an existing product record """

    def setUp(self):
        self.pasta = Product.objects.create(
            name='pasta', manufacturer='Black')
        self.spagetti = Product.objects.create(
            name='spagetti', manufacturer='Brown')

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('product_detail', kwargs={'pk': self.pasta.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = client.delete(
            reverse('product_detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)