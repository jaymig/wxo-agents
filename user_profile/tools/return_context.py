#return_context.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun


@tool
def context_from_session(context: AgentRun) -> str:
    """
    This tool displays the value of ALL context variables from the Agent,
    checking that each variable exists before returning it.
    Returns all 9 context variables in a consistent format.
    """

    req_context = context.request_context

    def safe_get(key: str, default: str = "Unknown"):
        value = req_context.get(key)
        return value if value not in (None, "") else default

    # Retrieve all 9 context variables
    wxo_user_name        = safe_get('wxo_user_name')
    wxo_email_id         = safe_get('wxo_email_id')
    employee_id          = safe_get('employee_id')
    employee_first_name  = safe_get('employee_first_name')
    employee_last_name   = safe_get('employee_last_name')
    role                 = safe_get('role')
    office_location      = safe_get('office_location')
    country              = safe_get('country')
    preferred_language   = safe_get('preferred_language')

    # Return all variables in a consistent, complete format
    return (
        f"User Profile Context Variables:\n"
        f"- WXO User Name: {wxo_user_name}\n"
        f"- WXO Email ID: {wxo_email_id}\n"
        f"- Employee ID: {employee_id}\n"
        f"- Employee First Name: {employee_first_name}\n"
        f"- Employee Last Name: {employee_last_name}\n"
        f"- Role: {role}\n"
        f"- Office Location: {office_location}\n"
        f"- Country: {country}\n"
        f"- Preferred Language: {preferred_language}"
    )

# Made with Bob

