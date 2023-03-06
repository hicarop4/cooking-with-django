from django.urls import reverse, resolve
from recipes import views

from .test_recipes_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):

    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category',
                       kwargs={'category_id': 1}))
        self.assertIs(views.category, view.func)

    def test_recipe_category_template_loads_recipe(self):
        self.make_recipe()
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        # testing some data from recipe
        self.assertIn('Recipe title', content)
        self.assertIn('Recipe description', content)
        self.assertIn('johndoe', content)

    def test_recipe_category_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 9999}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_doesnt_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': recipe.category.id}))
        self.assertEqual(response.status_code, 404)
