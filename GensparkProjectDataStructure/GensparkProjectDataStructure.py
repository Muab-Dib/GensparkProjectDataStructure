inventory = {
    "apple": (10, 2.5),
    "banana":(20, 1.2)
    } # We initialize some starting items in the inventory
price = 0 # this is so we can keep track of the price later
itemsToAdd = {} # We have a temporary dictionary to add new items into
try: # A try block in case an error occurs with user inputs
    print("Welcome to the Inventory Manager!")
    while True: # This will repeat indefinitely
        print("The following commands are available: Add, Remove, Display, Total, and Update") # Give the user a list of commands after each iteration
        userComm = input("Please enter a command: ")
        userComm = userComm.lower().capitalize() # We lowercase it first and then capitalize it so everything matches.
        if userComm == "Add": # This checks if we're trying to add an item
            newFruit = input("Add a new item (name,quantity,price): ") # The try except block will run here if someone attempts to add an item that doesn't have the item name, quantity, and price listed.
            newItem = newFruit.split(',') # We split the items based on the commas
            itemsToAdd[newItem[0].strip()] = (newItem[1].strip(), newItem[2].strip()) # store them inside a dictionary. We strip everything here in case the user tries inputting spaces within the commas
        elif userComm == "Remove": # if the user entered the remove command, we prompt them to enter an item to remove.
            removeFruit = input("Remove an item: ") # user prompt
            if removeFruit in inventory: # we check if its in the inventory
                del inventory[removeFruit] # if so, then we remove the key and values associated with it from the dictionary
        elif userComm == "Update": # If we call update, we add it to our inventory
            for i in itemsToAdd: # for each item in our temp dictionary, we update our inventory
                inventory.update(itemsToAdd)
            print("Updated inventory:") # show the updated inventory
            for i in inventory: # prints the details of the new inventory
                print(f"Item: {i}, Quantity: {inventory[i][0]}, Price: ${inventory[i][1]}")
            itemsToAdd.clear() # remove everything from the temp dictionary
        elif userComm == "Display": # Prints out the display 
            print("Current inventory:") # prints the items currently in our inventory
            for i in inventory: # for each item in our inventory, we print their details out
                print(f"Item: {i}, Quantity: {inventory[i][0]}, Price: ${inventory[i][1]}")
        elif userComm == "Total": # we'll total the price of all items here based on quantity and price
            price = 0 # set the price to 0 if we're totaling again
            for i in inventory: # for each item in our inventory, we multiply the quantity by the price, and add them up
                price += int(inventory[i][0]) * float(inventory[i][1])
            print(f"Total value of inventory: ${price}") # print final price
        else:
            print("Invalid command, please try again.") # user inputs an invalid command
except:
    print("Error, exitting program") # we restart the program if we catch an error.