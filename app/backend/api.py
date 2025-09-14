from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import get_response_from_ai_agents
from app.config.settings import settings
from app.common.logger import get_logger

logger = get_logger(__name__)
app = FastAPI(title="MULTI AI AGENT")

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

@app.post("/chat")
def chat_endpoint(request: RequestState):
    logger.info(f"Received request for model: {request.model_name}")

    if request.model_name not in settings.ALLOWED_MODEL_NAMES:
        logger.warning("Invalid model name")
        raise HTTPException(status_code=400, detail="Invalid model name")
    
    try:
        # Convert messages list to a single string (if your function expects a string)
        user_query = request.messages[0] if request.messages else ""

        response = get_response_from_ai_agents(
            llm_id=request.model_name,
            query=user_query,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt
        )

        logger.info(f"Successfully got response from AI Agent {request.model_name}")
        return {"response": response}
    
    except Exception as e:
        logger.error("Error occurred during response generation", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get AI response: {str(e)}"
        )
