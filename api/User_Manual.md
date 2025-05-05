Copied this from FastAPI Project - Frontend

# ITSC-3155 Section-051 Group-7 Final Project User Manual

## 1. Introduction - Project Overview

The Online Restaurant Ordering System (OROS) is a RESTful API-based solution that provides a tool for streamlining a restaurant's
operations and enhance the customer ordering experience while also providing a platform for restaurant owners to manage their
menu items, orders, and promotions. The solution is built using FastAPI, MySQL, and SQLAlchemy, and is designed to be easy to use
and understand. The API implements features for managing orders, customers, menu items, and more. This solution uses a SwaggerUI, 
instead of a front-end UI, for User-interaction. The below User Manual is provided to help users to use the solution - whether 
they are a member the Restaurant Staff or an ordering Custumer. The solution is designed to be easy to use and understand, with 
clear documentation and examples provided.

### 1.1. Prerequisites / Assumptions
We have made some assumptions, presuming your knowledge as outlined here.  That you are:
	- the machine you the SwaggerUI instantiated and ready for your to use (see below).
If the SwaggerUI is not instantiated, you will need to refer to the Technical Document for steps to do do so, including implementing
the MySQL server as well.  troubleshooting steps which walks you thru the process of setting up the project,
to get the SwaggerUI to work.  The Technical Document also provides a detailed overview of the project, including the technology stack used,
the database schema, and the API endpoints.

## 2. Customer
### 2.1. Creating an Account
#### 2.1.1: To create an account, from the SwaggerUI menu, select Post /customers/ Create Customer to expand the option.
[![Group7 OROS Docs](../api/images/SwaggerUI_SelectCreateCustomer.png)](https://github.com/mogonc34/ITSC3155051Group7Project)
#### 2.1.2: Click Try It Out in the upper right (highlighted here:
[![Group7 OROS Docs](../api/images/SwaggerUI_CreateCustomerTIO.png)](https://github.com/mogonc34/ITSC3155051Group7Project)
#### 2.1.3: Enter the required information in the fields highlighted here.
**Reminder, make note of your Customer ID, as you will need this to validate or make any changes to your account (2.2).
Once you have entered the required information, click Execute.  The program will create a new customer record with the
information you've provided and assign a new Customer ID.  A "Code 201, Successful Response" in the Responses section after
you've clicked 'Execute' signals that your Customer Account has been created successfully.
[![Group7 OROS Docs](../api/images/SwaggerUI_CreateCustomerExecute.png)](https://github.com/mogonc34/ITSC3155051Group7Project)

### 2.2. Validate Your Customer Account
We'll go ahead and validate your account has been created & stored - click on the Post /customers/{customer_id} Get Customer option,
then click 'Try It Out' and enter your Customer ID in the field (highlighted) provided.  Click 'Execute' and you should see a 
"Code 200, Successful Response" in the Responses section.  Validate your Customer Information is as entered above.
[![Group7 OROS Docs](../api/images/SwaggerUI_GetCustomer.png)](https://github.com/mogonc34/ITSC3155051Group7Project)

Note: if you failed to capture your Customer ID in 2.1.2, you will need to contact the restaurant staff to get your Customer ID.


### 2.2. Placing an Order
To place an order, the customer must provide their account information, the menu items they wish to order, and their payment information. The API will validate the input and create a new order record in the database.
### 2.3. Viewing Order Status
To view the status of an order, the customer must provide their order ID. The API will retrieve the order status from the database and return it to the customer.
### 2.4. Updating Account Information
To update account information, the customer must provide their account ID and the new information they wish to update. The API will validate the input and update the customer record in the database.
### 2.5. Deleting an Account
To delete an account, the customer must provide their account ID. The API will validate the input and delete the customer record from the database.
### 2.6. Viewing Menu Items
To view the menu items, the customer can make a GET request to the API. The API will retrieve the menu items from the database and return them to the customer.
### 2.7. Viewing Promotions
To view the promotions, the customer can make a GET request to the API. The API will retrieve the promotions from the database and return them to the customer.
### 2.8. Viewing Order History
To view the order history, the customer can make a GET request to the API. The API will retrieve the order history from the database and return it to the customer.
### 2.9. Viewing Customer Information
To view customer information, the customer can make a GET request to the API. The API will retrieve the customer information from the database and return it to the customer.
### 2.10. Updating Order Information
To update order information, the customer must provide their order ID and the new information they wish to update. The API will validate the input and update the order record in the database.
### 2.11. Deleting an Order
To delete an order, the customer must provide their order ID. The API will validate the input and delete the order record from the database.
### 2.12. Viewing Order Details
To view the details of an order, the customer must provide their order ID. The API will retrieve the order details from the database and return them to the customer.

## 3. Restaurant Staff
### 3.1. Creating a Menu Item
To create a menu item, the restaurant staff must provide the item name, description, price, and category. The API will validate the input and create a new menu item record in the database.
### 3.2. Updating a Menu Item
To update a menu item, the restaurant staff must provide the item ID and the new information they wish to update. The API will validate the input and update the menu item record in the database.
### 3.3. Deleting a Menu Item
To delete a menu item, the restaurant staff must provide the item ID. The API will validate the input and delete the menu item record from the database.
### 3.4. Viewing Menu Items
To view the menu items, the restaurant staff can make a GET request to the API. The API will retrieve the menu items from the database and return them to the restaurant staff.
### 3.5. Creating a Promotion
To create a promotion, the restaurant staff must provide the promotion name, description, start date, end date, and discount percentage. The API will validate the input and create a new promotion record in the database.
### 3.6. Updating a Promotion
To update a promotion, the restaurant staff must provide the promotion ID and the new information they wish to update. The API will validate the input and update the promotion record in the database.
### 3.7. Deleting a Promotion
To delete a promotion, the restaurant staff must provide the promotion ID. The API will validate the input and delete the promotion record from the database.
### 3.8. Viewing Promotions
To view the promotions, the restaurant staff can make a GET request to the API. The API will retrieve the promotions from the database and return them to the restaurant staff.
### 3.9. Viewing Order History
To view the order history, the restaurant staff can make a GET request to the API. The API will retrieve the order history from the database and return it to the restaurant staff.
### 3.10. Viewing Customer Information
To view customer information, the restaurant staff can make a GET request to the API. The API will retrieve the customer information from the database and return it to the restaurant staff.
### 3.11. Viewing Order Details
To view the details of an order, the restaurant staff must provide the order ID. The API will retrieve the order details from the database and return them to the restaurant staff.
### 3.12. Updating Order Information
To update order information, the restaurant staff must provide the order ID and the new information they wish to update. The API will validate the input and update the order record in the database.
### 3.13. Deleting an Order
To delete an order, the restaurant staff must provide the order ID. The API will validate the input and delete the order record from the database.
### 3.14. Viewing Order Status
To view the status of an order, the restaurant staff must provide the order ID. The API will retrieve the order status from the database and return it to the restaurant staff.
### 3.15. Viewing Customer Orders
To view the orders of a customer, the restaurant staff must provide the customer ID. The API will retrieve the customer orders from the database and return them to the restaurant staff.
### 3.16. Viewing Customer Ratings and Reviews
To view the ratings and reviews of a customer, the restaurant staff must provide the customer ID. The API will retrieve the customer ratings and reviews from the database and return them to the restaurant staff.
### 3.17. Viewing Customer Feedback
To view the feedback of a customer, the restaurant staff must provide the customer ID. The API will retrieve the customer feedback from the database and return it to the restaurant staff.
### 3.18. Viewing Customer Order History
To view the order history of a customer, the restaurant staff must provide the customer ID. The API will retrieve the customer order history from the database and return it to the restaurant staff.
### 3.19. Viewing Customer Order Details
To view the details of a customer's order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order details from the database and return them to the restaurant staff.
### 3.20. Viewing Customer Order Status
To view the status of a customer's order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order status from the database and return it to the restaurant staff.
### 3.21. Viewing Customer Order Promotions
To view the promotions applied to a customer's order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order promotions from the database and return them to the restaurant staff.
### 3.22. Viewing Customer Order Payments
To view the payments made by a customer for an order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order payments from the database and return them to the restaurant staff.
### 3.23. Viewing Customer Order Ratings and Reviews
To view the ratings and reviews given by a customer for an order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order ratings and reviews from the database and return them to the restaurant staff.
### 3.24. Viewing Customer Order Feedback
To view the feedback given by a customer for an order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order feedback from the database and return it to the restaurant staff.
### 3.25. Viewing Customer Order History
To view the order history of a customer, the restaurant staff must provide the customer ID. The API will retrieve the customer order history from the database and return it to the restaurant staff.
### 3.26. Viewing Customer Order Details
To view the details of a customer's order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order details from the database and return them to the restaurant staff.
### 3.27. Viewing Customer Order Status
To view the status of a customer's order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order status from the database and return it to the restaurant staff.
### 3.28. Viewing Customer Order Promotions
To view the promotions applied to a customer's order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order promotions from the database and return them to the restaurant staff.
### 3.29. Viewing Customer Order Payments
To view the payments made by a customer for an order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order payments from the database and return them to the restaurant staff.
### 3.30. Viewing Customer Order Ratings and Reviews
To view the ratings and reviews given by a customer for an order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order ratings and reviews from the database and return them to the restaurant staff.
### 3.31. Viewing Customer Order Feedback
To view the feedback given by a customer for an order, the restaurant staff must provide the customer ID and the order ID. The API will retrieve the customer order feedback from the database and return it to the restaurant staff.


With MySQL Server running and the SwaggerUI instantiated, your browser should have a long page menu that looks like this:
[![Group7 OROS Docs](../api/images/Group7_OROSSwaggerUIScreen2.png)](https://github.com/mogonc34/ITSC3155051Group7Project)
[![Group7 OROS Docs](../api/images/Group7_OROSSwaggerUIScreen3.png)](https://github.com/mogonc34/ITSC3155051Group7Project)
[![Group7 OROS Docs](../api/images/Group7_OROSSwaggerUIScreen4.png)](https://github.com/mogonc34/ITSC3155051Group7Project)

If not, refer to the Technical Document for troubleshooting steps which walks you thru the process of setting up the project,
to get the SwaggerUI to work.  The Technical Document also provides a detailed overview of the project, including the technology stack used,
the database schema, and the API endpoints.

, and Before you begin, ensure you have the following installed on your (local) system:


