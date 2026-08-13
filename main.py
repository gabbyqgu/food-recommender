print("WELCOMEE!! to the super duper awesome fabulous cool FOOD RECOMMENDER!!!\n")

# functions =========
def pick_a_number(question, min, max):
    while True:
        try:
            number = int(input(question))
            if min <= number <= max:
                return number 
            else:
                print(f"Please enter a number from {min} to {max}!!")
        except ValueError:
            print("bro type a number plz")

def chocolate_chat():
    chocolate_level = "What's your favorite kind of chocolate? (dark, milk, or white) ".strip().lower()


allergies = input("Do you have any dietary restrictions? ").strip().lower()
n = 1
while allergies.startswith("y") and n <= 3:
    print("that's too bad.")
    n += 1
    allergies = input("Do you have any dietary restrictions? ").strip().lower()
    if n == 3:
        print("just stop asking.")
        break # when the condition is met, BREAK out of the loop

sweet_level = "would you like a dessert or snack? "


## this is the MAIN QUESTION that branches out ##
while True:
    taste = input("\nDo you want something salty or sweet? or savory? ").lower().strip()
    if taste in ["salty", "sweet", "savory"]:
        break 
    print("please type either 'salty', 'sweet', or 'savory' or i will come and eat your food >:(") 

# THE SALTY STUFF YUM YUM =========

if taste == "salty":
    print("Yessss I love the sodium chloride!!") 
    spiciness = pick_a_number(
        "On a scale from zero to ten, "
        "how much do you like spicy food? ",
        0, 10)
    if spiciness < 4:
        print("\nwow u suck")
        soup = input("Do you like soup? ").strip().lower()
        if soup.startswith("y"):
            print("I would recommend a warm bowl of miso soup! OM NOM NOM")
        else:
            print("I would recommend a (NOT STALE) ham or tuna sandwich! delicious :D")
    elif spiciness < 8: 
        print("\nI seeee.")
        print("I would recommend some hot nashville fried chicken! gobble gobble crunch crunch")
    else:
        print("\nYou're a hot one ;D")
        print("I would recommend a nice steaming bowl of hot pot >:D WITH EXTRA PEPPERS! YUMMYYY")


# THE SWEET STUFF OOOOOHHH ==========
elif taste == "sweet":
    print("swweeeeet! I LOVE SWEET STUFF!!!\n")
    while True:
        sweet_level = input("Would you like a dessert or a snack? ").lower().strip()
        if sweet_level in ["dessert", "snack"]:
            break 
        print("please type either 'dessert'or 'snack' or i will come and eat ALL your sweets forever >:(\n") 

    if sweet_level == "dessert":
        print("GREAT CHOICE DESSERTS ARE MY FAVORITE THING IN THE ENTIRE WORLD!!")
        chocolate = pick_a_number("On a scale from zero to ten, how much do you like chocolate? ", 0, 10)
        if chocolate <= 1:
            print("You suck. I don't recommend anything.")
        else:
            if chocolate <= 8:
                print("coolio! I like chocolate too :D ")
            else:
                print("YES YOU'RE AWESOME!!")
            print("By being a loyal chocolate fan you have unlocked a SPECIAL SECRET MISSION!!! ")
            secret_mission = input("wip")
            chocolate_chat()
# THE SAVORY STUFF WEEEEEE ============
elif taste == "savory":
    print("yes i love msg too!")
