

def whichCake(ingredients,toppings,icing):

    if ingredients == "Sugar":
        print("So you want", ingredients, "in your cake")
    elif toppings == "Cherry":
        print("Cherry is good")
    elif icing == "hmm":
        print("Iceberg is boss")
    print("So you want", ingredients, toppings, "and", icing, "in your cake, awesome")
ingre = input("Name an Ingredient: ")
tops = input("name a topping: ")
ice = input("What's the icing? ")
whichCake(ingre,tops,ice)
