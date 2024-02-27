from fastapi import APIRouter

router = APIRouter(prefix="/demo1", tags=["posts"])


@router.get("/test")
def read_root():
    return {"hello": "world"}
