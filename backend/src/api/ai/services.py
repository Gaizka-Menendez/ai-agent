from .schemas import EmailMessageSchema
from .llms import get_openai_llm

def generate_email_message(query: str) -> EmailMessageSchema:
    
    llm = get_openai_llm().with_structured_output(EmailMessageSchema)
    messages = [
        (
            "system",
            "You are a helpful assistant for research and composing plaintext emails. Do not use markdown in your response."
        ),
        (
            "human", f"{query}. Do not use markdown in your response only plaintext"
        ),
    ]
    
    return llm.invoke(messages)
    
