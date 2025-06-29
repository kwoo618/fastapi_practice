from fastapi import APIRouter

router = APIRouter()

@router.get("/task")
async def list_tast():
    pass   #pass는 아무것도 하지 않는 문장(return 필요없음)

@router.post("/tast")
async def create_task():
    pass

@router.put("/tast/{tast_id}")
async def mark_task_as_done():
    pass

@router.delete("/tast/{task_id}/done")
async def unmark_task_as_done():
    pass