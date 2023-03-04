from .test_recipes_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 10),
        ('servings_unit', 10),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()  # VALIDATION OCCURS HERE

    @parameterized.expand([
        ('is_published', True),
        ('preparation_steps_is_html', False),
        ('cover', ''),
    ])
    def test_recipe_default(self, field, default):
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(getattr(self.recipe, field), default)

    def test_recipe_string_representation(self):
        self.recipe.title = "Testing representation"
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            "Testing representation - by johndoe", str(self.recipe))
