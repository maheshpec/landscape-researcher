from typing import Optional

from langchain_core.messages import BaseMessage
from pydantic import BaseModel


class State(BaseModel):
    messages: Optional[list[BaseMessage]] = list()
    file_path: Optional[str] = None