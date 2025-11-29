
from fastapi import APIRouter

router = APIRouter(prefix="/autocomplete", tags=["autocomplete"])

@router.post("")
async def autocomplete(payload: dict):
    code = payload.get("code","")
    if code.strip().endswith("pri"):
        return {"suggestion": "print('Hello World')"}
    elif "def" in code:
        return {"suggestion": "    pass"}
    return {"suggestion": "# continue typing..."}
