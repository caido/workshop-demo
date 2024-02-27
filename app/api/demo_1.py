from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.core.templates import templates

router = APIRouter(prefix="/demo1", tags=["posts"])


@router.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="demo1.jinja")


class Flag(BaseModel):
    flag: str


@router.post("/flag", status_code=201)
def post_flag(flag: Flag):
    return {"error": None}
