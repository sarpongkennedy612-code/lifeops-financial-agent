from strands_agents import tool
from typing import Dict, Any

@tool
def parse_invoice(bill_text: str) -> Dict[str, Any]:
    """Extracts vendor name, billing amount, and due date from bill text or invoice data."""
    return {
        "vendor": "CloudSaaS Hosting",
        "amount": 49.99,
        "billing_period": "September 2026",
        "due_date": "2026-09-15"
    }

@tool
def check_price_anomaly(vendor: str, current_amount: float) -> Dict[str, Any]:
    """Compares current bill against historical baseline memory to detect unwanted price hikes."""
    historical_baseline = 29.99
    price_diff = round(current_amount - historical_baseline, 2)
    has_price_hike = price_diff > 0.0
    return {
        "vendor": vendor,
        "historical_baseline": historical_baseline,
        "current_amount": current_amount,
        "price_increase": price_diff,
        "flagged_for_human_review": has_price_hike
    }

@tool
def execute_payment(vendor: str, amount: float, human_approved: bool) -> Dict[str, Any]:
    """Safely executes payment ONLY if human-in-the-loop approval is explicitly verified."""
    if not human_approved:
        return {
            "status": "PAUSED",
            "message": f"Payment of ${amount:.2f} to {vendor} BLOCKED. Requires human approval."
        }
    return {
        "status": "SUCCESS",
        "message": f"Payment of ${amount:.2f} to {vendor} executed safely following human validation.",
        "transaction_id": "TXN-2026-88912"
    }
