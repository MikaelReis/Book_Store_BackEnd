from django.test import TestCase
from product.models import Product, Category
from product.tests.factories import ProductFactory, CategoryFactory

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = ProductFactory()  # Usa a Factory
        self.assertIsNotNone(product.pk)  # Verifica se foi salvo no banco

    def test_product_has_categories(self):
        product = ProductFactory(category=[CategoryFactory(), CategoryFactory()])
        self.assertEqual(product.category.count(), 2)  # Verifica categorias associadas

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = CategoryFactory(title="Eletrônicos")
        self.assertEqual(category.title, "Eletrônicos")