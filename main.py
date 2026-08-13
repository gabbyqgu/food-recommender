print("WELCOMEE!! to the super duper awesome fabulous cool FOOD RECOMMENDER!!!")

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
    print("please type either 'salty', 'sweet', or 'savory' or i will come and eat your food >:()") 

# THE SALTY STUFF YUM YUM =========

if taste == "salty":
    print("Yessss I love the sodium chloride!!") 
    spiciness = pick_a_number(
        "On a scale from zero to ten, "
        "how much do you like spicy food? ",
        0, 10)
    if spiciness < 2:
        print("wow u suck")
    elif spiciness < 8: 
        print("ok")
    else:
        print("ur a hot one ;D")
# THE SWEET STUFF OOOOOHHH ==========
elif taste == "sweet":
    print("swweeeeet!")

# THE SAVORY STUFF WEEEEEE ============
elif taste == "savory":
    print("yes i love msg too!")