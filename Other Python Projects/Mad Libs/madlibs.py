"""
This program fills in the blanks in a Mad Libs game after prompting the user for input.
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print("The Mad Libs game has started!")

name = input("Enter a name: ")
adj1 = input("Enter a adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter one last adjective: ")
v = input("Enter a verb: ")
n1 = input("Enter a noun: ")
n2 = input("Enter another noun: ")
animal = input("Enter a animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

print(STORY % (name, adj1, adj2, animal, food, v, n1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, n2))