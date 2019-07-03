from django.test import TestCase
from inventory.models import Product, Batch, Order
from datetime import date


class ProductTest(TestCase):
    """ Test module for Product model """
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name='pasta', manufacturer='Little Italy')
        Product.objects.create(
            name='brownie', manufacturer='Brown')

    def test_product_manufacturer(self):
        product_pasta = Product.objects.get(id=1)
        product_brownie = Product.objects.get(id=2)
        self.assertEqual(
            product_pasta.manufacturer, "Little Italy")
        self.assertEqual(
            product_brownie.manufacturer, "Brown")


class BatchTest(TestCase):
    """ Test module for Batch model """
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name='pasta', manufacturer='Little Italy')
        Product.objects.create(
            name='brownie', manufacturer='Brown')
        Batch.objects.create(product=Product.objects.get(id=1), 
            units=1000, date_produced=date(2019,5,30), expiry_date=date(2020,6,30)
            )
        Batch.objects.create(product=Product.objects.get(id=2), 
            units=300, date_produced=date(2019,5,30), expiry_date=date(2019,6,18)
            )
        
      
    def test_batch_units(self):
        batch_1000=Batch.objects.get(product=Product.objects.get(id=1))
        self.assertEqual(
            batch_1000.units, 1000
        )
    
    def test_fresh(self):
        batch_1000=Batch.objects.get(product=Product.objects.get(id=1))
        self.assertEqual(
            batch_1000.freshness, "fresh"
        )

    def test_expired(self):
        batch_expired=Batch.objects.get(product=Product.objects.get(id=2))
        self.assertEqual(
            batch_expired.freshness, "expired"
        )

class OrderTest(TestCase):
    """ Test module for Order model """
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name='pasta', manufacturer='Little Italy')
        
        batch = Batch.objects.create(product=Product.objects.get(id=1), 
            units=1000, date_produced=date(2019,5,30), expiry_date=date(2020,6,30)
            )
        
        Order.objects.create(batch=batch, 
            units=10, company="Coop", order_date=date.today()
        )
        

    def test_order_unit(self):
        order=Order.objects.get(id=1)
        self.assertEqual(
            order.units, 10
        )
