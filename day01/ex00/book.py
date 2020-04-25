import datetime

from recipe import Recipe


class Book():

    def __init__(self, name):
        self.name = name
        self.last_update = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        self.creation_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        self.recipes_list = {
                'starter': list(),
                'lunch': list(),
                'dessert': list(),
        }

    def __str__(self):

        book = (
            f"Book's name: {self.name}\n"
            f"created at {self.creation_date}\n"
            f"last update: {self.last_update}\n"
            f"- Recipes by type:\n"
            f"\tstarters: "
            f"{', '.join(self.get_recipes_by_types('starter'))}\n"
            f"\tlunch: "
            f"{', '.join(self.get_recipes_by_types('lunch'))}\n"
            f"\tdessert: "
            f"{', '.join(self.get_recipes_by_types('dessert'))}\n")

        return book

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance. """
        for recipe_type, recipes in self.recipes_list.items():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe)
                    return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type. """
        names = [recipe.name for recipe in self.recipes_list[recipe_type]]

        return names

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update. """

        if not isinstance(recipe, Recipe):
            raise TypeError("Please, enter a recipe object!")

        recipes_type = recipe.recipe_type
        if recipe.name not in self.recipes_list[recipes_type]:
            self.recipes_list[recipes_type].append(recipe)

        self.last_update = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
