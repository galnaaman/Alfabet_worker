# README

## Alfabet Worker

Alfabet Worker is a Django application that sends notifications to the RabbitMQ. It's designed to notify participants about upcoming events.

## Requirements

- Python 3.9
- Django 4.2.9
- RabbitMQ
- PostgreSQL

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-repo/alfabet_worker.git
```

2. Navigate to the project directory:

```bash
cd alfabet_worker
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The application uses environment variables for configuration. You can set these variables in your environment, or create a `.env` file in the project root with the following variables:

- `DEBUG`: Set to `False` in production.
- `ALLOWED_HOSTS`: A list of strings representing the host/domain names that this Django site can serve.
- `POSTGRES_DB`: The name of your PostgreSQL database.
- `POSTGRES_USER`: The username of your PostgreSQL database.
- `POSTGRES_PASSWORD`: The password of your PostgreSQL database.
- `POSTGRES_HOST`: The host of your PostgreSQL database.
- `POSTGRES_PORT`: The port of your PostgreSQL database.
- `RABBITMQ_HOST`: The host of your RabbitMQ server.
- `RABBITMQ_PORT`: The port of your RabbitMQ server.
- `RABBITMQ_USERNAME`: The username of your RabbitMQ server.
- `RABBITMQ_PASSWORD`: The password of your RabbitMQ server.

## Running the Application

You can run the application using the following command:

```bash
gunicorn alfabet_worker.wsgi:application --bind 0.0.0.0:8000
```

This will start a Gunicorn server with your Django application. The `--bind` option tells Gunicorn to bind to all available network interfaces at port 8000.

## Docker

You can also run the application using Docker. Build the Docker image using the following command:

```bash
docker build -t alfabet_worker .
```

Then, run the Docker container:

```bash
docker run -p 8000:8000 alfabet_worker
```

## Functionality

The application includes a worker that sends notifications about upcoming events to RabbitMQ. The worker checks for events that are starting within the next 30 minutes and sends a notification for each event. The notifications include the event ID, name, start time, end time, and a list of participant emails.

The worker runs every 60 seconds. You can adjust this interval by modifying the `scheduler.add_job` call in `worker/worker.py`.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.