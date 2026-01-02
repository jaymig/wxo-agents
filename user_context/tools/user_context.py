#user_and_email.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun


@tool
def user_info(wxo_user_name: str, wxo_email_id: str):
    """
    Takes a user name and email ID, and returns a formatted message.
    """
    return  f"Hello, {wxo_user_name}! Your user_info email is {wxo_email_id}."


@tool
def session_context(context: AgentRun) -> str:
    """
    This tool displays the value of context from the Agent,
    checking that each variable exists before returning it.
    """

    req_context = context.request_context

    def safe_get(key: str, default: str = "Unknown"):
        value = req_context.get(key)
        return value if value not in (None, "") else default

    wxo_user_name        = safe_get('wxo_user_name')
    wxo_email_id         = safe_get('wxo_email_id')
 
    return f"Hello, {wxo_user_name}!,  Your session_context email is: {wxo_email_id}"
