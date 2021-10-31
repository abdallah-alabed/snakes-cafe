"""
This program is to allow customers to view the menu and order from it.
"""

menu="""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""

menuItems=[{"Appetizers":["Wings","Cookies","Spring Rolls"]},
{"Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"]},
{"Desserts":["Ice Cream","Cake","Pie"]},
{"Drinks":["Coffee","Tea","Unicorn Tears"]}]

counter={}

def ordering():
    order=input("> ")
    
    while order:
        if order != "quit":
                     
           if order in counter:
               counter[order]+=1
           else :
                counter[order]=1
           print(f"{counter[order]} order/s of {order} have been added to your meal")
           order=input("> ")

        elif order == "quit":
            print(f"your order:its count-> -> ->  {counter}")
            break
        
    






print(menu)
ordering()