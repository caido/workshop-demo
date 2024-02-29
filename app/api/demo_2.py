from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel

from app.core.templates import templates

router = APIRouter(prefix="/demo2")

counter = 0


@router.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="demo2.jinja")


@router.put("/user/flag")
def false_flag():
    global counter
    counter += 1
    return JSONResponse(
        content={"id": counter, "flag": f"This is definitely a real flag ({counter})"},
        status_code=201,
    )


@router.get("/user/{id}/flag")
def flag(id: str):
    if id == "49":
        return JSONResponse(
            content={"user": {"id": id, "flag": "SoManySnails"}}, status_code=418
        )

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
