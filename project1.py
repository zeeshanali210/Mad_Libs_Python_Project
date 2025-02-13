print("Wellcome to the mad libs game")
print("Fill in the blanks create a best story")

name = input("Enter your name: ") 
place = input("Enter your place: ")
adjective = input("Enter the adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
plural_noun = input("Enter plural noun")

mad_lib = f"""
one day {name} decided to visit {place}. It was an {adjective} day, and {name} saw an {animal} that was trying to {verb}.
Suddenly, {name} noticed a group of {plural_noun} nearby, and they all started chering loudly!
it was trully an unforgettable adventure!
"""
print("\n Here is your mad lib story")
print(mad_lib)