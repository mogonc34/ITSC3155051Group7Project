from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import order as model, customer as customer_model
from unittest.mock import MagicMock

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    # Fixture to mock the database session.
    session = mocker.Mock()
    session.add = mocker.Mock()
    session.commit = mocker.Mock()
    session.refresh = mocker.Mock()
    return session


@pytest.fixture
def mock_customer():
    # Fixture to mock a customer object.
    return customer_model.Customer(
        id=1,
        name="John Doe",
        email="johndoe@example.com",
        phone_number="123-456-7890",
        address="123 Main St, Anytown, USA"
    )


# -------------  Unit Tests  -----------------
def test_create_order(db_session, mock_customer):
    # Test creating an order - Create a sample order
    order_data = {
        "customer_id": mock_customer.customer.id,
        "description": "Order for Test"
    }

    # Create a mock order object
    order_object = model.Order(**order_data)

    # Mock the database session
    db_session.add = MagicMock()
    db_session.commit = MagicMock()
    db_session.refresh = MagicMock()
    db_session.refresh.return_value = order_object

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer_id == mock_customer.customer_id
    assert created_order.description == "Order for Test"
    db_session.add.assert_called_once_with(order_object)
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once_with(order_object)

# Test database failure during order creation.
def test_create_order_database_failure(db_session, mock_customer):
    order_data = {
        "customer_id": mock_customer.customer.id,
        "description": "Order for Test"
    }
    order_object = model.Order(**order_data)

    # Simulate a database failure
    db_session.commit.side_effect = Exception("Database error")

    # Expect an exception
    with pytest.raises(Exception, match="Database error"):
        controller.create(db_session, order_object)
        
    # Verify add was called but commit failed
    db_session.add.assert_called_once_with(order_object)
    db_session.commit.assert_called_once()
    
# Test the POST endpoint for CREATing orders
def test_post_order_endpoint(db_session, mocker):
    # Mock the controller's create method
    mocker.patch("controllers.orders.create", return_value=model.Order(id=1, customer_id=mock_customer.customer_id, description="Order for Test"))
    
    # Send a POST request to the endpoint
    response = client.post("/orders/", json={
        "customer_id": mock_customer.customer_id,
        "description": "Order for Test"
    })

    # Assertions
    assert response.status_code == 201
    assert response.json() == {
        "id": 1, "customer_id": mock_customer.customer_id, "description": "Order for Test"
    }

# Test the Read (GET) endpoint for orders
def test_review_order_endpoint(db_session, mocker):
    # Mock the controller's read_one method
    mocker.patch("controllers.orders.read_one", return_value=model.Order(
        id=1, customer_id=1, description="Order for Test"))

    # Send a GET request to the endpoint
    response = client.get("/orders/1")

    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "customer_id": 1, "description": "Order for Test"
    }

# Test UPDATing an order (POST) endpoint
def test_update_order(db_session, mocker):
    # Mock the controller's update method
    mocker.patch("controllers.orders.update", return_value=model.Order(
        id=1, customer_id=1, description="Updated Order Description"))

    # Send a PUT request to the endpoint
    response = client.put("/orders/1", json={
        "customer_id": 1,
        "description": "Updated Order Description"
    })

    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "customer_id": 1, "description": "Updated Order Description"
    }

# Test the Clear Cart (DELETE) endpoint for orders
def test_clear_cart_endpoint(db_session, mocker):
    # Mock the controller's read method
    mocker.patch("controllers.orders.read", return_value=[model.Order(
        id=1, customer_id=1, description="Order for Test")])

    # Send a DELETE request to the endpoint
    response = client.delete("/orders/clear_cart")

    # Assertions
    assert response.status_code == 204
    assert response.content == b""


# Test the DELETE endpoint for deleting an order
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