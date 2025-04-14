import factory
from product.models import Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker("word")
    slug = factory.Faker("slug")
    active = True

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker("word")
    price = factory.Faker("random_number", digits=4)
    active = True

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for cat in extracted:
                self.category.add(cat)
        else:
            self.category.add(CategoryFactory())  # Cria uma categoria automática
