## ITSC-3155 Section 051 Group-7 Final Project Technology Stack & Uses

[Meet Group-7](https://raw.githubusercontent.com/mogonc34/ITSC3155051Group7Project/refs/heads/main/group_bio_template/index.html?token=GHSAT0AAAAAADCZBW5E24JYHPUNDRTD3M462AUATRA)

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
- 🔍 [Pydantic](https://docs.pydantic.dev), used by FastAPI, for the data validation and settings management.
- [SQLAlchemy](https://www.sqlalchemy.org/) for the (Object Relational Mapper - ORM).
- 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions.
- 💾 [MySQL (Community) and MySQL Workbench](https://www.mysql.com) as the MySQL database.
- 🚀 [SwaggerUI](https://swagger.io/tools/swagger-ui/) for user interaction (no frontend requirement).
- 💃 [Uvicorn](https://uvicorn.org), web server for SwaggerUI.
- 🐋 [PyCharm](https://www.jetbrains.com/pycharm/) for development .
- ✅ [Pytest](https://pytest.org) for Unit Testing.
- 📦 [GitHub](https://www.github.com) for collaborative development and version control.


### Successful SwaggerUI browser page
[![API docs](api/images/Group7_OROS_SwaggerUI_Screen1.png)(https://github.com/mogonc34/ITSC3155051Group7Project)

### Key API Endpoints
 | Method | Endpoint         | Description                  |
 |--------|------------------|------------------------------|
 | GET    | /orders/         | Retrieve all orders          |
 | POST   | /orders/         | Create a new order           |
 | GET    | /orders/{id}     | Retrieve an order by ID      |
 | PUT    | /orders/{id}     | Update an order by ID        |
 | DELETE | /orders/{id}     | Delete an order by ID        |
 | GET    | /customers/      | Retrieve all customers       |
 | POST   | /customers/      | Create a new customer        |
 | GET    | /customers/{id}  | Retrieve a customer by ID    |
 | PUT    | /customers/{id}  | Update a customer by ID      |
 | DELETE | /customers/{id}  | Delete a customer by ID      |
 | GET    | /menu_items/     | Retrieve all menu items      |
 | POST   | /menu_items/     | Create a new menu item       |
 | GET    | /menu_items/{id} | Retrieve a menu item by ID   |
 | PUT    | /menu_items/{id} | Update a menu item by ID     |

 bring 'Technical Document' over from User Manual

 ### 2.3 Assumed User Knowledge
We are making some assumptions with your knowledge as outlined here.  That you are:
	- familiar use of the IDE's command line interface (CLI) to run the project.
	- familiar with how to use a Python IDE to run and debug the project code. (Project Team used PyCharm or Visual Studio Pro 2022)
	- familiar with how to use a web browser to access the SwaggerUI interface.
	- familiar with how to use the FastAPI framework to create and run a web application.
	- familiar with how to use a SQL database client to interact with the MySQL database.
	- familiar with how to use a testing framework to run unit tests.
	- familiar with how to use a version control system to manage the project code.
	- familiar with how to clone a GitHub repository and set up a local development environment.

## 3. Set up the MySQL database:
Open MySQL Workbench and create a new database named `onlinerestaurantordersys_db`.
### 3.1. Create the database and tables:
```sql
CREATE DATABASE onlinerestaurantordersys_db;
USE onlinerestaurantordersys_db;
```

### 3.2. Update the database connection settings in the `main.py` file:
```python
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{conf.db_user}:{quote_plus(conf.db_password)}@{conf.db_host}:{conf.db_port}/{conf.db_name}?charset=utf8mb4"
```
[![Group7 OROS Docs](../api/images/MySQL_db_structure.png)](https://github.com/mogonc34/ITSC3155051Group7Project)

### 3.3. Update the db config Class in the `config.py` file:
```python
    db_user = "yourlocalhostusername"  # Replace with your MySQL (localhost) user, if different
    db_password = "yourlocalhostpassword"  # Replace with your MySQL (localhost) password
```
[![Group7 OROS Docs](../api/images/MySQL_db_structure.png)](https://github.com/mogonc34/ITSC3155051Group7Project)


