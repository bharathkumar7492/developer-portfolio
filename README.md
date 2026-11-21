# Developer Portfolio

A personal developer portfolio built using Python, FastAPI, Jinja2, Bootstrap 5, and MySQL.

## Features

- Responsive portfolio website
- About, Skills, Education, and Projects sections
- Dynamic project listing using Jinja2
- Contact form with MySQL database storage
- Contact form success and validation messages
- Downloadable resume
- GitHub and LinkedIn links

## Technologies Used

- Python
- FastAPI
- Jinja2
- HTML, CSS, Bootstrap 5
- MySQL
- SQLAlchemy
- PyMySQL

## Project Structure

## Project Structure

```text
developer_portfolio/
├── app/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   └── static/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```



## Setup Instructions

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```text
   pip install -r requirements.txt
   ```
4. Create a MySQL database named developer_portfolio.
5. Create a .env file using .env.example and configure your database URL.
6. Run the application:
   
   ```text
   uvicorn app.main:app --reload
   ```
7. ```text
    Open http://127.0.0.1:8000
    ```

### Author

Bharathkumar Ravi
- GitHub: https://github.com/bharathkumar7492
- LinkedIn: https://www.linkedin.com/in/bharathkumar7492/
