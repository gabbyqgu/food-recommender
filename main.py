print("WELCOMEE!! to the super duper awesome fabulous cool FOOD RECOMMENDER!!!")
allergies = input("Do you have any dietary restrictions? ").strip().lower()
n = 1
while allergies == "yes" and n <= 4:
    print("that's too bad.")
    n += 1
    allergies = input("Do you have any dietary restrictions? ").strip().lower()
    if n == 4:
        print("just stop asking.")
        break

sweet_level = "would you like a dessert or snack? "