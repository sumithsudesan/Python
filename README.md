# Order Service

The Order Service is a microservice for managing orders, implemented using Python and Flask. It interacts with a MySQL database for data persistence and uses various Python libraries for its functionality.

## Features

- **HTTP Service**: Accepts JSON data for order management operations.
- **Endpoints**:
  - **Place Order**: Allows users to place orders.
  - **Get Order List**: Retrieves a list of orders associated with the user.
  - **Delete Order**: Deletes an order based on order ID.
- **Database**: Communicates with a MySQL database to store and retrieve order data.
- **Configuration**: Reads configuration from a ConfigMap for database and service details.

## Technology Stack

- **Language**: Python
- **Framework**: Flask
- **Libraries**:
  - `Flask`: Web framework for building the RESTful API.
  - `PyMySQL`: MySQL client library for connecting to the MySQL database.
  - `pytest`: Testing framework for Python.
- **Database**: MySQL
- **Configuration Management**: Kubernetes ConfigMap for managing environment variables.