from flask import Blueprint, request, jsonify
from database import get_db
import pymysql
from pymysql import MySQLError

order_service_blueprint = Blueprint('order_service', __name__)

# Place order - POST
@order_service_blueprint.route('/orders', methods=['POST'])
def place_order():
    data = request.json
    if not data or not all(key in data for key in ('user_id', 'item', 'quantity')):
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        db = get_db()     # Get DB
        cursor = db.cursor()

        db.begin()        # Start transaction
        
        # Insert order
        cursor.execute("INSERT INTO orders (user_id, item, quantity) VALUES (%s, %s, %s)",
                       (data['user_id'], data['item'], data['quantity']))

        db.commit()       # Commit transaction  
        return jsonify({'message': 'Order placed successfully'}), 201
    except MySQLError as e:
        db.rollback()     # rollback
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        db.rollback()     # rollback
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Get order - GET
@order_service_blueprint.route('/orders', methods=['GET'])
def get_orders():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'Missing user_id parameter'}), 400

    try:
        db = get_db()     # Get DB
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM orders WHERE user_id = %s", (user_id,))
        orders = cursor.fetchall()
        return jsonify(orders), 200
    except MySQLError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Delete order - DELETE
@order_service_blueprint.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        db = get_db()      # Get DB
        cursor = db.cursor()       

        db.begin()         # Start transaction
        
        cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
        db.commit()        # Commit transaction
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'Order not found'}), 404
        return jsonify({'message': 'Order deleted successfully'}), 200
    except MySQLError as e:
        db.rollback()      # rollback
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        db.rollback()      # rollback
        return jsonify({'error': 'An unexpected error occurred'}), 500