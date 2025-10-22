import random  

# Create 3 rows (each row is a list with 3 elements)
row1 = ['🏝️', '🏝️', '🏝️']
row2 = ['🏝️', '🏝️', '🏝️']
row3 = ['🏝️', '🏝️', '🏝️']

# Create a 3x3 map containing the three rows
map = [row1, row2, row3]

# Print the initial map
print(f"{row1}\n{row2}\n{row3}")

# Generate random coordinates for the treasure (1 to 3)
x = random.randint(1, 3)
y = random.randint(1, 3)

print("your choise will be with 🚫 and the treasure with ❌")

# Get the position input from the user (column and row)
pos = input("enter the position to put the treasure (column row): ").split()

# Convert the input values to integers
col = int(pos[0])
row = int(pos[1])

# Check if the player's guess matches the random treasure position
if col == x and row == y:
    # Mark the treasure position with an '❌'
    map[row - 1][col - 1] = '❌'
    print(f"{row1}\n{row2}\n{row3}")
else:
    # If the position is incorrect
    print("wrong position")
    print("the correct position is:")

    # Show the player's chosen position using 🚫
    map[row - 1][col - 1] = '🚫'

    # Show the correct treasure position using ❌
    map[y - 1][x - 1] = '❌'

    # Print the map with both symbols visible
    print(f"{row1}\n{row2}\n{row3}")
    print("try again")
