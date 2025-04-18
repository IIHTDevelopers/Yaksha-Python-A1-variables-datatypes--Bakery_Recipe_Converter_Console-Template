CUP_FLOUR_TO_GRAMS = 128
CUP_SUGAR_TO_GRAMS = 200

def convert_flour_to_grams(cups):
    """Convert flour from cups to grams (1 cup = 128 grams)"""
    if not isinstance(cups, (int, float)) or cups <= 0:
        raise ValueError("Flour amount must be positive")
    grams = cups * CUP_FLOUR_TO_GRAMS
    return round(grams)

def convert_sugar_to_grams(cups):
    """Convert sugar from cups to grams (1 cup = 200 grams)"""
    if not isinstance(cups, (int, float)) or cups <= 0:
        raise ValueError("Sugar amount must be positive")
    grams = cups * CUP_SUGAR_TO_GRAMS
    return round(grams)

if __name__ == "__main__":
    print("Welcome to Recipe Converter!")
    print("-" * 30)
    
    recipe_name = input("Enter recipe name: ")
    flour_cups = float(input("Enter flour (cups): "))
    sugar_cups = float(input("Enter sugar (cups): "))
    
    flour_grams = convert_flour_to_grams(flour_cups)
    sugar_grams = convert_sugar_to_grams(sugar_cups)
    
    print("\nCONVERTED RECIPE:", recipe_name)
    print(f"Flour: {flour_grams}g")
    print(f"Sugar: {sugar_grams}g")