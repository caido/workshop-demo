from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from app.core.templates import templates

router = APIRouter(prefix="/demo2")


@router.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="demo2.jinja")


@router.get("/user/{id}/flag")
def false_flag(id: str):
    if id == "49":
        return {"user": {"id": id, "flag": "SoManySnails"}}

    if id == "87":
        return RedirectResponse(url="/demo3/admin/secret")

    return {"user": {"id": id, "flag": f"Wrong ({id}) thing"}}


@router.get("/files/{name}.js")
def js(name: str):
    content = f"console.log('Hello from {name}!');"
    return Response(content=content, media_type="text/javascript")


class Analytic(BaseModel):
    event: str


@router.post("/analytics")
def analytics(event: Analytic):
    return {"error": None}


@router.post("/user/analytics")
def old_path():
    response = RedirectResponse(url="/demo2/analytics")
    return response
