from art import logo_1
from art import list
from shopping_data import data
from shopping_data import prices
import time
import os


print(logo_1)
print(list)
checkout_loop = 0

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def add_product():
  product = int(input("What product would you like to add? \n"))
  while product > 10:
    print("Invalid input, Please enter a vaild item id (The item id is the number on the left side of the item name))")
    product = int(input("What product would you like to add? \n"))
  quantity = int(input("How many would you like to add? \n"))
  data[product - 1]['item_quantity'] += quantity
  data[product - 1]['item_price'] += quantity * prices[product - 1]['item_price']
  input(f"You have added {quantity} {data[product - 1]['item_name']} (Enter to continue)")

def remove_product():
  product = int(input("What product would you like to remove? \n"))
  while product > 10:
    print("Invalid input, Please enter a vaild item id (The item id is the number on the left side of the item name))")
    product = int(input("What product would you like to remove? \n"))
    
  if data[product - 1]['item_quantity'] > 0:
    quantity = int(input("How many would you like to remove? \n"))
    data[product - 1]['item_quantity'] -= quantity
    data[product - 1]['item_price'] -= quantity * prices[product - 1]['item_price']
    input(f"You have removed {quantity} {data[product - 1]['item_name']} (Enter to continue)")
    for item in data:
      if item['item_quantity'] < 0:
        item['item_quantity'] = 0
        print("You have removed more products than you have in your cart, so your this item will be removed from your cart")
  else:
    input("You don't have this item in your cart (Enter to continue)")
      

  
 
def shopping_list():
  cart_total = 0
  print("Here is your shopping list:")
  for item in data:
    if item['item_quantity'] > 0:
      cart_total += item['item_price']
      print(f"{item['item_quantity']} {item['item_name']} for ${item['item_price']}")
  print(f"Which your total is: ${cart_total}")
  

def checkout():
  total = 0
  print("The products you have ordered are:")
  for item in data:
    if item['item_quantity'] > 0:
      total += item['item_price']
      print(f"{item['item_quantity']} {item['item_name']} for ${item['item_price']}")
  print(f"Which your total is: ${total}")




add_product()
time.sleep(1.5)
clear_console()
print(logo_1)
print(list)
while checkout_loop == 0:

  decision = input("Do you want to add or remove a product, or see your shopping cart, or move to checkout (Add, Remove, Cart, Checkout)? \n").lower()
  while decision != "add" and decision != "remove" and decision !="checkout" and decision !="cart":
    print("Invalid input, Please write Add, Remove or Car or Checkout")
    decision = input("Do you want to add or remove a product, or move to checkout (Add, Remove, Checkout)? \n").lower()
    
  if decision == "add":
    add_product()
    clear_console()
    print(logo_1)
    print(list)
  elif decision == "remove":
    remove_product()
    clear_console()
    print(logo_1)
    print(list)
  elif decision == "cart":
    shopping_list()
    input("Back to shopping?\n")
    clear_console()
    print(logo_1)
    print(list)
  elif decision == "checkout":
    clear_console()
    checkout()
    checkout_loop = 1
    

