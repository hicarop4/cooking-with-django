from django.test import TestCase
from recipes import models
from django.contrib.auth.models import User


class RecipeTestBase(TestCase):

    def make_category(self, name='Categoria'):
        return models.Category.objects.create(name=name)

    def make_author(self,
                    first_name='John',
                    last_name='Doe',
                    username='johndoe',
                    password='123456',
                    email='johndoe@gmail.com'
                    ):
        return User.objects.create_user(
            username, email, password,
            first_name=first_name, last_name=last_name,
        )

    def make_recipe(self, category_data=None, author_data=None):
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}

        return models.Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title='Recipe title',
            description='Recipe description',
            slug='recipes-slug',
            preparation_time=10,
            preparation_time_unit='minutos',
            servings=5,
            servings_unit='porções',
            preparation_steps='Preparation steps haha',
            preparation_steps_is_html=False,
            is_published=True
        )
