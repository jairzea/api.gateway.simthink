from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from adapter_interface.adapter_proxy import prepare_study, run_study

app = FastAPI()

class PreparePayload(BaseModel):
    persona: str
    organization_info: str
    user_id: int
    research_goal: str
    product_info: str
    sample_size: int
    use_rag: bool
    rag_ids: object
    investigation_id: str

class RunPayload(BaseModel):
    temp_id: str
    investigation_name: str

@app.post("/prepare")
def prepare(payload: PreparePayload):
    try:
        result = prepare_study(payload.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run")
def run(payload: RunPayload):
    try:
        result = run_study(payload.temp_id, payload.investigation_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))