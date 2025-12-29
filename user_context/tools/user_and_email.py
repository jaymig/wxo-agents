#user_and_email.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def echo_user_info(wxo_user_name: str, wxo_email_id: str):
    """
    Takes a user name and email ID, and returns a formatted message.
    """
    return  f"Hello, {wxo_user_name}! Your email as {wxo_email_id}."
