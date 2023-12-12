# Multi-threaded Web Crawling System

## Overview

This project develops a multi-threaded web crawling system in Python, leveraging several OS-level concepts to enhance efficiency and performance. Designed to perform data scraping from various websites in a respectful and efficient manner, it adheres to robots.txt rules and prioritizes tasks based on content type.

**Key OS concepts utilized include:**

**Multi-threading:** By implementing multi-threading, the crawler can handle multiple tasks simultaneously, significantly improving the speed of data collection. This is crucial for large-scale scraping tasks, where processing each URL sequentially could be time-consuming.

**Concurrency:** The system employs concurrency control mechanisms to handle simultaneous access to shared resources, such as the database. This ensures data integrity and avoids potential issues like race conditions, which are common in multi-threading environments.

**Network Communication:** At its core, the crawler interacts with web servers using network protocols. This involves understanding and efficiently using system-level networking capabilities for sending requests and receiving responses from servers.

**File System Interaction:** The crawler stores fetched data and logs into the file system. Efficient file handling and data storage are essential for managing the vast amounts of data typically collected during web crawling.

These OS concepts are fundamental to creating a robust and efficient web crawling system, enabling it to handle multiple tasks in parallel, manage data and network resources effectively, and operate at a scale needed for comprehensive web scraping.

## Features
- **Robust Web Crawling:** Utilizes `requests` and `BeautifulSoup` for fetching and parsing web content.
- **Multi-threading Support:** Employs `ThreadPoolExecutor` for concurrent crawling tasks.
- **Respect for robots.txt:** Integrates `RobotFileParser` to comply with website scraping policies.
- **Priority Queueing:** Uses `redis` for prioritized task management.
User Authentication: Implements user login and registration using `Flask-Login` and `Flask-WTF`.
Secure Password Handling: Leverages `Flask-Bcrypt` for hashing user passwords.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Git

### Steps
#### 1. Clone the Repository
```
git clone https://github.com/venkateshtantravahi/OsWebScrawler.git

cd OsWebScrawler
```

#### 2. Set Up a Virtual Environment
- Windows:
```
python -m venv venv
venv\Scripts\activate
```
- Linux/Mac:
```
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```
pip install -r requirements.txt
```

#### 4. Set Environment Variables
- Create a `.env` file in the project root directory.
- Set the necessary environment variables (e.g., `SECRET_KEY`).
- For Redis, set `redis_host` and `redis_port` in the `Config` class in `config.py`.

#### 5. Initialize the Flask Application
- Windows:
```
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

- Linux/Mac:
```
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

#### 6. Database Initialization
- In the Flask shell:
```
flask shell
>>> from app import db
>>> db.create_all()
```
This step creates the database tables based on your models.

### Running the Application
After installation, use flask run to start the application.

- before starting the application make sure run the redis-server in terminal by following below command:
```
redis-server
```
- then 
```
-- if we need to debug mode
flask --debug run 
-- else
flask run
```

## Usage

## Components
- **WebCrawler:** The core component for scraping websites.
- **RequestQueue:** Manages crawling tasks with priority handling.
- **LoginForm/RegisterForm:** For user authentication.
- **Config:** Holds configuration settings for the application.

## Database Setup

Our application uses `SQLAlchemy` as an *ORM (Object-Relational Mapping)* tool for database interactions. The database setup is managed within the Flask application context.

#### Models
- The database models are defined in the `models.py` file.
- We have three primary models: `Users`, `CrawledData`, and `Data`. Each model corresponds to a table in the SQLite database.
- `Users` model handles user information and authentication.
- `CrawledData` stores information about each URL crawled by the user.
- `Data` is used for storing generic application data.

#### Configuration
- Database configurations are set in the `app.config.Config` class, located in the main application initialization file.
- The SQLite database is used, with the file `db.sqlite3` located in the project's root directory.

#### Initialization
The database is initialized with the Flask application context in the main `app` initialization file.
We use `db.create_all()` within the application context to create the database tables based on the defined models.
#### Running the Application
- When the Flask application is started (from the entry point script), it imports the `app` and `db` instances and initializes the database.
- This setup ensures that the database is ready to store and retrieve data as the application runs.


Ensure that all configurations in the config module are set correctly before starting the application.


## Logging
"Logging in our application is set up to assist in monitoring and debugging. It captures detailed information about the application's execution, errors, and important state changes. This helps in identifying issues quickly and understanding the behavior of the application under different scenarios. Logs are stored in 'app.log' and also displayed in the console for error-level messages."

## Contribution
We welcome contributions to our project. If you're interested in contributing, please:

- Fork the repository.
- Create a new branch for your feature.
- Commit your changes with clear, descriptive messages.
- Push to the branch and submit a pull request.
- Ensure your code adheres to the project's style and requirements.
- Include unit tests wherever possible.
