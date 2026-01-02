# Creating a simple web app

In this section, we will create and run a simple node.js web application, and create an embedded web page for the Hello Agent Demo agent.

You can learn more about context variables in the [ADK documentation](https://developer.watson-orchestrate.ibm.com/agents/build_agent#providing-access-to-context-variables). 

!!! note
     In this tutorial, we will be modifying the hello-agent that was created in the introduction tutorial and enabling it to access context.  This tutorial will use wxo running in IBM cloud.


## Context Variable concepts

1. Agent can only access the specific context variables that it is configured to access.  As the builder, you specify which context variables the agent can access via the agent configuration file. 
2. You need to instruct the agent about the availability of the context variables.  
3. The value of context variables can be set via the API and via embedded chat.
4. All agents have access to two default context variables:  wxo_email_id, wxo_user_name


## Context variable tutorial overview

This tutorial will walk you through creating a simple web application, which contains context, that is passed to the embedded wxO chat and then on to the agent.

Here is a diagram of the flow of the context variables.

TODO: Insert diagram here

Before we can enable a web application to pass context, we need to setup security on wxO, so that wxO will be able to un encrypt the context that will be passed. 


If you are ready to do that now, please proceed to [Configuring security and keys](./configuring-keys.md){target="_blank"}.













