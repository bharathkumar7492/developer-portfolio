from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import home, contact
from app.database import engine, Base
from app.models.contact import Contact



app = FastAPI(
    title="Developer Portfolio",
    description="Personal Portflio Website",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# serve static file
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(home.router)
app.include_router(contact.router)

