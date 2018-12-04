name = 'J Dong'
age = 25 # not a lie
height_in_inches = 70 # inches
height = round(height_in_inches * 2.54)
weight_in_lbs = 180 # lbs
weight = round(weight_in_lbs * 0.45359)
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} cms tall")
print(f"He's {weight} kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teetch are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + height
print(f"If I add {age}, {height}, and {weight} I got {total}")