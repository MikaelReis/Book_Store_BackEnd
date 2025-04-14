from django.urls import reverse
from rest_framework.test import APITestCase
from product.tests.factories import ProductFactory

class ProductViewSetTest(APITestCase):
    def test_list_products(self):
        ProductFactory.create_batch(3)
        url = reverse('product-list')  # Agora deve funcionar
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)