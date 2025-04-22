from fastapi import FastAPI
from pydantic import BaseModel
import re
import nltk
from fastapi.middleware.cors import CORSMiddleware

# Download NLTK data (run once)
nltk.download('punkt')

# Create FastAPI app
app = FastAPI()

# CORS Settings
origins = ["*"] # Allow all origins (can be modified to restrict access)

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Pydantic model for user queries
class UserQuery(BaseModel):
    question: str

@app.post("/chat")
async def chat(query: UserQuery):
    question = query.question.lower()

    # Simple keyword-based response logic
    if re.search(r'\bmath\b', question):
        response = "Sure! I can help with math. What specific topic are you working on?"
    elif re.search(r'\bscience\b', question):
        response = "Science is fascinating! Are you studying physics, chemistry, or biology?"
    elif re.search(r'\bhistory\b', question):
        response = "History is interesting! What period or event are you learning about?"
    else:
        response = "I'm not sure about that. Could you clarify your question?"

    return {"question": query.question, "response": response}

# Run the app using Uvicorn when the script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



