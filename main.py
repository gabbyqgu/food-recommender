import random 

# functions =========
def pick_a_number(question, min, max):
# gets the user to pick a number within a specific range #
    while True:
        try:
            number = int(input(question))
            if min <= number <= max:
                return number 
            else:
                print(f"Please enter a number from {min} to {max}!!")
        except ValueError:
            print("bro type a number plz")

def yes_or_no(question):
# asks the user to reply yes or no #
    while True:
        answer = input(question).lower().strip()
        if answer.startswith("y"):
            return True
        elif answer.startswith("n"):
            return False
        else:
            print("Pleaseeeeee answer the yes or no question ._.")


def chocolate_chat():
# short chocolate shenanigans #
    while True:
        chocolate_level = input("What's your favorite kind of chocolate? (dark, milk, or white) ").strip().lower()
        if chocolate_level in ["dark", "milk", "white"]:
            break
        else:
            print("\nplz write dark, milk, or white or else I will eat all your chocolate forever.")
    if chocolate_level == "dark":
        print("YESSS UR AUTOMATICALLY PART OF THE COOL KIDS CLUB! °˖✧◝(⁰▿⁰)◜✧˖°")
        print("DARK CHOCOLATE IS THE BEST KIND OF CHOCOLATE EVER!!!!")
        if yes_or_no("Do you wanna hear a joke? :D "):
            input("ur so awesome! okokokok here it is: "
                  "what kind of fruit loves chocolate? ")
            print("a COCOA-NUT!!! HAHAHAHAHAHA. om nom nom")
        else:
            print("oh. :(( ok then.")
    elif chocolate_level == "milk":
        print("i see i see i get it, milk chocolate is pretty good i guess!")
        print("Here's an imaginary deluxe piece of beautiful silky milk chocolate as you wait for ur ultimate food rec :DD!!")
    elif chocolate_level == "white":
        print("just get out. are you even human (°□°;)")


def secret_mission():
# hangman with the most random words ever! 
    word_bank = ["fish", "python", "papaya", "brownie", "cake", "caterpillar", "rocks", "mailman", "mountain", "bookstore"]
    word = random.choice(word_bank) # randomly picks 1 item from a list/string
    guessed = ["_"] * len(word)
    hangman = [
        """
        -----
        |   |
            |
            |
            |
        =========
        """,
        """
        -----
         |   |
         O   |
             |
             |
        =========
        """,
        """
        -----
         |   |
         O   |
         |   |
             |
        =========
        """,
        """
        -----
         |   |
         O   |
        /|   |
             |
        =========
        """,
        """
        -----
         |   |
         O   |
        /|\\  |
             |
        =========
        """,
        """
        -----
         |   |
         O   |
        /|\\  |
        /    |
        =========
        """,
        """
        -----
         |   |
         O   |
        /|\\  |
        / \\  |
        =========
        """
    ]
    wrong_guesses = 0
    max_attempts = 6
    print("WELCOME to....HANGMAN!!!!")
    play_hangman = yes_or_no("ready to play? ")
    if play_hangman:
        while wrong_guesses < max_attempts:
            print("\nWORD: ", " ".join(guessed))
            guess = input("Guess a letter! : ").lower().strip()
            if guess.isalpha() and len(guess) == 1:
                if guess in word:
                    for i in range(len(word)):
                        if word[i] == guess:
                            guessed[i] = guess
                    print("YAYY!! ✅ KEEP GOINGGG")
                else:
                    wrong_guesses += 1
                    print(hangman[wrong_guesses])
                    print("aw man ❌ try again!!") 
                    print(f"Wrong guesses: {wrong_guesses}")
                if "_" not in guessed:
                    print("\nYOU'VE WON!!🥳🎉🕺")
                    print(f"The word was: {word}! :D")
                    break
            else:
                print("Please guess 1 letter!")

        if wrong_guesses == max_attempts:
            print("\noh no u lost :(")
            print(f"The word was: {word}!")
        retry = yes_or_no("Play again? ")
        if retry:
            secret_mission()
    else:
        print("oh.\n")
        
 ################################################

def food_recommender():
    pass
print("WELCOMEE!! to the super duper awesome fabulous cool FOOD RECOMMENDER!!!\n")
start = yes_or_no("✧｡٩(ˊᗜˋ )و✧*｡ \nREADY TO GET YOUR RECOMMENDATION?? ◝(ᵔᗜᵔ)◜")
if start:
    pass
else:
    print("oh ok then hater I hope your pillow is warm on both sides.")
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
    print("swweeeeet! I LOVE SWEET STUFF!!! ᕕ( ᐛ )ᕗ \n")
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
            if chocolate <= 9:
                print("coolio! I like chocolate too :D ")
            else:
                print("YES YOU'RE AWESOME!!")
                print("By being a loyal chocolate fan you have unlocked a SPECIAL SECRET MISSION!!! ")
                print("\n(ps: if you ever see me irl I will treat u to a million dark chocolate specialties :D)")
                secret_mission()
            chocolate_chat()
# THE SAVORY STUFF WEEEEEE ============
elif taste == "savory":
    print("yes i love msg too!")
