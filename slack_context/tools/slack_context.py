#return_context.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun


@tool
def slack_context(context: AgentRun) -> str:
    """
    This tool displays the value of ALL context variables from the Agent,
    checking that each variable exists before returning it.
    Returns all 9 context variables in a consistent format.

    This tool was specifically designed to read the context that the slack channel passes.
    Here is an example of the "channel" context passed from slack:
    {
    "context": {
        "channel": {
            "customer_id": "XXXXXXXXXXXXXXXXXX",
            "channel_type": "slack",
            "slack": {
                "team_id": "YYYYYYYYYYYYYY",
                "channel_id": "111AAAA2222",
                "user_id": "ZZZ9999YYYY",
                "user_email": "abc@example.com",
                "custom_fields": {},
                "user_real_name": "Kayla"
            }
        },
        "wxo_email_id": "embeduser@mailinator.com",
        "wxo_user_name": "embeduser@mailinator.com",
        "wxo_tenant_id": "20250603-1111-2222-30a0-1be42032236e_4444444-5555-6666-8095-c859e3b31294"
    }
    """

    req_context = context.request_context

    def safe_get(key: str, default: str = "Unknown"):
        value = req_context.get(key)
        return value if value not in (None, "") else default

    # Retrieve all 9 context variables
    wxo_user_name        = safe_get('wxo_user_name')
    wxo_email_id         = safe_get('wxo_email_id')

    
    user_email: str = req_context.get('channel', {}).get('slack', {}).get('user_email', '')
    if not user_email:
        return False


    user_real_name: str = req_context.get('channel', {}).get('slack', {}).get('user_real_name', '')
    if not user_real_name:
        return False 


    # Return all variables in a consistent, complete format
    return (
        f"User Profile Context Variables:\n"
        f"- WXO User Name: {wxo_user_name}\n"
        f"- WXO Email ID: {wxo_email_id}\n"
        f"- User Real Name (slack): {user_real_name}\n"
        f"- User Email (slack): {user_email}\n"        
    )

# Made with Bob


    user_email: str = user_context.get('channel', {}).get('slack', {}).get('user_email', '')
    if not user_email:
        return False