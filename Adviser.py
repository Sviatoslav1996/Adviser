#Создайте развлекательный чат-бот на Python.
#Данный бот может рекомендовать фильмы,
#музыку,
#игры по жанрам,
#анекдоты,
#интересные истории,
#а также предоставить возможность поиграть в игру.
#При желании можете добавить дополнительные возможности.

import random
import pyjokes

film_library = {
    "film1": "The Godfather",
    "film2": "The Shawshank Redemption",
    "film3": "Gone with the Wind",
    "film4": "Eternals",
    "film5": "The Suicide Squad",
    "film6": "Shang-Chi and the Legend of the Ten Rings",
    "film7": "Crurlla",
    "film8": "Spider-Man: No Way Home",
    "film9": "Red Notice",
    "film10": "Chaos Walking",
    "film11": "Jungle Cruise",
    "film12": "Venom: Let There Be Carnage",
    "film13": "Ghostbusters: Afterlife",
    "film14": "Hitman's Wife's Bodyguard",
    "film15": "Godzilla vs. Kong",
    "film16": "The King's Man",
    "film17": "No Time to Die",
    "film18": "Black Widow",
    "film19": "Dune: Part One",
    "film20": "Outside the Wire",
    "film21": "Free Guy",
    "film22": "Without Remorse",
    "film23": "The Tomorrow War",
    "film24": "Zack Snyder's Justice League",
    "film25": "Army of the Dead",
    "film26": "Snake Eyes: G.I. Joe Origins",
    "film27": "Wrath of Man",
    "film28": "Thunder Force",
    "film29": "Love and Monsters",
    "film30": "The Forever Purge",
    "film31": "The Matrix Resurrections",
    "film32": "Escape Room: Tournament of Champions",
    "film33": "Don't Breathe 2",
    "film34": "Sweet Girl",
    "film35": "Vacation Friends"
}

def get_random_film():
    return random.choice(list(film_library.values()))

print("Welcome to ADVISER")

menu = '''
Select an action:
1. Film
2. Music
3. Game
4. Joke
5. Story
6. Play Game
0. Exit
'''

while True:
    select = input(menu)

    if select == "1":
        user_choice1 = get_random_film()
        print(user_choice1)
    elif select == "0":
        print("Goodbye")
        break
    elif select == "2":
        print("https://soundcloud.com/discover")
    elif select == "3":
        print("https://gaminggorilla.com/most-popular-video-games-now/")
    elif select == "4":
        joke = pyjokes.get_joke(category="neutral")
        print(joke)
    elif select == "5":
        print("https://blog.reedsy.com/short-stories/")
    elif select == "6":
        print("Guess the secret word. You have 5 attempts.")
        answer = "Refrigerator"
        attempts = 4
        user_answer = input("It is found in every home: ").title()

        while attempts > 0:
            if user_answer == answer:
                print("That's the correct answer!")
                break
            else:
                print("Incorrect.")
            
            attempts -= 1
            if attempts > 0:
                user_answer = input(f"{attempts} attempts left. Try again: ").title()

        else:
            print("Sorry, you've run out of attempts. The answer is Refrigerator.")
    else:
        print("Invalid choice. Please try again.")
