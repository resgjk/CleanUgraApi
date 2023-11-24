from pydantic import BaseModel

class ReceiveMsg(BaseModel):
    msg: str
