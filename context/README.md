# Overview

This set of agents and tools were created to demonstrate context_variable support within agents, tools, flows and knowledge.

## Scenario

This example is a ficticious insurance company SageLife, and the AI agent is used by advisors who need to connect to a live human agent.


## Agent Concept

Context Agent - an agent that has access to a few context variables
 - employee_id
 - employee_first_name
 - employee_last_name
 - policy_number
 - policy_status
 - intent
 - business_name


## Tools concept

 The agent has the following tools available to it

- employee_details
   - Input:  Employee ID
   - Output:  First_name, Last_name
- policy_details
    - Input:  Employee ID
    - Output:  policy_number, policy_status
- end_session
    - Output:  All context variables

