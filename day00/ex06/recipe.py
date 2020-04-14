cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
        },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
        },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
        },
    }


def print_recipe(recipe):
    print(f"Recipe for {recipe}:")
    print(f"Ingredients list: {cookbook[recipe]['ingredients']}")
    print(f"To be eaten for {cookbook[recipe]['meal']}.")
    print(f"Takes {cookbook[recipe]['prep_time']} minutes of cooking.")


def remove_from_cookbook(recipe):
    del cookbook[recipe]


def add_to_cookbook(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time,
    }


def print_recipe_names():
    print('You have the following recipes in your cookbook:')
    for name in cookbook.keys():
        print(f'- {name}')


USER_MSG = (
    "Please select an option by typing the corresponding number:\n"
    "1: Add a recipe\n"
    "2: Delete a recipe\n"
    "3: Print a recipe\n"
    "4: Print the cookbook\n"
    "5: Quit")

print(USER_MSG)
first_time = True
while True:
    if not first_time:
        choice = input('Do you want to see the options again? [y/n]\n')
        if choice[0].lower() == 'y':
            print(USER_MSG)
    user_input = input()
    first_time = False
    if not user_input.isdigit() or int(user_input) not in range(1, 6):
        print(
            'This option does not exist, please type the correspoing number.')
        print('To exit, enter 5.')
        continue
    if user_input == '5':
        print('Cookbook closed.')
        break
    elif user_input == '1':
        recipe_name = input(
            "Please enter the name of the recipe you want to add\n")
        if recipe_name in cookbook:
            print('This recipe is the cookbook already')
            continue
        ingredients = input(
            "OK! Now the ingredients, separeted by commas\n").split(',')
        meal = input('Great! What meal is this recipe for?\n')
        need_prep_time = True
        print('And how many minutes does it take to be done?')
        while need_prep_time:
            try:
                prep_time = int(input())
                need_prep_time = False
            except ValueError:
                print('Please, enter a integer number.')
                continue
        add_to_cookbook(recipe_name, ingredients, meal, prep_time)
        print(f'Allright! {recipe_name} was added to the cookbook')
        continue
    elif user_input == '2':
        recipe_to_delete = input(
            "Please enter the name of the recipe to be deleted:\n")
        if recipe_to_delete in cookbook:
            remove_from_cookbook(recipe_to_delete)
            print(f'{recipe_to_delete} was deleted from the cookbook!')
            continue
        print(f'{recipe_to_delete} is not in the cookbook')
    elif user_input == '3':
        recipe_to_print = input(
            "Please enter the recipe's name to get its details:\n")
        if recipe_to_print in cookbook.keys():
            print_recipe(recipe_to_print)
        else:
            print('This recipe is not in the cookbook')
        continue
    elif user_input == '4':
        print_recipe_names()
        continue
