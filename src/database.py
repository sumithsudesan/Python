import pymysql
from flask import current_app, g
from pymysql import MySQLError

# Get database connection
def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            user=current_app.config['MYSQL_USER'],          # User
            password=current_app.config['MYSQL_PASSWORD'],  # Password
            host=current_app.config['MYSQL_HOST'],          # host
            port=current_app.config['MYSQL_PORT'],          # Port
            database=current_app.config['MYSQL_DB'],        # database
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

# Close database connection
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Initalised DB
def init_app(app):
    app.teardown_appcontext(close_db)
   
    with app.app_context():  # Initialize the database
        db = get_db()
        cursor = db.cursor()
       
        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            item VARCHAR(255) NOT NULL,
            quantity INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')                # Create the orders table if it does not exist
        db.commit()
