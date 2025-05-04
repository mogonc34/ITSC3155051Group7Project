Copied this from FastAPI Project - Frontend

# ITSC-3155 Section-051 Group-7 Final Project User Manual

## 1. Introduction
This project is an Online Restaurant Ordering System (OROS) built using FastAPI, MySQL, and SQLAlchemy. 
It provides a RESTful API for managing orders, customers, menu items, and more. The project uses SwaggerUI 
for API interaction and testing, eliminating the need for a frontend.

This manual provides instructions for setting up, running, and interacting with the project.

## 2. Project Overview
This project is an Online Restaurant Ordering System (OROS) built using FastAPI, MySQL, and SQLAlchemy.
It provides a RESTful API for managing orders, customers, menu items, and more. The project uses SwaggerUI
for API interaction and testing, eliminating the need for a frontend.  Yes, it should be considered barebones, 
but it is a working project that meets the requirements of the course - to demonstrate understanding of setup, 
use of a RESTful API, and CRUD operations.  The project is designed to be easy to use and understand, with 
clear documentation and examples provided.

## 3. Prerequisites
Before you begin, ensure yoiu have the following installed on your (local) system:

### 3.1. Development Tools
- [MySQL (Community) and MySQL Workbench](https://www.mysql.com) (or other SQL database client)
- [PyCharm](https://www.jetbrains.com/pycharm/) (or other Python IDE)
- [GitHub](https://www.github.com) (or other version control system)

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
- [SwaggerUI](https://swagger.io/tools/swagger-ui/) (or other API documentation tool)
- [Uvicorn](https://uvicorn.org) (or other ASGI web server)

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
 
Due to project timelines, no frontend build was required.  Instead [Uvicorn](https://uvicorn.org), an ASGI web server implementation for Python, has been 
used in conjunction with [SwaggerUI](https://swagger.io/tools/swagger-ui/) is substituted for scaled-down frontend Interactions.

## Project Implementation

Before you begin, you will need to install:
	- [PyCharm](https://www.jetbrains.com/pycharm/) (or other Python IDE)
	- [MySQL (Community) and MySQL Workbench](https://www.mysql.com) (or other SQL database client)
	- [Pydantic](https://docs.pydantic.dev) (or other data validation library)
	- [SQLAlchemy](https://www.sqlalchemy.org/) (or other ORM)
	- [SQLModel](https://sqlmodel.tiangolo.com) (or other SQL database interactions)
	- 
	- pymysql (or other MySQL driver)
	- cryptography (or other encryption library)
	- httpx (or other HTTP client)
	- MagicMock (or other mocking library)
	- [Pytest](https://pytest.org) (or other testing framework)
	- [SwaggerUI](https://swagger.io/tools/swagger-ui/) (or other API documentation tool)
	- [Uvicorn](https://uvicorn.org) (or other ASGI web server)


With the above tools installed, and properly instantiated, you should seetart the project

### Assumed User Knowledge
use the command line interface (CLI) to run the project.
	- Familiar with how to use a Python IDE to run and debug the project code. (Project Team used PyCharm or Visual Studio Pro 2022)
	- Familiar with how to use a web browser to access the SwaggerUI interface.
	- Familiar with how to use the FastAPI framework to create and run a web application.
	- Familiar with how to use a SQL database client to interact with the MySQL database.
	- Familiar with how to use a testing framework to run unit tests.

To implement this project, you will need to understand
	- Familiar with how to 