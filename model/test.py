from pydantic import BaseModel


class CalcModel(BaseModel):
    result: int = 0
