# define amount of types of people
types_of_people = 10
# define string variable contains type_of_people inside
x = f"There are {types_of_people} types of people"

# define two string variables
binary = "binary"
do_not = "don't"
# define string variable contains two variables defined above
y = f"Those who know {binary} and thos who {do_not}."

# print out string variables defined above
print(x)
print(y)

# print x and y inside other strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# set up variable hilarious to value False
hilarious = False
# set up a string variable, with space for embeded string
joke_evaluation = "Isn't that joke so funny?! {}"

# format hilarious into joke_evaluation
print(joke_evaluation.format(hilarious))

# set up two string variables
w = "This is the left side of..."
e = "a string with a right side."

# combine two strings together
print(w + e)