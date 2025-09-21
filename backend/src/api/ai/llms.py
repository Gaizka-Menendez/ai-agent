import os
from langchain_openai import ChatOpenAI
from .schemas import EmailMessageSchema


OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL") or None
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or None
OPENAI_MONEL_NAME = os.getenv("OPENAI_MONEL_NAME") or "gpt-4o-mini"
if not OPENAI_API_KEY:
    raise NotImplementedError("'OPENAI_API_KEY' was not implemented")




# llm_base = ChatOpenAI(**openai_params)
# llm_base = ChatOpenAI(
#     model_name=OPENAI_MONEL_NAME,
#     api_key=OPENAI_API_KEY,
#     base_url=OPENAI_BASE_URL
# )

def get_openai_llm():
    openai_params = {
        "model": OPENAI_MONEL_NAME,
        "api_key": OPENAI_API_KEY
    }

    if OPENAI_BASE_URL:
        openai_params["base_url"] = OPENAI_BASE_URL
        
    return ChatOpenAI(**openai_params)

# llm = llm_base.with_structured_output(EmailMessageSchema)