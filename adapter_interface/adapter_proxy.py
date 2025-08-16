import os
import sys
from dotenv import load_dotenv

load_dotenv()

AGENTS_ROOT = os.getenv("SIMTHINK_AGENTS_ROOT")
if AGENTS_ROOT and AGENTS_ROOT not in sys.path:
    sys.path.insert(0, AGENTS_ROOT)

from simthink_adapter import adapter

def prepare_study(payload: dict) -> dict:
    return adapter.prepare_market_study(payload)

def run_study(temp_id: str, investigation_name: str) -> dict:
    return adapter.run_market_study(temp_id=temp_id, investigation_name=investigation_name)