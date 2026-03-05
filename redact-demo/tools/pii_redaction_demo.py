from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun


@tool
def pii_redaction_demo(context: AgentRun) -> str:
    """
    Complete PII redaction demonstration tool that:
    1. Displays example PII values that will be written
    2. Writes the PII values to context variables
    3. Reads back the context variables to confirm they were set
    4. Displays the final values stored in context
    
    This tool demonstrates the full lifecycle of PII data in context variables
    and how these values can be redacted in analytics.
    
    Args:
        context (AgentRun): The agent run context for storing and reading PII data.
    
    Returns:
        str: A comprehensive report showing all steps of the PII redaction demo.
    """
    
    req_context = context.request_context
    
    # Define the PII examples based on IBM documentation patterns
    pii_examples = {
        "pii_email": "john.doe@example.com",
        "pii_date": "12/25/2023",
        "pii_ssn": "123-45-6789",
        "pii_credit_card": "4532-1234-5678-9010",
        "pii_phone": "+1 (555) 123-4567",
        "pii_ip_address": "192.168.1.100",
        "pii_postal_address": "123 Main Street, Apt 4B, New York, NY 10001",
        "pii_health_insurance": "ABC123456789",
        "pii_salary": "$75,000 per year"
    }
    
    # Build the response showing all three steps
    response = "=" * 60 + "\n"
    response += "PII REDACTION DEMONSTRATION\n"
    response += "=" * 60 + "\n\n"
    
    # STEP 1: Display the values that will be written
    response += "📋 STEP 1: Example PII Values to Write\n"
    response += "-" * 60 + "\n"
    response += "The following PII values will be written to context variables:\n\n"
    response += "📧 Email: john.doe@example.com\n"
    response += "📅 Date: 12/25/2023\n"
    response += "🔢 SSN: 123-45-6789\n"
    response += "💳 Credit Card: 4532-1234-5678-9010\n"
    response += "📱 Phone: +1 (555) 123-4567\n"
    response += "🌐 IP Address: 192.168.1.100\n"
    response += "🏠 Postal Address: 123 Main Street, Apt 4B, New York, NY 10001\n"
    response += "🏥 Health Insurance: ABC123456789\n"
    response += "💰 Salary: $75,000 per year\n"
    response += "\n"
    
    # STEP 2: Write to context variables
    response += "✍️  STEP 2: Writing to Context Variables\n"
    response += "-" * 60 + "\n"
    response += "Writing all PII values to their respective context variables...\n\n"
    
    # Perform the actual write operation
    req_context.update(pii_examples)
    
    response += "✅ Successfully wrote 9 PII values to context variables:\n"
    response += "   • pii_email\n"
    response += "   • pii_date\n"
    response += "   • pii_ssn\n"
    response += "   • pii_credit_card\n"
    response += "   • pii_phone\n"
    response += "   • pii_ip_address\n"
    response += "   • pii_postal_address\n"
    response += "   • pii_health_insurance\n"
    response += "   • pii_salary\n"
    response += "\n"
    
    # STEP 3: Read back from context variables
    response += "📖 STEP 3: Reading from Context Variables\n"
    response += "-" * 60 + "\n"
    response += "Reading back the values to confirm they were stored correctly:\n\n"
    
    # Read each value back
    email = req_context.get('pii_email')
    date = req_context.get('pii_date')
    ssn = req_context.get('pii_ssn')
    credit_card = req_context.get('pii_credit_card')
    phone = req_context.get('pii_phone')
    ip_address = req_context.get('pii_ip_address')
    postal_address = req_context.get('pii_postal_address')
    health_insurance = req_context.get('pii_health_insurance')
    salary = req_context.get('pii_salary')
    
    response += f"📧 Email: {email}\n"
    response += f"📅 Date: {date}\n"
    response += f"🔢 SSN: {ssn}\n"
    response += f"💳 Credit Card: {credit_card}\n"
    response += f"📱 Phone: {phone}\n"
    response += f"🌐 IP Address: {ip_address}\n"
    response += f"🏠 Postal Address: {postal_address}\n"
    response += f"🏥 Health Insurance: {health_insurance}\n"
    response += f"💰 Salary: {salary}\n"
    response += "\n"
    
    # Summary
    response += "=" * 60 + "\n"
    response += "✅ DEMONSTRATION COMPLETE\n"
    response += "=" * 60 + "\n\n"
    response += "📊 Summary:\n"
    response += "• All 9 PII types have been successfully written to context variables\n"
    response += "• All values have been read back and confirmed\n"
    response += "• These values are now stored in the conversation context\n\n"
    
    response += "🔒 PII Redaction:\n"
    response += "When analytics are enabled with PII redaction, these patterns will be\n"
    response += "automatically masked in logs and analytics data based on the configured\n"
    response += "regular expressions. The conversation will continue to have access to\n"
    response += "the actual values, but they will appear as [REDACTED] in analytics.\n\n"
    
    response += "📖 For more information about PII patterns, see:\n"
    response += "https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=settings-managing-agent-analytics#pii-regular-expression-patterns\n"
    
    return response

# Made with Bob
