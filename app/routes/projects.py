from fastapi import APIRouter
from fastapi.templating import Jinja2Templates



router = APIRouter()


templates = Jinja2Templates(directory="app/templates")

projects = [
    {
        "name": "Task Manager API",
        "description": "A REST API for managing user tasks with CRUD operations, JWT authentication and user specific task management.",
        "technologies": "Python | FastAPI | MySQL | SQLAlchemy | JWT",
        "github": "https://github.com/bharathkumar7492/fastapi-task-manager"
    },
    {
        "name":"Employee Leave Management API",
        "description": "A backend application for managing employee leave requests with role based access control for employees, managers and administrators.",
        "technologies": "Python | FastAPI | MySQL | SQLAlchemy | JWT",
        "github": "https://github.com/bharathkumar7492/employee-leave-management-api"
    },
    {
        "name":"Expense Tracker",
        "description": "A desktop application for recording, managing and tracking personal expenses with database integration.",
        "technologies": "Python | MySQL | PyQt6",
        "github": "https://github.com/bharathkumar7492/Expense-Tracker-Application"
    },
    {
        "name":"Weather API Application",
        "description": "A desktop weather application that retrieves weather information using an external weather API.",
        "technologies": "Python | PyQt5 | OpenWeatherMap API",
        "github": "https://github.com/bharathkumar7492/Weather-Application"
    },
    {
        "name":"Banking System",
        "description": "A simple Python banking application where users can create an account, log in, deposit money, withdraw money, and check their balance.",
        "technologies": "Python | Dictionaries | Functions | Loops",
        "github": "https://github.com/bharathkumar7492/Banking-Program-Project"
    },
]