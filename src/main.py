from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.llm import LLM  # Your LLM integration module
from src.voice import Voice  # Your Text-to-Speech module

app = FastAPI()

# Initialize LLM and Voice modules
llm = LLM()
voice = Voice()

# Global toggle for voice responses
voice_enabled = False

# Request model for text generation
class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 50
    num_return_sequences: int = 1

# Request model for text-to-speech
class SpeechRequest(BaseModel):
    text: str
    gender: str = "male"

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Allie", "model_name": "ALLEN"}

# Text generation endpoint
@app.post("/generate/")
def generate_text(request: TextGenerationRequest):
    try:
        response = llm.generate(request.prompt, request.max_length, request.num_return_sequences)
        # Speak the response if voice is enabled
        if voice_enabled:
            voice.speak(response[0])
        return {"generated_text": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Toggle voice response
@app.post("/toggle-voice/")
def toggle_voice(enabled: bool):
    global voice_enabled
    voice_enabled = enabled
    return {"voice_enabled": voice_enabled}

# Text-to-speech endpoint
@app.post("/speak/")
def speak(request: SpeechRequest):
    try:
        voice.set_voice(request.gender)
        voice.speak(request.text)
        return {"message": f"Spoken: {request.text}", "gender": request.gender}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add more endpoints as needed...
