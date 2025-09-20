from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session
from typing import List


router = APIRouter()

# api/chats/
@router.get("/")
def chat_health():
    return {"status": "ok"}


@router.get("/recent/", response_model = List[ChatMessageListItem]) # así nos evitamos devolver el id con el get
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage) # sql query
    results = session.exec(query).fetchall()[:10]
    return results


# HTTP POST
# curl -X POST -d '{"message": "Hello world"}' -H "Content-Type: application/jason" http://localhost:8080/api/chats/
@router.post("/", response_model=ChatMessage)
def create_chat_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data = payload.model_dump() # pydantic -> dict
    object_instance = ChatMessage.model_validate(data)
    # ready to store in the db
    session.add(object_instance)
    session.commit()
    session.refresh(object_instance) # ensures id/primary key is added to the object instance
    
    return object_instance
    