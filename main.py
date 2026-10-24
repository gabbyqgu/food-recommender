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
            joke_likeness = yes_or_no("Did you like the joke?? ")
            if joke_likeness: 
                print("omg THANK YOU!! i know i'm just the funniest person ever. 🍫")
                print("as a thank you enjoy hangman!! ")
                secret_mission()
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
    print("!disclaimer i am only familiar with american + eastern asian foods so i may be innacurate in other cuisines!")
    if user_cuisine == "american":
        print("YEEHAW HOWDY THERE WELCOME TO THE LAND OF THE FREEEEEE 🗽🍔🦅🤠🏈💥")
        while True:
            american_dish = input("pick a dish to dive deeper (っ˘ڡ˘ς):\nburgers :P\nfried\nsouthern 🤠\nthanksgiving-style\n"
                                  "tailgate! (it's essentially food u can eat while walking/easy to share)\nCOSTCO!").lower().strip()
            if american_dish in ["burgers", "fried", "southern", "thanksgiving-style", "tailgate", "costco"]:
                break
            print("please pick a dish and spell it correctly 🥺 they are all very yummy :D (espeeeeciiallyy costco)")
        if american_dish == "burgers":
            pass
        elif american_dish == "fried":
            pass
        elif american_dish == "southern":
            pass
        elif american_dish == "thanksgiving-style" or american_dish == "thanksgiving":
            pass
        elif american_dish == "tailgate":
            pass
        elif american_dish == "costco":
            print("I LOVE COSTCO I PRACTICALLY LIVE THERE!!!!!!! if you live not in america i envy you bc i keep seeing like amazing costco food court items")
            while True:
                costco_hack = input("Do you want to hear some costco hacks(im a costco executive member i know ball)").lower().strip()
                if costco_hack.startswith("y"):
                    print("OK LET ME ENLIGHTEN YOU WITH MY COSTCO KNOWLEDGE!")
                    print("OK if prices end in .99¢ theyre like normal")
                    print("but if the prices end in .97¢ these are SUPER CHEAP LIKE BUY IT ALLL")
                    print("if it ends in .88¢ or .49¢ or .79¢ .00¢ its like also really cheap")
                    print("if theres an asterisk(*) THEN GET IT BECUASE ITS NEVER COMING BACK 😱😱")
                    print("and if you dont get the hot dog youre really missing out on life")
                    print("AND theres a 30 day price match so if something goes on sale after you've already bought it YOU CAN LIKE GET IT PRICE MATCHED HOW COOL IS THAT???")
                    print("and also max out on samples 😌 i promise you they dont care ive gone back like 10x (they hate me)")
                    print("anyways....")
                    break
                elif costco_hack.startswith("n"):
                   print("oh its ok then!") 
                   break
                else:
                    print("Pleaseeeeee answer yes or no :D if you dont know what costco is its this ELITE warehouse with SAMPLES and you can bulk buy stuff!!")
            print("ok so i HAVE to recommend the $1.50 hot dog and drink combo ")


    elif user_cuisine == "japanese":
        print("japanese food is actually peak FANTASTIC CHOICE I LOVE JAPANNN 🌸🍣🗾🍙🏯🍡")
        while True:
            japanese_dish = input("pick a dish to dive deeper ദ്ദി ˉ͈̀꒳ˉ͈́ )✧: \nnoodles/soup\nstreet food\nfried\nfishy\nsweet\n").lower().strip()
            if japanese_dish in ["noodles", "noodles/soup", "soup", "street food", "fried", "fishy", "sweet"]:
                break 
            print("please pick a dish and spell it correctly 🥺 they are all very yummy :D") 
        if japanese_dish == "noodles" or japanese_dish == "noodles/soup" or japanese_dish == "soup":
            pass
        elif japanese_dish == "street food":
            print("so japanese street food is SO ELITE!")
        elif japanese_dish == "fried":
            print("this stuff is so addicting i swear. my comfort food 🤗")
        elif japanese_dish == "fishy":
            fish_joke = input("what do you call a fish without an eye? ")
            print("a fsh. ha. ha. ha!! soo witty")
        elif japanese_dish == "sweet":
            print("this is the stuff of my DREAMSSSSS")

        print("ദ്ദി ˉ͈̀꒳ˉ͈́ )✧")
        print("(っ˘ڡ˘ς)")
        print("૮₍ •⤙•˶")

    elif user_cuisine == "korean":
        print("안녕하세요!! (HII) ⸜(｡˃ ᵕ ˂ )⸝♡")
        while True:
            korean_dish = input("pi")

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
        print("indian food is so good i could eat naan for DAYS! 🕌🪷🍛🧡🤍💚")

    else:
        print("sorry, the super awesome food recommender has not added your cuisine of choice yet.")
        cuisine_repick = yes_or_no("pick another one? ")
        if cuisine_repick:
            cuisine_chat(cuisine)
        else:
            return


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
        if random_number == 8 or random_number == 5 or random_number == 1:
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
