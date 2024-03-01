from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.core.templates import templates

router = APIRouter(prefix="/demo1")


@router.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="demo1.jinja")


class Flag(BaseModel):
    flag: str


@router.post("/flag")
def flag(request: Request, flag: Flag):
    user_type = request.headers.get("x-snail")
    if user_type == "admin":
        return JSONResponse(
            content={"flag": "SnailsAreCute"},
            status_code=200,
        )
    else:
        return JSONResponse(
            content={"error": "No Flag For You!"},
            status_code=200,
        )


@router.get("/junk/{id}")
def junk(id: int):
    return {"user": {"id": id}}
