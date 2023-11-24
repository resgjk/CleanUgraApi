from pydantic import BaseModel

class ReceiveMsg(BaseModel):
    message: str
