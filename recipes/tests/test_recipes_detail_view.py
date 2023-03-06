from django.urls import reverse, resolve
from recipes import views

from .test_recipes_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):

    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(views.recipe, view.func)

    def test_recipe_detail_returns_404_if_no_recipe_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 9999}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_correct_recipe(self):
        # Check if the detail template loads the correct recipe
        self.make_recipe()
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        # testing some data from recipe
        self.assertIn('Recipe title', content)
        self.assertIn('Recipe description', content)
        self.assertIn('johndoe', content)

    def test_recipe_detail_template_doesnt_load_recipes_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEquals(response.status_code, 404)
