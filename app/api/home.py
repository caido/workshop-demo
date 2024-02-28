from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.core.templates import templates

router = APIRouter()


@router.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="home.jinja")
