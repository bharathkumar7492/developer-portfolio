from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.routes.projects import projects



router = APIRouter()

# jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@router.get("/", include_in_schema=False, name="home")
def home(request: Request):
    return templates.TemplateResponse(request,
                                      "index.html",
                                      {
                                        "title": "Bharathkumar | Software Developer",
                                       "projects": projects,
                                       "success": request.query_params.get("success"),
                                       "error": request.query_params.get("error")
                                       })