import json

from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        # Cria um usuário e torna-o staff e superuser
        self.user = UserFactory()
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

        # Gera o token para autenticação
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

        # Cria um produto inicial para testes de listagem
        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self):
        """
        Deve retornar HTTP 200 e a lista de produtos (incluindo self.product).
        """
        url = reverse("product-list", kwargs={"version": "v1"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = response.json()

        self.assertEqual(product_data["results"][0]["title"], self.product.title)
        self.assertEqual(
            float(product_data["results"][0]["price"]), float(self.product.price)
        )
        self.assertEqual(product_data["results"][0]["active"], self.product.active)

    def test_create_product(self):
        """
        Deve permitir que um superusuário crie um produto e retorne HTTP 201.
        """
        category = CategoryFactory()
        payload = {"title": "notebook", "price": 800.00, "categories_id": [category.id]}

        url = reverse("product-list", kwargs={"version": "v1"})
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="notebook")
        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(float(created_product.price), 800.00)
