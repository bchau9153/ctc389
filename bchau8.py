#Benson Chau
#Lab 8

play_again = "yes"

while play_again == "yes":
    name = input("Welcome traveler! What is your name? ")
    print("Hello " + name + ", you wake up in an old abandoned mansion. The front door is locked behind you, and you must find a way through the house.")

    choice1 = float(input("You are standing in the main hallway. There are 3 paths you can take. \n 1. Go up the stair case \n 2. Go into the kitchen \n 3. Go into the library \n Which path do you choose? "))

    if choice1 == 1:
        print(name + " climbs up the creaky staircase and hears whispering coming from upstairs.")
    elif choice1 == 2:
        print(name + " walks into the kitchen and finds a strange smell coming from the oven.")
    elif choice1 == 3:
        print(name + " enters the library and notices a book glowing faintly on a shelf.")
    else:
        print("You hesitate, but the house pulls you foward anyway.")

    choice2 = float(input("You find a locked wooden chest in the room. Next to it are 3 small keys. \n 1. Try the rusty key \n 2. Try the silver key \n 3. Try the golden key \n Which key do you try? "))

    if choice2 == 1:
        print("The rusty key snaps in the lock, but the chest pops open anyway.")
    elif choice2 == 2:
        print("The silver key turns smoothly and the chest clicks open.")
    elif choice2 == 3:
        print("The golden key glows for a second before the chest creaks open.")
    else:
        print("None of the keys seem right, but the chest opens on its own.")

    print("Inside the chest, you find a map, a candle, and a smal dagger.")

    choice3 = float(input("You now reach a long dark corridor with 3 dors at the end. \n 1. The red door \n 2. The blue door \n 3. The green door \n Which door do you open? "))

    if choice3 == 1:
        print("Behind the red door is a room full of old portraits watching you.")
    elif choice3 == 2:
        print("Behind the blue door is a cold room wth a frozen fountain.")
    elif choice3 == 3:
        print("Behind the green door is a greenhouse full of overgrown plants.")
    else:
        print("The doors are all sealed shut, so you force you way through a crack in the wall.")

    choice4 = float(input("A ghostly figure appears and offers you 3 choices before it will let you pass. \n 1. Answer its riddle \n 2. Offer it the candle from the chest \n 3. Run past it \n What do you do? "))

    if choice4 == 1:
        print("You answer the riddle correctly and the ghost bows before fading away.")
    elif choice4 == 2:
        print("The ghost takes the candle happily and drifts aside to let you pass.")
    elif choice4 == 3:
        print("You sprint past the ghost, and it howls but does not follow.")
    else:
        print("The ghost stares at you silently, then simply vanishes.")

    choice5 = float(input("You reach the final room. There is a large door with 3 symbols carved into it. \n 1. Press the sun symbol \n 2. Press the moon symbol \n 3. Press the star symbol \n Which symbol do you press? "))

    if choice5 == 1:
        print("The sun symbol glows bright and the door swings open into sunlight.")
    elif choice5 == 2:
        print("The moon symbol glows softly and the door opens into a cool night breeze.")
    elif choice5 == 3:
        print("The star symbol sparkles and the door opens into a sky full of stars.")
    else:
        print("None of the symbols react, but the door slowly creaks open regardless.")

    print(name + " you step through the final door and escape the mansion. You win!")
    play_again = input("Would you like to play again? ")
print("Thanks for playing, " + name + "!")
