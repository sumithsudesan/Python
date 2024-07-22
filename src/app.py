from flask import Flask, jsonify
from order_service import order_service_blueprint
from database import init_app
from config import get_config

app = Flask(__name__)

# Load configuration
config = get_config()
app.config.from_object(config)

init_app(app)   # Initialize the database

# Register blueprints
app.register_blueprint(order_service_blueprint)

# Handle resource not found
@app.errorhandler(404)          # Error handlers - 404
def resource_not_found(e):
    return jsonify(error=str(e)), 404

# Handle internal server
@app.errorhandler(500)          # Error handlers - 500
def internal_server_error(e):
    return jsonify(error=str(e)), 500

# Handle bad request
@app.errorhandler(400)          # Error handlers - 400
def bad_request(e):
    return jsonify(error=str(e)), 400

# main function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.ORDER_SERVICE_HTTP_PORT)
