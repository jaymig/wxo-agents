from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun

@tool
def update_user_context(context: AgentRun) -> str:
    """
    Demonstrates how to set wxo_email_id and wxo_user_name context variables:
    - Set wxo_email_id and wxo_user_name together via update() (bulk).

    Args:
        context (AgentRun): The agent run context containing request metadata.
        new_email (str): The email address to set.
        new_user_name (str): The user name to set.

    Returns:
        str: Confirmation with the updated values.
    """
    req_context = context.request_context

    # --- Bulk update for multiple related keys
    req_context.update({
        "wxo_email_id": "micky@disney.com",
        "wxo_user_name": "mickey mouse"
    })

    # --- Read back to confirm
    email = req_context.get("wxo_email_id")
    name = req_context.get("wxo_user_name")


    return (
        "Context updated -> "
        f"wxo_email_id: {email}, "
        f"wxo_user_name: {name}"
    )