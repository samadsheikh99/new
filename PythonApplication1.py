# Create an empty set to store the data
data_set = set()

# Use a while loop to continuously get data from the user
while True:
    user_input = input("Please enter data (or 'exit' to stop): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break
    
    # Add the user's input to the set
    data_set.add(user_input)

# Print the set containing the entered data
print("Data entered by the user:")
for item in data_set:
    print(item)
