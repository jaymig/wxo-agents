from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun

@tool
def update_user_profile(context: AgentRun, user_age: int, user_login: str, user_password: str) -> str:
    """
    Demonstrates two ways to set context variables:
    - Set user_age individually via item assignment (single key).
    - Set user_login and user_password together via update() (bulk).

    Args:
        context (AgentRun): The agent run context containing request metadata.
        user_age (int): The user's age to store.
        user_login (str): The user's login identifier.
        user_password (str): The user's password.

    Returns:
        str: Confirmation with the updated values.
    """
    req_context = context.request_context

    # --- Single-key assignment (ideal for one value)
    req_context["user_age"] = user_age

    # --- Bulk update for multiple related keys
    req_context.update({
        "user_login": user_login,
        "user_password": user_password,
    })

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