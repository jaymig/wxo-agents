# Overview

This set of agents and tools were created to demonstrate context_variable support within agents, tools, and eventually flows and knowledge.

## Scenario

This example is a ficticious insurance company SageLife, and the AI agent is used by advisors who need to connect to a live human agent.


## Agent Concepts

Context Supervisor Agent - an agent that has access to a few context variables
 - employee_id
 - employee_first_name
 - employee_last_name
 - policy_number
 - policy_status
 - intent
 - business_name

Context Collaborator Agent - an agent that has access to the same context as supervisor as well as a tool to display the context


## Tools concept

 The collaborator agent has the following tool available to it

- context_from_session
   - Input:  
   - Output:
        f"Hello, {wxo_user_name}! "
        f"Employee ID: {employee_id}, "
        f"Employee First Name: {employee_first_name}, "
        f"Employee Last Name: {employee_last_name}, "
        f"Role: {role}, "
        f"Country: {country}, "
        f"Preferred Language: {preferred_language}"


