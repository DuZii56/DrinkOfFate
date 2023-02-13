import random
import json
import os

script_dir = os.path.dirname(__file__)

ingredients_list = []
drink_list = []
fate = []
category = [78, 79, 140, 141, 202, 203, 260, 261, 310, 311, 350, 351]
display_page = [30, 31, 38, 39, 50, 51, 56, 57, 68, 69, 
    90, 91, 108, 109, 118, 119, 122, 123, 154, 155, 
    176, 177, 182, 183, 188, 189, 214, 215, 226, 227, 
    238, 239, 272, 273, 278, 279, 288, 289, 314, 315]
virgin = [13, 33, 43, 53, 59, 93, 125, 186, 187, 208, 217, 229, 291, 313, 317, 335, 352, 353, 355, 356]

def main():
    #Read all recipies
    with open(script_dir + "/ListOfDrinks.json", "r") as f:
        for line in f:
            drink_list.append(json.loads(line))
    f.close()

    #All available ingredients
    with open(script_dir + "/IngredientsList.txt", "r") as f:
        ingredients_list = f.read()
    f.close
    ingredients_list = ingredients_list.replace("[", "").replace("]", "").replace("\n", "").split(",")
    #Picks drinks based on ingredients in stock
    for drink in drink_list:
        if set(drink["ingredients"]).issubset(ingredients_list):
            fate.append(drink)
    result = random.randint(0,len(fate)-1)
    try:
        print('"' + fate[result]["name"] + '"')
        for j in fate[result]["proportions"]:
            print(" ", j)
        print("Glass:", (fate[result]["glass"] + "\n"))
    except:
        print("No drinks available :(")
        
    #Developer notes:
    #Create a UI.
    #Current version does not consider alternative ingredients (i.e. milk or cream)
main()
