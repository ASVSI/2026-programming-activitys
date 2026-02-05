from django.test import TestCase
from .models import Product, userdetails

class ProductTestCase(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name="Test Product", price=20)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 20)

    def test_update_product(self):
        product = Product.objects.create(name="Initial Product", price=10)
        product.name = "Updated Product"
        product.price = 45
        product.save()
        updated_product = Product.objects.get(pk=product.pk)
        self.assertEqual(updated_product.name, "Updated Product")
        self.assertEqual(updated_product.price, 45)

    def test_delete_product(self):
        product = Product.objects.create(name="Delete Me", price=10)
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(name="Delete Me")

class UserDetailsTestCase(TestCase):
    def test_create_userdetails(self):
        user = userdetails.objects.create(name="John Doe", email="johndoe@gmail.com", password="password123")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "johndoe@gmail.com")
        self.assertEqual(user.password, "password123")
        
    def test_update_userdetails(self):
        user = userdetails.objects.create(name="Jane Doe", email="johndoe@gmail.com", password="password123")
        user.name = "Jane Smith"
        user.email = "johndoe1@gmail.com"
        user.password = "newpassword456"
        user.save()
        updated_user = userdetails.objects.get(pk=user.pk)
        self.assertEqual(updated_user.name, "Jane Smith")