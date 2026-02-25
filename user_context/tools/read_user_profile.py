from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun


@tool
def read_user_profile(context: AgentRun) -> str:
    """
    Demonstrates how to read user_age, user_login, user_password 
    context variables from AgentRun

    Args:
       No Args

    Returns:
        str: Current values of user_age, user_login, user_password.
    """
    req_context = context.request_context

    # Read back to confirm
    age = req_context.get("user_age")
    login = req_context.get("user_login")
    password = req_context.get("user_password")

    return (
        "Context updated -> "
        f"user_age: {age}, "
        f"user_login: {login}, "
        f"user_password: {password}"
    )