import random

def main():
    dice()


def dice():
    isPlaying : bool = True
    while (isPlaying):
        print("Type 'r' to roll the dice.")
        userInput : str = input()
        if (userInput.lower() == "r"):
            target : int = random.randint(1,6)
            print(" -\n|"+ str(target) +"|\n -")
        else:
            print("Thanks for rolling!")
            isPlaying = False


# Defines the main function for the file.
if __name__ == "__main__":
    main()