from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()  # VALIDATION OCCURS HERE

    def test_recipe_fields_max_length(self):
        fields = [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 10),
            ('servings_unit', 10),
        ]

        # for field in fields:
        #     self.recipe[field[0]] = 'A' * field[1] + 5
        for field, max_length in fields:
            with self.subTest(field=field, max_length=max_length):
                setattr(self.recipe, field, 'A' * (max_length + 1))
                with self.assertRaises(ValidationError):
                    self.recipe.full_clean()  # VALIDATION OCCURS HERE
