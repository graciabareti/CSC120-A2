from typing import Dict, Union, Optional
class ResaleShop:

    # What attributes will it need?

    # How will you set up your constructor?
     # What methods will you need?

    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = {}
        self.itemID= 0
         # You'll remove this when you fill out your constructor

    def buy(self,computer):
        """ Will return the item ID. """
       #global itemID
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
       # return itemID
        

    def update_price(self,item_id: int, new_price: int):
        """ Will update the price of an item or notify whether its not possible."""
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item",item_id, "not found. Cannot update price.")
        

    def sell(self,item_id: int):
        """ Will print out whether an item is available, sold, or not found."""
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        """ Will print out if an item is in inventory."""
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    def refurbish(self,item_id: int, new_os: Optional[str] = None):
        """ Will print out the item if available for refurbishing and if not print that another item needs to be selected."""
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")


   