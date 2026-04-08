import uuid
from datetime import datetime

def create_ticket(issue):
    return {
        "ticket_id": str(uuid.uuid4())[:8],
        "issue": issue,
        "status": "Open",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }