from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model
from unittest.mock import MagicMock

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    session = mocker.Mock()
    session.add = mocker.Mock()
    session.commit = mocker.Mock()
    session.refresh = mocker.Mock()
    return session


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_name": "John Doe",
        "description": "Order for Test"
    }

    # Create a mock order object
    order_object = model.Order(**order_data)

    # Mock the database session
    db_session.add = MagicMock()
    db_session.commit = MagicMock()
    db_session.refresh = MagicMock()
    db_session.refresh.return_value = order_object

    mock_order = model.Order(id=1, **order_data)
    db_session.refresh.side_effect = lambda x: setattr(x, "id", 1)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.id == 1
    assert created_order.customer_name == "John Doe"
    assert created_order.description == "Order for Test"
    db_session.add.assert_called_once_with(order_object)
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once_with(order_object)

def test_create_order_database_failure(db_session):
    order_data = {
        "customer_name": "Jane Doe",
        "description": "Order for Test"
    }
    order_data = model.Order(**order_data)

    # Simulate a database failure
    db_session.commit.side_effect = Exception("Database error")

    # Expect an exception
    with pytest.raises(Exception, match="Database error"):
        controller.create(db_session, order_object)
        
    # Verify add was called but commit failed
    db_session.add.assert_called_once_with(order_object)
    db_session.commit.assert_called_once()
    
# Test the POST endpoint for orders
def test_post_order_endpoint(db_session, mocker):
    # Mock the controller's create method
    mocker.patch("controllers.orders.create", return_value=model.Order(id=1, customer_name="John Doe", description="Order for Test"))
    
    # Send a POST request to the endpoint
    response = client.post("/orders/", json={
        "customer_name": "John Doe",
        "description": "Order for Test"
    })

    # Assertions
    assert response.status_code == 201
    assert response.json() == {
        "id": 1, "customer_name": "John Doe", "description": "Order for Test"
    }

# Test the Review (GET) endpoint for orders
def test_review_order_endpoint(db_session, mocker):
    # Mock the controller's read_one method
    mocker.patch("controllers.orders.read_one", return_value=model.Order(
        id=1, customer_name="John Doe", description="Order for Test"))
    # Send a GET request to the endpoint
    response = client.get("/orders/1")
    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "customer_name": "John Doe", "description": "Order for Test"
    }

# Update an order (PUT) endpoint
def test_update_order(db_session, mocker):
    # Mock the controller's update method
    mocker.patch("controllers.orders.update", return_value=model.Order(
        id=1, customer_name="John Doe", description="Updated Order Description"))

    # Send a PUT request to the endpoint
    response = client.put("/orders/1", json={
        "customer_name": "John Doe",
        "description": "Updated Order Description"
    })

    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "customer_name": "John Doe", "description": "Updated Order Description"
    }

# Test the Clear Cart (DELETE) endpoint for orders
def test_clear_cart_endpoint(db_session, mocker):
    # Mock the controller's read method
    mocker.patch("controllers.orders.read", return_value=[model.Order(
        id=1, customer_name="John Doe", description="Order for Test")])
    # Send a DELETE request to the endpoint
    response = client.delete("/orders/clear_cart")
    # Assertions
    assert response.status_code == 204
    assert response.content == b""



def test_delete_order_endpoint(db_session, mocker):
    # Mock the controller's delete method
    mocker.patch("controllers.orders.delete", return_value=None)

    # Send a DELETE request to the endpoint
    response = client.delete("/orders/1")

    # Assertions
    assert response.status_code == 204
    assert response.content == b""


# The following 32-lines are the original skeleton code provided for the course project
# from fastapi.testclient import TestClient
# from ..controllers import orders as controller
# from ..main import app
# import pytest
# from ..models import orders as model

# # Create a test client for the app
# client = TestClient(app)


# @pytest.fixture
# def db_session(mocker):
#     return mocker.Mock()


# def test_create_order(db_session):
#     # Create a sample order
#     order_data = {
#         "customer_name": "John Doe",
#         "description": "Test order"
#     }

#     order_object = model.Order(**order_data)

#     # Call the create function
#     created_order = controller.create(db_session, order_object)

#     # Assertions
#     assert created_order is not None
#     assert created_order.customer_name == "John Doe"
#     assert created_order.description == "Test order"