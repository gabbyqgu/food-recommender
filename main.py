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
        print("so I guess I'll just recommend a white chocolate chip blondie. ok but these are actually really fire "
        "if you've never had them before. esp with BIG whtie chocolate chunks that are like sorta melty but you can't " 
        "have any sort of nuts in them like idk who in their right mind puts NUTS into something so delectable but " 
        "anyway its gotta be slightly crunchy near the edges of the blondie but not so much as a brownie and soft and " 
        "fudge-y in the middle!! add loads of vanilla and OMG totally add some caramel thatd be SO YUMMYY!! like hidden " 
        "pockets of caramel!!! ok enjoy! ( ദ്ദി ˙ᗜ˙ )✧ ")
        return
    
def cuisine_chat(cuisine):
    user_cuisine = input(cuisine).strip().lower()
    if user_cuisine == "american":
        print("YEEHAW HOWDY THERE WELCOME TO THE LAND OF THE FREEEEEE 🗽🍔🦅🤠🏈💥")
    elif user_cuisine == "japanese":
        print("japanese food is actually peak FANTASTIC CHOICE I LOVE JAPANNN 🌸🍣🗾🍙🏯🍡")
    elif user_cuisine == "korean":
        print("안녕하세요!! (HII) ⸜(｡˃ ᵕ ˂ )⸝♡")
    elif user_cuisine == "chinese":
        print("NI HAO 我爱你! 🫰🫰(i luv u!!)🥡🐲🥮🥢🧧")
    elif user_cuisine == "italian":
        print("Italian food is litearlly my FAVORITE EVERR! I love italy like the food is so good and the gelato is litearlly the best "
                "and the historical monuments are so cool like i cant believe the pantheon was built like 2000 years ago GENUNIELY INSANE "
                "and the architecture is so cool but my favorite part by far is def the pasta it just tastes SO MUCH BETTER NO JOKE theres "
                "like a gazillion types of pasta and sauces but all are really simple but require SO MUCH TECHNIQUE and i just want to be like "
                "the guy from ratatouille and cook italian food and be happy 🤌🛵🍋🏛️🍕🍝")
    elif user_cuisine == "mexican":
        print("hola como estas me gusta food 🪇🤠🌮🌶️🌵")
    elif user_cuisine == "french":
        print("oui oui baguette 🥖🥐🗼")
    elif user_cuisine == "greek":
        pass
    elif user_cuisine == "indian":
        pass
    else:
        print("sorry, the super awesome food recommender has not added your cuisine of choice yet.")


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
    print("WELCOMEE!! to the super duper awesome fabulous cool FOOD RECOMMENDER!!!\n")
    start = yes_or_no("✧｡٩(ˊᗜˋ )و✧*｡ \n\nREADY TO GET YOUR RECOMMENDATION?? ◝(ᵔᗜᵔ)◜ ")
    if not start:
        print("oh ok then hater I hope your pillow is warm on both sides.")
        return # ends the entire function
    allergies = input("Do you have any dietary restrictions? ").strip().lower()
    n = 1
    while allergies.startswith("y") and n <= 3:
        print("that's too bad.")
        n += 1
        allergies = input("Do you have any dietary restrictions? ").strip().lower()
        if n == 3:
            print("just stop asking.")
            return
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
                return
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
        random_number = pick_a_number("Pick a number any number between 1 and 10: ", 1, 10)
        if random_number == 8 or random_number == 5:
            input("HOLY GUACAMOLE YOU'RE A MIND READER!!! HIGH 5 ")
            print("i just wanted to say that i actually have no idea what the difference is between salty and savory i think savory is just fancier but i dont really know T_T")
            print("ANYWAYS! you get some special treatment for picking the right number :0")
            cuisine_chat("What's your favorite cuisine? ")
        else:
            print("oops wrong number ಠ╭╮ಠ ")




    feedback = yes_or_no("Did you enjoy your recommendation? ")
    if feedback:
        print("YESSS AWESOME I'M SO HAPPY FOR YOU!!!! ᕕ( ᐛ )ᕗ DO ENJOY!!!")
    else:
        print("I'm sorry about that :( ")
        retry = yes_or_no("Would you like to get another recommendation? ")
        if retry:
            food_recommender()
        else:
            print("Ok I guess see you in the afterlife! weeeeeeeeeeeeeeeeeeee")

food_recommender()
