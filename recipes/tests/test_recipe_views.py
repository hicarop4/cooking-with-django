from django.urls import reverse, resolve
from recipes import views

from unittest import skip

from .test_recipe_base import RecipeTestBase


class RecipeViewTest(RecipeTestBase):

    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(views.home, view.func)

    def test_recipe_home_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn("Nenhuma receita encontrada",
                      response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipe(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        # testing some data from recipe
        self.assertIn('Recipe title', content)
        self.assertIn('Recipe description', content)
        self.assertIn('johndoe', content)
        # testing if we are receiving the recipes from view context
        context_recipes = response.context['recipes']
        self.assertEquals(len(context_recipes), 1)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category',
                       kwargs={'category_id': 1}))
        self.assertIs(views.category, view.func)

    def test_recipe_category_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 9999}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(views.recipe, view.func)

    def test_recipe_detail_returns_404_if_no_recipe_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 9999}))
        self.assertEqual(response.status_code, 404)
