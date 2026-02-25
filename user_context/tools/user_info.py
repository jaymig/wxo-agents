from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun


@tool
def user_info(wxo_user_name: str, wxo_email_id: str):
    """
    Takes a user name and email ID, and returns a formatted message.
    Note that this is not reading from AgenRun
    """
    return  f"Hello, {wxo_user_name}! Your user_info email is {wxo_email_id}."
