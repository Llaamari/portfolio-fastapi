# Portfolio FastAPI

Portfolio FastAPI is a modern web application that provides user management and task management APIs. This project is built using FastAPI and PostgreSQL and supports full-fledged RESTful APIs for user and task management. The goal is to provide users with the ability to easily manage projects and tasks.

## Technologies and Tools

- **FastAPI** – A modern, fast web application framework.
- **SQLAlchemy** – ORM for database management.
- **PostgreSQL** – Relational database.
- **Docker** – Creating and managing containerized environments.
- **Poetry** – Python dependency management.

## Installation Instructions

The following instructions will help you get your project up and running locally:

### 1. Download and install Poetry

If you don't have Poetry installed yet, you can install it as follows:

- **Windows**:
```bash
  curl -sSL https://install.python-poetry.org | python3 -
```
- **macOS/Linux:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. Clone the project repository

Clone this project from GitHub:
```bash
git clone https://github.com/Llaamari/portfolio-fastapi.git
cd portfolio-fastapi
```

### 3. Install dependencies

Install project dependencies using Poetry:
```bash
poetry install
```

### 4. Run the application with Docker

The application can be run with Docker using the following commands. This command creates and starts the Docker containers:
```bash
docker-compose up --build
```
After this, the application will be available at `http://localhost:8000`.

### 5. Use the API

The API's main pages and documentation are available at the following URL:<br>
http://localhost:8000/docs<br>
FastAPI provides automatically generated Swagger UI documentation for API endpoints.

## API interfaces

### User management

- **POST /auth/login**: Log in using your email address and password.
- **GET /users/me**: Retrieve information about the logged-in user.

### Task management

- **POST /tasks/**: Create a new task.
- **GET /tasks/**: Retrieve all tasks.
- **GET /tasks/{task_id}**: Retrieve a single task based on its ID.

## Testing

The tests are written using the `pytest` testing framework. You can run all tests with the following command:
```bash
poetry run pytest
```

### 1. Creating a testing environment in Docker

```bash
docker-compose exec api pytest
```

## Community participation

You can participate in the project and make improvements or corrections by submitting a pull request on GitHub. All contributions are welcome.

## License

This project is licensed under the MIT License. See the license for more details.