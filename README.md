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

# Restaurant App API Endpoints

## Menu-Items

### Menu-Items List
- URL: `http://127.0.0.1:8000/restaurant/menu-items`
- Method: GET

### Menu-Items Retrieve
- URL: `http://127.0.0.1:8000/restaurant/menu-items/5`
- Method: GET

### Menu-Items Create
- URL: `http://127.0.0.1:8000/restaurant/menu-items`
- Method: POST
- Body:
  ```json
  {
      "title": "Kale Guacamole",
      "category": "Appetizers",
      "price": 12.5
  }
  ```

### Menu-Items Update
- URL: `http://127.0.0.1:8000/restaurant/menu-items/1`
- Method: PATCH
- Body:
  ```json
  {
      "title": "Kale Guacamole With Redberry"
  }
  ```

### Menu-Items Delete
- URL: `http://127.0.0.1:8000/restaurant/menu-items/1`
- Method: DELETE
- Body:
  ```json
  {
      "title": "Cheeseburger Beef",
      "category": "Main",
      "price": 15.99
  }
  ```
  
Please provide the next chunk of JSON data.
Sure, I understand your task. Based on the JSON data you've provided, here are the endpoints that I have found:

## Restaurant App
### Menu Items
- GET /restaurant/menu-items - retrieve a list of all menu items
- GET /restaurant/menu-items/{id} - retrieve a specific menu item by ID
- POST /restaurant/menu-items - create a new menu item
- PATCH /restaurant/menu-items/{id} - update a specific menu item by ID
- DELETE /restaurant/menu-items/{id} - delete a specific menu item by ID

## Booking App
### Cart
- GET /restaurant/cart/menu-items - retrieve a list of all menu items in the cart
- GET /restaurant/cart/menu-items/{id} - retrieve a specific menu item in the cart by ID
- POST /restaurant/cart/menu-items - add a new menu item to the cart
- PATCH /restaurant/cart/menu-items/{id} - update a specific menu item in the cart by ID
- DELETE /restaurant/cart/menu-items - remove all menu items from the cart

Please let me know if there's anything else you'd like me to do.



# API Endpoints

## Restaurant App
### Cart
- **GET** `/restaurant/cart/menu-items` - Get a list of menu items in the cart
- **GET** `/restaurant/cart/menu-items/{id}` - Get a specific menu item in the cart
- **POST** `/restaurant/cart/menu-items` - Add a new menu item to the cart
- **PATCH** `/restaurant/cart/menu-items/{id}` - Update a specific menu item in the cart
- **DELETE** `/restaurant/cart/menu-items` - Remove a menu item from the cart

### Category
- **GET** `/restaurant/category` - Get a list of categories
- **GET** `/restaurant/category/{id}` - Get a specific category
- **POST** `/restaurant/category` - Add a new category
- **PATCH** `/restaurant/category/{id}` - Update a specific category
- **DELETE** `/restaurant/category` - Remove a category


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

## API Endpoints

### Restaurant App

#### Categories

- **Category List**
  - Method: GET
  - URL: `http://127.0.0.1:8000/restaurant/category`
- **Category Retrieve**
  - Method: GET
  - URL: `http://127.0.0.1:8000/restaurant/category/1`
  - Headers: 
    - `Authorization: Token 77dba0dcf70aada8f11c925557f086029aa36fbc`
- **Category Create**
  - Method: POST
  - URL: `http://127.0.0.1:8000/restaurant/category`
- **Category Update**
  - Method: PATCH
  - URL: `http://127.0.0.1:8000/restaurant/category/1`
  - Headers: 
    - `Authorization: Token 21850f59d0e5e04633d0679f8b019dd9ea313855`
  - Request Body:
    ```
    {
        "title": "Main"
    }
    ```
- **Category Delete**
  - Method: DELETE
  - URL: `http://127.0.0.1:8000/restaurant/category`

#### Orders

- **Order List**
  - Method: GET
  - URL: `http://127.0.0.1:8000/restaurant/orders`
- **Order ID Retrieve**
  - Method: GET
  - URL: `http://127.0.0.1:8000/restaurant/orders/1`
  - Headers: 
    - `Authorization: Token cdb01f3ff19f5373a7bbe8e461bf4d3c591c852e`
- **Order Create**
  - Method: POST
  - URL: `http://127.0.0.1:8000/restaurant/orders`
- **Order Update**
  - Method: PATCH
  - URL: `http://127.0.0.1:8000/restaurant/orders/1`
  - Headers: 
    - `Authorization: Token 9dd8b645a583b5953d457317566960a842de385d`
  - Request Body:
    ```
    {
        "status": "True",
        "delivery_crew": "delivery_1"
    }
    ```
- **Order Delete**
  - Method: DELETE
  - URL: `http://127.0.0.1:8000/restaurant/orders/1`







# Restaurant App API Endpoints

## Orders

### List all orders
- URL: `/restaurant/orders`
- Method: `GET`

### Retrieve order by ID
- URL: `/restaurant/orders/:id`
- Method: `GET`
- Authentication required: Yes
- Authorization required: Yes

### Create new order
- URL: `/restaurant/orders`
- Method: `POST`

### Update order
- URL: `/restaurant/orders/:id`
- Method: `PATCH`
- Authentication required: Yes
- Authorization required: Yes

### Delete order
- URL: `/restaurant/orders/:id`
- Method: `DELETE`

# Booking App API Endpoints

## Groups

### List all groups
- URL: `/auth/group`
- Method: `GET`

### List all users in all groups
- URL: `/auth/groups/all/users`
- Method: `GET`

### List all users in manager group
- URL: `/auth/groups/manager/users`
- Method: `GET`

### Create new user in manager group
- URL: `/auth/groups/manager/users`
- Method: `POST`

### Delete user from manager group
- URL: `/auth/groups/manager/users/:id`
- Method: `DELETE`

### Update user in manager group
- URL: `/auth/groups/manager/users/:id`
- Method: `PATCH`

### List all users in delivery-crew group
- URL: `/auth/groups/delivery-crew/users`
- Method: `GET`

### Create new user in delivery-crew group
- URL: `/auth/groups/delivery-crew/users`
- Method: `POST`

### Delete user from delivery-crew group
- URL: `/auth/groups/delivery-crew/users/:id`
- Method: `DELETE`


To document the API endpoints for the Django website with the `restaurant_app` and `booking_app` applications, we can use the following format in the README.md file:

## API Endpoints

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
