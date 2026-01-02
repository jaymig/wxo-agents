#return_context.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun


@tool
def context_from_session(context: AgentRun) -> str:
    """
    This tool displays the value of context from the Agent,
    checking that each variable exists before returning it.
    """

    req_context = context.request_context

    def safe_get(key: str, default: str = "Unknown"):
        value = req_context.get(key)
        return value if value not in (None, "") else default

    wxo_user_name        = safe_get('wxo_user_name')
    employee_id          = safe_get('employee_id')
    employee_first_name  = safe_get('employee_first_name')
    employee_last_name   = safe_get('employee_last_name')
    country              = safe_get('country')
    role                 = safe_get('role')
    preferred_language   = safe_get('preferred_langauge')

    return (
        f"Hello, {wxo_user_name}! "
        f"Employee ID: {employee_id}, "
        f"Employee First Name: {employee_first_name}, "
        f"Employee Last Name: {employee_last_name}, "
        f"Role: {role}, "
        f"Country: {country}, "
        f"Preferred Language: {preferred_language}"
    )
