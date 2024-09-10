
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!


def madlib():
    print("Let's create a fun story! Please provide the following words:")

    # Collect inputs from the user
    name = input("")
    adjective = input(" ")
    animal = input(" ")
    place = input("")
    verb = input(" ")
    food = input("")

    # Create the story using an f-string
    story = (f"One day, {name} was walking through the {place} when they saw a very {adjective} {animal}. "
             f"{name} decided to {verb} right away, but the {animal} surprised them by offering some {food} to share! "
             f"Together, they had a wonderful time enjoying the meal in the middle of the {place}.")

    # Display the story
    print("\nHere is your madlib story:")
    print(story)



































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")