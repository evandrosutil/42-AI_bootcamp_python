class Recipe():
    """
    The Recipe object contains information about a recipe.

    Attributes:
    ----------
        name (str): The recipe's name
        cooking_lvl (int): From 1 to 5, tells how difficult is to make it
        cooking_time (int): In how many minutes this recipe can be done.
        ingredients (list): list of ingredients needed to make the recipe.
        recipe_type (str): Is it `starter`, `lunch` or `dessert` type.
        description (str): Optional. Brief description of the recipe.
    """

    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, recipe_type, description=''):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __setattr__(self, name, value):

        attr_str = ['name', 'description', 'recipe_type']
        attr_int = ['cooking_lvl', 'cooking_time']

        if name in attr_str and not isinstance(value, str):
            raise TypeError(f"Recipe's {name} must be a string!")
        elif name in attr_int and not isinstance(value, int):
            raise TypeError(f"Recipe's {name}  must be a integer!")
        elif name == 'ingredients' and not isinstance(value, list):
            raise TypeError(f"Recipe's ingredients must be a list!")
        elif name == 'cooking_lvl' and value not in range(1, 6):
            raise ValueError("Recipe's cooking lvl must be betwwen 1-5!")
        elif name == 'recipe_type' \
                and value.lower() not in ['starter', 'lunch', 'dessert']:
            raise ValueError(
                "Recipe's type must be either starter, lunch or dessert!")
        super().__setattr__(name, value)

    def __str__(self):
        """Return the string to print with the recipe info."""

        recipe_info = (
            f"Recipe: {self.name}\n\tCooking level: {self.cooking_lvl}\n\t"
            f"Cooking time: {self.cooking_time}\n\t"
            f"Ingredients: {', '.join(self.ingredients)}\n\t"
            f"Recipe type: {self.recipe_type}\n\t"
            f"Description: {self.description}")

        return recipe_info
