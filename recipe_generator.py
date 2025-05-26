#I want to create a program that will suggest recipes for a user according to their list of ingredients and dietary requirements.
#I think i will create a list of ingredients categorized into respective food groups + prompt the user to tell me the ingredients they want to use. 
#perhaps there should be alternatives suggested if one of the ingredients mentioned by the user 
#doesn't mesh with their allowed diet

food_groups = {
    "proteins" : ['chicken', 'beef', 'eggs', 'fish', 'lentils', 'beans', 'minced beef'],
    "dairy"  : ['milk', 'cheese', 'yogurt', 'ice cream', 'buttermilk', 'cream'],
    "carbohydrates" : ['pasta', 'rice', 'bread', 'potatoes', 'whole grains'],
    "fats and oils" : ['butter', 'ghee', 'lard', 'palm oil', 'coconut oil', 'vegetable oil', 'olive oil'],
    "vegetables" : ['broccoli', 'carrot', 'cabbage', 'lettuce', 'onion', 'celery', 'rhubarb', 'pumpkin', 'garlic', 'bok choy', 'mushroom'],
    "fruits" : ['strawberry', 'tomato', 'blueberry', 'grape', 'orange', 'lemon', 'lime', 'banana', 'watermelon', 'mango', 'peach'],
    "spices" : ['salt', 'pepper', 'garlic powder', 'chicken bouillion'],
    "condiments" : ['honey', 'soy sauce', 'oyster sauce', 'sesame oil', 'fish sauce', 'chili oil'],
    "non-dairy" : ['coconut milk', 'soy milk', 'almond milk', 'oat milk']
}

all_known_ingredients = [item for sublist in food_groups.values() for item in sublist]

food_choice = []

while True:
    ingredients = input("What ingredients would you like to use? (press q to quit): ")
    if ingredients.lower() == "q":
        break
    elif ingredients not in all_known_ingredients:
        print("Sorry, we don't have that! Please pick another food.")
    else:
        food_choice.append(ingredients)

diet_specif = []
diet_restrict = input("Do you have any dietary restrictions? (y/n): ")
if diet_restrict.lower() == 'y':
    diet_input = input("Enter your restrictions, separated by commas (e.g., vegetarian, gluten-free): ").lower()
    diet_specif = [d.strip() for d in diet_input.split(",")]
else:
    diet_specif.append("none")

recipes = [
    
    
    {
        "meal" : "Veggie Stir Fry",
        "ingredients" : ['onion', 'broccoli', 'butter', 'mushroom', 'soy sauce', 'bok choy'],
        "diet" : ["vegetarian", "gluten-free"]
    },

    {
        "meal" : "steamed fish in coconut curry",
        "ingredients" : ['fish', 'coconut milk', 'chili oil', 'onion', 'soy sauce', 'rice'],
        "diet" : ["pescatarian", "dairy free"]
    },

    {
        "meal" : "spaghetti bolognese",
        "ingredients" : ['olive oil', 'tomato', 'pasta', 'celery', 'onion', 'garlic', 'minced beef', 'chicken bouillion'],
        "diet" : "none"
    }
    
    
]

matching_recipe = []

for recipe in recipes:
    ingredients_ok = all(item in food_choice for item in recipe["ingredients"])
    diet_ok = all(d in recipe["diet"] or recipe["diet"] == ["none"] for d in diet_specif)
    
    if ingredients_ok and diet_ok:
        matching_recipe.append(recipe["meal"])

if matching_recipe:
    print("Good choices! With your selected ingredients, you can make ")
    for r in matching_recipe:
        print(f"- {r}")
else:
    print("Sorry! We don't have any recipes that use all the ingredients you selected.")






