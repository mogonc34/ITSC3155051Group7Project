Copied this from FastAPI Project - Frontend

# ITSC-3155 Section-051 Group-7 Final Project User Manual

## 1. Introduction
This project designs, plans, and builds an Online Restaurant Ordering System (OROS), built using FastAPI, MySQL, 
and SQLAlchemy.  The solution provides a RESTful API for managing orders, customers, menu items, and more. The 
project uses SwaggerUI for API/database interaction, eliminating the need for a frontend.  We use GitHub for 
version control and collaborative development.  The project is designed to be easy to use and understand, with 
clear documentation and examples provided.


This manual provides instructions for setting up, running, and interacting with the project.

## 2. Project Overview
This project is an Online Restaurant Ordering System (OROS) built using FastAPI, MySQL, and SQLAlchemy.
It provides a RESTful API for managing orders, customers, menu items, and more. The project uses SwaggerUI
for API interaction and testing, eliminating the need for a frontend.  The solution is near barebones, 
but it is a working solution satisfying requirements of the course project and built using Agile-Scrum framework
building a Product Back Log with (prioritized) User Stories, a Use Case Diagram, a Class Diagram, and an Activity
(with Swim Lanes) Diagram to aid in overall design and work planning leading to the final building of the coding 
solution.  The main objective of the project is to provide a working solution for an Online Restaurant Ordering 
System (OROS) that demonstrates understanding of setup and use of a RESTful API, and database CRUD operations.

No frontend build was required - in order to demonstrate our API-interactive CRUD operations, we use [Uvicorn](https://uvicorn.org),
- an ASGI web server implementation for Python - in conjunction with [SwaggerUI](https://swagger.io/tools/swagger-ui/).

## 3. Prerequisites
Before you begin, ensure yoiu have the following installed on your (local) system:

### 3.1. Development Tools
- [MySQL (Community) and MySQL Workbench](https://www.mysql.com) (or other SQL database client)
- [PyCharm](https://www.jetbrains.com/pycharm/) (or other Python IDE)
- [GitHub](https://www.github.com) (or other version control system)
- [SwaggerUI](https://swagger.io/tools/swagger-ui/) (or other API documentation tool)

### 3.2 Python Libraries
- [FastAPI](https://fastapi.tiangolo.com) - or other Python web framework
- [Pydantic](https://docs.pydantic.dev) - or other data validation library
- [SQLAlchemy](https://www.sqlalchemy.org/) - or other ORM (Object Relational Mapper)
- [SQLModel](https://sqlmodel.tiangolo.com) - or other SQL database interactions
- [PyMySQL](https://pypi.org/project/PyMySQL/) - or other MySQL driver
- [cryptography](https://pypi.org/project/cryptography/) - or other encryption library
- [HTTPX](https://www.python-httpx.org/) - or other HTTP client
- [MagicMock](https://docs.python.org/3/library/unittest.mock.html) - or other mocking library
- [Pytest](https://pytest.org) (or other testing framework)
- [Uvicorn](https://uvicorn.org) (or other ASGI web server)

### 3.3 Assumed User Knowledge
We are making some assumptions with your knowledge as outlined here
''' That you are familiar use of the IDE's command line interface (CLI) to run the project.
	- Familiar with how to use a Python IDE to run and debug the project code. (Project Team used PyCharm or Visual Studio Pro 2022)
	- Familiar with how to use a web browser to access the SwaggerUI interface.
	- Familiar with how to use the FastAPI framework to create and run a web application.
	- Familiar with how to use a SQL database client to interact with the MySQL database.
	- Familiar with how to use a testing framework to run unit tests.

## 4. Cloning the Repository

### 4.1. To clone the repository, use the following command in your terminal:
	```git clone https://github.com/mogonc34/ITSC3155051Group7Project.git cd ITSC3155051Group7Project```
### 4.2. Create and activate a virtual environment:
	```python -m venv .venv/vin/activate```
	```source venv/bin/activate``` (Linux/Mac) or ```venv\Scripts\activate``` (Windows)
### 4.3. Install the required dependencies:
	```pip install -r requirements.txt```

## 5. Set up the MySQL database:
Open MySQL Workbench and create a new database named `onlinerestaurantordersys_db`.
### 5.1. Create the database and tables:
	```sql
	CREATE DATABASE onlinerestaurantordersys_db;
	USE onlinerestaurantordersys_db;
	```

### 5.2. Update the database connection settings in the `main.py` file:
	```python
	DATABASE_URL = "mysql+pymysql://username:password@localhost/onlinerestaurantordersys_db"
	```
[![Group7 OROS docs](api/images/MySQL_db_structure.png)](https://github.com/mogonc34/ITSC3155051Group7Project)


## 6. Running the Project
### 6.1. Start the FastAPI (Uvicorn) server:
```uvicorn main:app --reload```
### 6.2. Access the SwaggerUI interface:
	[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
### 6.3. Use the SwaggerUI interface to interact with the API:
- **GET**: Retrieve data from the API.
- **POST**: Create new records in the database.
- **PUT**: Update existing records in the database.
- **DELETE**: Remove records from the database.
### 6.4. Use the API endpoints to perform CRUD operations:
[![Group7 OROS docs](api/images/Group7_OROS_SwaggerUI_Screen1.png)](https://github.com/mogonc34/ITSC3155051Group7Project)
[![Group7 OROS docs](api/images/Group7_OROS_SwaggerUI_Screen2.png)](https://github.com/mogonc34/ITSC3155051Group7Project)
[![Group7 OROS docs](api/images/Group7_OROS_SwaggerUI_Screen3.png)](https://github.com/mogonc34/ITSC3155051Group7Project)
[![Group7 OROS docs](api/images/Group7_OROS_SwaggerUI_Screen4.png)](https://github.com/mogonc34/ITSC3155051Group7Project)