# Handle contact form submissions separately from homepage route.

from fastapi import APIRouter, Form, Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.database import get_db
from app.models.contact import Contact




router = APIRouter()


@router.post("/contact")
def sumbit_contact(name: str = Form(...),
                   email: str = Form(...),
                   message: str = Form(...), 
                   db: Session = Depends(get_db)):
    
    name = name.strip()
    email = email.strip()
    message = message.strip()
    
    if not name or not email or not message:
        return RedirectResponse(url="/?error1#contact", status_code=303)
    
    contact = Contact(name=name,
                      email=email, 
                      message=message)
    
    db.add(contact)
    db.commit()
    
    return RedirectResponse(url="/?success=1#contact", status_code=303)