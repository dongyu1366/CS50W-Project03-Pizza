# Project 3

###### Web Programming with Python and JavaScript

This project build an web application for handling a pizza restaurant’s online orders. Users are able to regiter and log in to browse the restaurant’s menu, add items to their cart, and submit their orders. Users can go to cart page to see what are in their carts and go to order page to see their own orders.     
Meanwhile, except having the same permission as ordinary users, superuser can view all existing orders, and change their status.

https://dong-project03-pizza.herokuapp.com/     

## Project structure
The project name is 'pizza', and there are two applications in it, named as orders and users.    
- **orders:** Includes the models to define all meals, and views of all behaviors like add a meal to the cart, delete a meal, placeorder, etc. The most of templates are also here.
- **users:** Includes register ,login and logout views & templates.
- **database:** The project use django default database, SQLite 3.

## All Functionalities
- **Menu:** The web application supports all of the available menu items for [Pinnochio’s Pizza & Subs](http://www.pinocchiospizza.net/menu.html).
- **Adding Items:** Superuser could use Django Admin to add, update, and remove items on the menu. I have already added all of the items from the Pinnochio’s menu into database using the Admin UI.
- **Registration, Login, Logout:** Site users (customers) are able to register for the web application with a username, password, first name, last name, and email address. Customers then are able to log in and log out of the website.
- **Shopping Cart:** Once logged in, users would see a representation of the restaurant’s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” The contents of the shopping would be saved even if a user closes the window, or logs out and logs back in again.
- **Placing an Order:** Once there is at least one item in a user’s shopping cart, they would be able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total (no need to worry about tax!) before placing an order.
- **Viewing Orders:** Users could view the order page to check their own orders. When site administrators(Superuser) log in, a addtional link will appear on navbar, superuser could have access to a page where they can view any orders that have already been placed and change the order status.
- **Personal Touch:** Site administrators can view any orders that have already been placed and mark orders as complete and allowing users to see the status of their pending or completed orders.

## How to run
1. Create a virtual environment and install requirements
$ pip install -r requirements.txt
2. Run the project
$ python manage.py runserver
3. View the web application
Go to homepage: http://127.0.0.1:8000/     
Go to Django Admin: http://127.0.0.1:8000/admin/     

