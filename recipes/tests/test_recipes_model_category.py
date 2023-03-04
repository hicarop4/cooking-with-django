from django.core.exceptions import ValidationError
from .test_recipes_base import TestCase
from recipes.models import Category


class CategoryModelTest(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='Categoria Teste')
        self.category.full_clean()
        self.category.save()
        return super().setUp()

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), self.category.name.capitalize())

    def test_category_name_max_length(self):
        setattr(self.category, 'name', 'A' * 66)
        with self.assertRaises(ValidationError):
            self.category.full_clean()
