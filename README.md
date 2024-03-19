# Provenance Logging Microservice

This is a Python-based microservice that consumes provenance data from a RabbitMQ message queue and logs it to a CouchDB database. The microservice is designed to be part of a larger system, where it can be used to capture and store provenance information for various processes.

## Features

- Consumes provenance data from a RabbitMQ exchange
- Logs the received data to a CouchDB database
- Also logs the data to stdout for debugging purposes
- Utilizes a fanout logger to write to multiple destinations simultaneously
- Dockerized for easy deployment and testing

## Components

### `consume.py`

This is the main script that sets up the microservice. It creates a `CouchLogger` and a `Logger` that writes to stdout. These loggers are combined using a fanout logger, which allows writing to multiple destinations. The script then creates a `Subscriber` instance, which connects to the RabbitMQ exchange and starts consuming messages. The received messages are passed to the fanout logger.

### `couch.py`

This module contains the `CouchLogger` class, which is responsible for logging the provenance data to a CouchDB database. The class connects to the specified CouchDB instance and creates the database if it doesn't exist. The `log` method saves the received entry to the database. The `from_environment` static method allows easy creation of a `CouchLogger` instance using environment variables.

### `docker-compose.yml`

The Docker Compose file is provided for testing purposes. It sets up the microservice along with its dependencies (RabbitMQ and CouchDB). The microservice itself is built from the current directory using the included `Dockerfile`. The RabbitMQ and CouchDB services are configured using environment variables, and healthchecks are set up to ensure the services are running before the microservice starts consuming messages.

## Usage

To use this microservice in a larger project, you would typically deploy it alongside the other components of your system. The microservice expects the following environment variables to be set:

- `COUCHDB_HOST`: The hostname of the CouchDB instance
- `COUCHDB_USER`: The username for accessing CouchDB
- `COUCHDB_PASSWORD`: The password for accessing CouchDB
- `COUCHDB_DB`: The name of the CouchDB database to use
- `RABBITMQ_HOST`: The hostname of the RabbitMQ instance
- `RABBITMQ_USER`: The username for accessing RabbitMQ
- `RABBITMQ_PASSWORD`: The password for accessing RabbitMQ
- `RABBITMQ_EXCHANGE`: The name of the RabbitMQ exchange to consume from

For testing purposes, you can use the provided `docker-compose.yml` file to spin up the microservice along with its dependencies. Make sure to set the required environment variables in the Docker Compose file or in a separate `.env` file.