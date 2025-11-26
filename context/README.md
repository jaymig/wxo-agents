# Overview

This set of agents and tools were created to demonstrate context_variable support within agents, tools, and eventually flows and knowledge.  This proceedure requires that you have [ADK installed](https://developer.watson-orchestrate.ibm.com/getting_started/installing), a developer or saas tenant and have [configured your environment](https://developer.watson-orchestrate.ibm.com/environment/initiate_environment).

# Getting started

Ready to install?

1) Download this repo
   ```
   gh repo clone jaymig/wxo-agents
   ```

2) Change into the 'context' directory
   ```
   cd context
   ```

3) Run the bash install script
   ```
   bash ./deploy.sh
   ```



## Scenario

This example is a ficticious insurance company SageLife.  Additional details are in progress.


## Agent Concepts

Context Supervisor Agent - an agent that has access to a few context variables: 
   - "employee_id", 
   - "employee_first_name", 
   - "employee_last_name",
   - "role", 
   - "office_location", 
   - "country", 
   - "preferred_language",
   - "wxo_user_name"

Context Collaborator Agent - an agent that has access to the same context as supervisor as well as a tool to display the context


## Tool concept

 The collaborator agent has the following tool:

- context_from_session
   - Input:  read from context
   - Output:
  
        f"Hello, {wxo_user_name}! " 
  
        f"Employee ID: {employee_id}, "

        f"Employee First Name: {employee_first_name}, "
     
        f"Employee Last Name: {employee_last_name}, "
     
        f"Role: {role}, "
     
        f"Country: {country}, "
     
        f"Preferred Language: {preferred_language}"


