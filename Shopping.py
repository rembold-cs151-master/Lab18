# Filename: Shopping.py

"""
Program which writes several functions to take the several
given dictionaries and access or select their elements to
determine the overall price of a purchase.
"""


# Store Dictionaries
prices = {
        "apple": 2, 
        "orange": 5, 
        "bread": 3, 
        "pumpkin": 10, 
        "truffle": 50, 
        "toilet paper": 8
        }
stock = {
        "apple": 3, 
        "orange": 5, 
        "bread": 13, 
        "pumpkin": 8, 
        "truffle": 1, 
        "toilet paper": 2
        }

# Consumer Lists
shopping_list_A = {"apple": 2, "pumpkin": 1, "bread": 2, "toilet paper": 3}
shopping_list_B = {"pumpkin": 9, "toilet paper": 10}
shopping_list_C = {"truffle": 1, "orange": 7, "chicken": 2, "apple": 2, "toilet paper": 1}


# Add your buy_the_store function below! Be sure to include a short doc-string!






# Add your buy_list function below! And again, include a doc-string!







if __name__ == '__main__':
    # Some hopefully helpful testing commands
    print(buy_the_store(stock, prices)) # Should be $216

    # print(buy_list(shopping_list_A, stock, prices))
    # print(buy_list(shopping_list_B, stock, prices))
    # print(buy_list(shopping_list_C, stock, prices))
