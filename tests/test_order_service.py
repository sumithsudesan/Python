import pytest
from flask import Flask, jsonify
from src.order_service import order_service_blueprint
from src.database import init_app
from src.config import get_config

# Create client
@pytest.fixture
def client():
    app = Flask(__name__)
    # get config
    config = get_config()
    app.config.from_object(config)
    
    # Initalise DB
    init_app(app)
    app.register_blueprint(order_service_blueprint)

    # 
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify(error=str(e)), 500

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error=str(e)), 400

    with app.test_client() as client:
        yield client

# Test case - Place order
def test_place_order(client):
    response = client.post('/orders', json={'user_id': 1, 'item': 'item1', 'quantity': 2})
    # Validate response
    assert response.status_code == 201
    assert response.json['message'] == 'Order placed successfully'

    # Invalid input data
    response = client.post('/orders', json={})
    # Validate response
    assert response.status_code == 400

# Test case - Get order
def test_get_orders(client):
    response = client.get('/orders', query_string={'user_id': 1})
    # Validate response
    assert response.status_code == 200

# Test case - Delete order
def test_delete_order(client):
    # Assuming there's already an order with id 1 in the test database
    response = client.delete('/orders/1')

    # Validate response
    assert response.status_code == 200      
    assert response.json['message'] == 'Order deleted successfully'