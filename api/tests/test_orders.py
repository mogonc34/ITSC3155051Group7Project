from fastapi.testclient import TestClient
import pytest
from unittest.mock import MagicMock
from ..controllers import orders as controller
from ..main import app
from ..models import order as order_model, customer as customer_model

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
        customer_id=1,
        name="John Doe",
        email="johndoe@example.com",
        phone_number="123-456-7890",
        address="123 Main St, Anytown, ST USA"
    )


@pytest.fixture
def mock_order(mock_customer):
    # Fixture to mock a order object.
    return order_model.Order(
        order_id=1,
        customer_id=mock_customer.customer_id,
        payment_id = 99,
        order_date = "2025-04-27 22:33:11",
        order_status = "Test Order",
        total_price = 23.57
    )


@pytest.fixture(autouse=True)
def mock_database_connection(mocker):
    # Fixture to mock the database connection.
    mocker.patch("sqlalchemy.create_engine")
      


# -------------  Unit Tests  -----------------
def test_create_order(db_session, mock_customer, mock_order):
    # Test creating an order - Create a sample order
    order_data = {
        "order_id": mock_order.order_id,
        "customer_id": mock_customer.customer_id,
        "order_status": "Test Order"
    }

    # Create a mock order object
    order_object = mock_order(**order_data)

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
    assert created_order.order_status == "Order Create Test Passed"
    db_session.add.assert_called_once_with(order_object)
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once_with(order_object)

# Test database failure during order creation.
def test_create_order_database_failure(db_session, mock_customer, mock_order):
    order_data = {
        "order_id": mock_order.order_id,
        "customer_id": mock_customer.customer_id,
        "order_status": "Test Order",
    }
    order_object = order_model.Order(**order_data)

    # Simulate a database failure
    db_session.commit.side_effect = Exception("Database error")

    # Expect an exception
    with pytest.raises(Exception, match="Database error"):
        controller.create(db_session, order_object)
        
    # Verify add was called but commit failed
    db_session.add.assert_called_once_with(order_object)
    db_session.commit.assert_called_once()
    
# Test the POST endpoint for CREATing orders
def test_post_order_endpoint(db_session, mocker, mock_customer):
    # Mock the controller's create method
    mocker.patch("api.controllers.orders.create", return_value=order_model.Order(order_id=1, 
           customer_id=mock_customer.customer_id, order_status="Test Order"))
    
    # Send a POST request to the endpoint
    response = client.post("/orders/", json={
        "customer_id": mock_customer.customer_id,
        "order_status": "Test Order"
    })

    # Assertions
    assert response.status_code == 201
    assert response.json() == {
        "id": 1, "customer_id": mock_customer.customer_id, "order_status": "Test Order"
    }

# Test the Read (GET) endpoint for orders
def test_review_order_endpoint(db_session, mocker, mock_customer):
    # Mock the controller's read_one method
    mocker.patch("api.controllers.orders.read_one", return_value=order_model.Order(
        order_id=1, customer_id=1, order_status="Test Order"))

    # Send a GET request to the endpoint
    response = client.get("/orders/1")

    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "customer_id": 1, "order_status":  "Test Order"
    }

# Test UPDATing an order (POST) endpoint
def test_update_order(db_session, mocker):
    # Mock the controller's update method
    mocker.patch("api.controllers.orders.update", return_value=order_model.Order(
        order_id=1, customer_id=1, order_status="Unit Test"))

    # Send a PUT request to the endpoint
    response = client.put("/orders/1", json={
        "customer_id": 1,
        "order_status": "Unit Test"
    })

    # Assertions
    assert response.status_code == 200
    assert response.json() == {
        "order_id": 1, "customer_id": 1, "order_status": "Unit Test"
    }

# Test the Clear Cart (DELETE) endpoint for orders
def test_clear_cart_endpoint(db_session, mocker):
    # Mock the controller's read method
    mocker.patch("api.controllers.orders.read", return_value=[order_model.Order(
        order_id=1, customer_id=1, order_status="statusdeleted")])

    # Send a DELETE request to the endpoint
    response = client.delete("/orders/clear_cart")

    # Assertions
    assert response.status_code == 204
    assert response.content == b""


# Test the DELETE endpoint for deleting an order
def test_delete_order_endpoint(db_session, mocker):
    # Mock the controller's delete method
    mocker.patch("api.controllers.orders.delete", return_value=None)

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