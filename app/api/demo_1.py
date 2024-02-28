from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.core.templates import templates

router = APIRouter(prefix="/demo1")


@router.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="demo1.jinja")


class Flag(BaseModel):
    flag: str


@router.post("/flag", status_code=201)
def flag(flag: Flag):
    return {"error": None}


@router.get("/junk/{id}")
def junk(id: int):
    return {"user": {"id": id}}
