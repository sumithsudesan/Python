import os

# For handle the Config
class Config:
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')                        # mysql user
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'Test123!')            # password
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')                   # hostname
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))                     # port
    MYSQL_DB = os.getenv('MYSQL_DB', 'order_db')                        # order_db    
    ORDER_SERVICE_HTTP_PORT = int(os.getenv('ORDER_SERVICE_HTTP_PORT', 8080))   # order service port

# Get config
def get_config():
    return Config()