def recipe_page(name, info, ingred, instructions):
    print(name)
    print(info)
    print( )
    print("INGREDIENTS")
    for item in ingred:
        print(item + ingred[item])
    print( )
    print("INSTRUCTIONS")
    for i in range(len(instructions)):
        print(instructions[i])
        
def gooey_darkest_deepest_chocolate_pudding_cake():
    name = "gooey darkest deepest chocolate pudding cake"
    info = "Cook time: 65 minutes"
    ingred = {"Granulated sugar: ": "1 1/4 cup", "All-purpose flour: ": "1 cup", "Cocoa powder: ": "3/4 cup", "Baking powder: ": "2 tsp", "Fine sea salt: ": "1/4 tsp", "Milk: ": "1/2 cup", "Melted butter: ": "1/3 cup", "Vanilla extract: ": "1 1/2 tsp", "Packed light brown sugar: ": "1/2", "Hot water: ": "1 1/4", "Ice cream: ": "as much as you want!"}
    instructions = ["Step 1: Preheat oven to 350 degrees F", "Step 2: Whisk together the 3/4 cup of sugar, flour, 1/4 cup of cocoa, baking powder and salt in a bowl. Whisk in the milk, butter and vanilla. Stir together until smooth with a wooden spoon or spatula.", "Step 3: Pour the batter into an ungreased 9-inch square baking pan. Use an offset spatula to level into pan.", "Step 4: Whisk together the sugars and cocoa and sprinkle it evenly over the batter. Pour the hot water over the top, resist the temptation to stir it into the batter.", "Step 5: Bake about 30 minutes, you want the center to bubble and look almost set, almost like an undercooked brownie. Take out of the oven and let stand 15 minutes.", "Step 6: Serve with ice cream and eat it all, enjoy your hard work"]
    recipe_page(name, info, ingred, instructions)

gooey_darkest_deepest_chocolate_pudding_cake()

def user_recipe():
    name = input("Enter your recipe name: ")
    info = input ("Enter the cook time: ")
    len_of_recipe = int(input("Enter the number of steps in the recipe: "))
    ingred = {"all the ingrediats": "no"}
    instructions = []
    for i in range(len_of_recipe):
        next_step = input("Enter the next step: ")
        instructions.append(next_step)
    recipe_page(name, info, ingred, instructions)

user_recipe()