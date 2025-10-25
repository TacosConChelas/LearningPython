def main():
    item = str(input("Item: ")).lower().strip()

    valid_calories(item)

def valid_calories(item):
    fruits = {
        "apple" : 130, "avocado" : 50, "bannana" : 110, "cantaloupe" : 50, "grapefruit" : 60,
        "grapes" : 90, "honeydew melon" : 50, "kiwifruit": 90, "lemon" : 15, "lime" : 20,
        "nectaline" : 60, "orange" : 80, "peach" : 60, "pear" : 100, "pineapple" : 50,
        "plums" : 70, "strawberries" : 50, "sweet cherries" : 100, "tangerine" : 50, "watermelon" : 80 
    }
    if item in fruits.keys():
        print("Calories:", fruits[item])

main()