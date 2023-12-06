from fastapi import APIRouter
from model.test import CalcModel
from helper.test import calc

router = APIRouter(
    prefix="/test",
)


@router.get("calc")
def calc_test(
        a: int,
        b: int,
        c: str,
):
    return calc(a, b, c)
