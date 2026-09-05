from strands_agents import Agent
from src.tools import parse_invoice, check_price_anomaly, execute_payment

def build_financial_agent() -> Agent:
    """Initializes the AWS Strands Agent with toolbelt and execution guardrails."""
    tools = [parse_invoice, check_price_anomaly, execute_payment]
    
    agent = Agent(
        name="LifeOpsFinancialAgent",
        instructions=(
            "You are an autonomous financial assistant. Your goal is to inspect recurring "
            "invoices, compare charges against historical baselines to flag price hikes, "
            "and NEVER invoke payment tools without explicit human-in-the-loop validation."
        ),
        tools=tools
    )
    return agent

if __name__ == "__main__":
    agent = build_financial_agent()
    print("✅ LifeOps Financial Agent initialized successfully with AWS Strands toolbelt.")
