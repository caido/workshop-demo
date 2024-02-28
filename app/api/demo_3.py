from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.core.templates import templates

router = APIRouter(prefix="/demo3")


@router.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="demo3.jinja")
