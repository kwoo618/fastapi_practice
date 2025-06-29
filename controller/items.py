# controller/items.py

from typing import Union
from fastapi import APIRouter

router=APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404:{"descriprion":"Not found"}},
)

@router.get("/{item_id}")
def read_item(item_id:int,q:Union[str,None]=None):
    return {"item_id":item_id,"q":q}