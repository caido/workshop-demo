import base64
import codecs
import json
from fastapi import APIRouter, Request, Response
from pydantic import BaseModel

from app.core.templates import templates

router = APIRouter(prefix="/demo3")


@router.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name="demo3.jinja")


@router.get("/admin/secret")
def admin_secret(request: Request):
    # Extract auth
    snail_key = request.headers.get("x-snail-key")
    decoded = bytes.fromhex(base64.b64decode(snail_key).decode("utf-8")).decode("utf-8")
    data = json.loads(decoded)

    if data.get("role") == "admin":
        return {
            "flag": codecs.encode("HiddenSnails", "rot_13"),
            "encoding": "ceasar_favourite",
        }
    else:
        return Response(status_code=403)
