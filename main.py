"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0.00

# Number of characters.
numChars = 8

# Color of characters.
color = "gold"

# Type of wood.
woodType = "oak"

# Write assignment and if statements here as appropriate.

#Creating Base charge

if charge == 0:
    charge += 35.00


# Find how many number of characters

if numChars > 5: 
    charge += (numChars - 5 ) *4
elif numChars <= 5:
    charge += 0.00
# Find what type of wood they want

if woodType == "oak":
    charge += 20.00
elif woodType == "pine":
    charge += 0.00

#Find what type of coloring for the characters

if color == "black":
    charge += 0.00
if color == "white":
    charge += 0.00
elif color == "gold":
    charge += 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
