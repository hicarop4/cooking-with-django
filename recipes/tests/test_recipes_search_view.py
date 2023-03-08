from django.urls import reverse, resolve
from recipes import views
from .test_recipes_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):

    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_search_views_function_is_correct(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertEqual(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(
            reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_escaped_on_title(self):
        url = reverse('recipes:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn('Search for &quot;&lt;Teste&gt;&quot;',
                      response.content.decode('utf-8'))

    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = 'This is recipe 1',
        title2 = 'This is recipe 2'

        recipe1 = self.make_recipe(slug='onet', title=title1, author_data={
                                   'username': 'oneauthor'})

        recipe2 = self.make_recipe(slug='twot', title=title2, author_data={
                                   'username': 'twoauthor'})

        url = reverse('recipes:search')
        response1 = self.client.get(f'{url}?q={title1}')
        response2 = self.client.get(f'{url}?q={title2}')
        response_both = self.client.get(f'{url}?q=this')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])