
story : list = [["One day I will visit space. I will build a rocketship that looks like a ", "noun"],
                ["I will ","verb"],
                [" before blasting off in the rocketship.", "end"],
                ]

def main():
    madlibs()
    pass

# Asks questions depending on list length and returns a story
def madlibs():
    
    # Init variables for later use
    answers : list = []
    result : str = ""

    # Asks questions and adds the answer to the answers list
    for x in story:
        if (x[1] is "end"):
            break
        print("Type a " + x[1] + ":")
        answers.append(input())

    # Creates a string with the result story.
    for x in story:
        if (x[1] is "end"):
            result += x[0]
            break
        result += x[0] + answers[story.index(x)]

    # Prints the result
    print(result)
    

# Defines the main function for the file.
if __name__ == "__main__":
    main()