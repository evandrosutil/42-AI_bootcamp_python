import unittest

from book import Book
from recipe import Recipe


class TestBookAndRecipe(unittest.TestCase):

    def test_book_without_name(self):
        with self.assertRaises(TypeError):
            Book()

    def test_creat_book_instance(self):
        book = Book('recipes')
        self.assertEqual(book.name, 'recipes')

    def test_add_recipe(self):
        recipe = Recipe(
            name='Simple Salad',
            cooking_lvl=1,
            cooking_time=15,
            ingredients=[
                'lettuce',
                'cress',
                'arugula',
                'tomatoes',
                'parmesan cheese'],
            recipe_type='starter',
            description='a simple starter.')
        book = Book('recipes')
        book.add_recipe(recipe)
        self.assertIn(recipe, book.recipes_list[recipe.recipe_type])

    def test_get_recipe_by_name(self):
        recipe = Recipe(
            name='Simple Salad',
            cooking_lvl=1,
            cooking_time=15,
            ingredients=[
                'lettuce',
                'cress',
                'arugula',
                'tomatoes',
                'parmesan cheese'],
            recipe_type='starter',
            description='a simple starter.')
        book = Book('recipes')
        book.add_recipe(recipe)
        added = book.get_recipe_by_name('Simple Salad')
        self.assertEqual(added, recipe)

    def test_get_recipes_by_types(self):
        recipe = Recipe(
            name='Simple Salad',
            cooking_lvl=1,
            cooking_time=15,
            ingredients=[
                'lettuce',
                'cress',
                'arugula',
                'tomatoes',
                'parmesan cheese'],
            recipe_type='starter',
            description='a simple starter.')
        book = Book('recipes')
        book.add_recipe(recipe)
        book_starters = book.get_recipes_by_types('starter')
        self.assertIsInstance(book_starters, list)
        self.assertEqual(len(book_starters), 1)
        self.assertEqual(book_starters[0], recipe.name)

if __name__ == "__main__":
    unittest.main()
