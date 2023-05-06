## Starting commands:

* `python3 manage.py makemigrations`: Creates new database migration files based on any changes you've made to your Django models since the last migration.
* `python3 manage.py migrate`: Synchronizes the database schema with the models defined in your Django app.
* `python3 manage.py createinitialdata`: Prepopulates initial data for both Restaurant App and Booking App.
* `python3 manage.py runserver`: Starts the development server on `http://127.0.0.1:8000/`.

Note that these commands assume you're using Python 3 and have already navigated to your Django project directory in the terminal or command prompt. The specific syntax and options may vary depending on the version of Django you're using and the structure of your project.


## Endpoints

baseurl = http://127.0.0.1:8000/

* `admin/`: The admin panel for managing your Django project.
* `auth/register/`: The registration endpoint for creating new user accounts.
* `auth/login/`: The login endpoint for existing users to authenticate themselves.
* `restaurant/`: The endpoint for managing restaurants in your project.
* `booking/`: The endpoint for managing bookings made by customers.
* `auth/users/`: The endpoint for retrieving, updating, and deleting user information.
* `auth/token/login/`: The token authentication endpoint for obtaining an access token.
* `auth/token/logout/`: The token authentication endpoint for revoking an access token.



## erferf


Sure, here's the markdown format for the above JSON chunk:

# API Endpoints

## Restaurant App

### Category
- **GET** `/restaurant/category` - Get a list of categories
- **GET** `/restaurant/category/{id}` - Get a specific category
- **POST** `/restaurant/category` - Add a new category
- **PATCH** `/restaurant/category/{id}` - Update a specific category
- **DELETE** `/restaurant/category/{id}` - Remove a category

### MenuItems
- **GET** `restaurant/menu-items` - Get a list of menu items
- **GET** `restaurant/menu-items/{id}` - Get a specific menu item
- **POST** `restaurant/menu-items` - Add a new menu item
- **PATCH** `restaurant/menu-items/{id}` - Update a specific menu item
- **DELETE** `restaurant/menu-items/{id}` - Remove a menu item

### Cart
- **GET** `/restaurant/cart/menu-items` - Get a list of menu items in the cart
- **GET** `/restaurant/cart/menu-items/{id}` - Get a specific menu item in the cart
- **POST** `/restaurant/cart/menu-items` - Add a new menu item to the cart
- **PATCH** `/restaurant/cart/menu-items/{id}` - Update a specific menu item in the cart
- **DELETE** `/restaurant/cart/menu-items` - Remove a menu item from the cart

### Order
- **GET** `/restaurant/orders` - Get a list of menu items in the cart
- **GET** `/restaurant/orders/{id}` - Get a specific menu item in the cart
- **POST** `restaurant/orders` - Add a new menu item to the cart
- **PATCH** `restaurant/orders/{id}` - Update a specific menu item in the cart
- **DELETE** `restaurant/orders/{id}` - Remove a menu item from the cart



## Booking App
### Reservation
- **GET** `/booking/reservation` - Get a list of reservations
- **GET** `/booking/reservation/{id}` - Get a specific reservation
- **POST** `/booking/reservation` - Add a new reservation
- **PATCH** `/booking/reservation/{id}` - Update a specific reservation
- **DELETE** `/booking/reservation` - Remove a reservation

### Table
- **GET** `/booking/table` - Get a list of tables
- **GET** `/booking/table/{id}` - Get a specific table
- **POST** `/booking/table` - Add a new table
- **PATCH** `/booking/table/{id}` - Update a specific table
- **DELETE** `/booking/table` - Remove a table



## Groups

### List all groups
- **GET** `/auth/group`

### List all users in all groups
- **GET** `/auth/groups/all/users`

### Manager Group
- **GET** `/auth/groups/manager/users` - List all users in manager group: 
- **POST** `/auth/groups/manager/users` - Create new user in manager group: 
- **DELETE** `/auth/groups/manager/users/:id` - Delete user from manager group: 
- **PATCH**  `/auth/groups/manager/users/:id` - Update user in manager group: 

### Delivery-Crew Group
- **GET** `/auth/groups/delivery-crew/users` - List all users in delivery-crew group: 
- **POST** `/auth/groups/delivery-crew/users` - Create new user in delivery-crew group: 
- **DELETE** `/auth/groups/delivery-crew/users/:id` - Delete user from delivery-crew group: 

To document the API endpoints for the Django website with the `restaurant_app` and `booking_app` applications, we can use the following format in the README.md file:




# - - - - - - - - -
## DJOSER Endpoints

### Authentication

- `POST /api-token-auth`: Authenticate a user with a username and password. No authentication required.

### Registration (Djoser)

- `POST /auth/users/`: Register a new user with a username, password, email, first name, last name, and groups. No authentication required.

### Login (Djoser)

- `POST /auth/token/login`: Obtain a token for a user with a username and password. No authentication required.

### Logout (Djoser)

- `POST /auth/token/logout`: Logout a user. Authentication required with a token in the `Authorization` header.

### Account Info (Djoser)

- `GET /auth/users/`: Retrieve information about the authenticated user. Authentication required with a token in the `Authorization` header.

### Manager

- `GET /api/manager`: Retrieve information about the manager. Authentication required with a token in the `Authorization` header.
