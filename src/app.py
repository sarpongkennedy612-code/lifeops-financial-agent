import streamlit as st
from src.agent import build_financial_agent
from src.tools import parse_invoice, check_price_anomaly, execute_payment

st.set_page_config(page_title="LifeOps Financial Agent", page_icon="💳", layout="wide")

st.title("💳 LifeOps Financial Guardrail Agent")
st.caption("Powered by AWS Strands Agents & AWS Bedrock AgentCore")

st.markdown("---")

st.subheader("1. Invoice Ingestion & Audit")
invoice_input = st.text_area(
    "Paste invoice text or raw receipt:",
    value="CloudSaaS Hosting - Monthly Subscription - Amount: $49.99 - Date: Sep 2026"
)

if st.button("Run Agent Audit"):
    with st.spinner("Strands Agent analyzing invoice and checking historical baselines..."):
        parsed = parse_invoice(invoice_input)
        anomaly = check_price_anomaly(parsed["vendor"], parsed["amount"])
        st.session_state["parsed_bill"] = parsed
        st.session_state["anomaly_report"] = anomaly

if "anomaly_report" in st.session_state:
    report = st.session_state["anomaly_report"]
    bill = st.session_state["parsed_bill"]
    
    st.markdown("### 🔍 Agent Audit Report")
    col1, col2, col3 = st.columns(3)
    col1.metric("Vendor", bill["vendor"])
    col2.metric("Current Charge", f"${bill['amount']}")
    col3.metric("Baseline Price", f"${report['historical_baseline']}", delta=f"+${report['price_increase']}")
    
    if report["flagged_for_human_review"]:
        st.error(f"⚠️ Price Hike Detected! Charge increased by ${report['price_increase']:.2f}.")
        st.markdown("### 🛡️ Human-in-the-Loop Validation Gate")
        st.warning("Action Paused: High-value transaction requires explicit human confirmation.")
        
        approval = st.checkbox("I authorize LifeOps Agent to execute this payment.")
        
        if st.button("Execute Financial Action"):
            result = execute_payment(bill["vendor"], bill["amount"], human_approved=approval)
            if result["status"] == "SUCCESS":
                st.success(result["message"])
            else:
                st.error(result["message"])
