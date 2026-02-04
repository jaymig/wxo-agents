# User Context agent

This tutoral introduces context variables.  You are instructed how to deploy an agent which has been enabled with the ```wxo_user_name``` and ```wxo_email_id``` context variables and two tools that can read and display the values of those variables.  

These two context variables are the best to start with, since the default watsonx Orchstate chat portal sets the value of the variables during the session.  Custom context variables are covered in a subsequent article(wip).

!!! note
     This tutorial requires the use of the Agent Development Kit (ADK).  Installation of the ADK is outside of the scope of these tutorials.  Please see the [ADK installation](https://developer.watson-orchestrate.ibm.com/getting_started/installing){target="_blank"} documentation for details. 

!!! note
     The agent spec file includes customized welcome message and starter prompts.  Please see the [Starter Prompt](https://developer.watson-orchestrate.ibm.com/agents/build_agent#starter-prompts){target="_blank"} documentation for details. 

More information on context varibles is located in this [ADK documentation](https://developer.watson-orchestrate.ibm.com/agents/build_agent#providing-access-to-context-variables){target="_blank"}     

In this tutorial you will:

1. Add tools to your tenant which are able to read and display the ```wxo_user_name``` and ```wxo_email_id``` context variables.

2. Import an agent that is configured with support for the context variables.

3. Interact with the agent and have it display the values of the variables.

4. The examples used in this tutorial are located in the user_info folder of this [git repository](https://github.com/jaymig/wxo-agents){target="_blank"}.  The repo contains deploy script which can be used to install the agent and tools.  Alternatively, you can follow the step by step instructions below.

## Import the tools

1. Download the example [python tool spec file](https://github.com/jaymig/wxo-agents/blob/main/user_context/tools/user_context.py){target="_blank"} and the [reqiurements.txt file](https://github.com/jaymig/wxo-agents/blob/main/user_context/tools/requirements.txt){target="_blank"} into your 'demo' folder.
<br>

2. Import the tool file using the below command line
```
orchestrate tools import -k python -f ./user_context.py -r ./requirements.txt
```
NOTE: It is important that you are running the 'orchestrate' command from the same directory as the user_context.py and requirements.txt files.
<br>
NOTE: This python file actually includes two tools.
<br>
You should see an output as follows:
```
[INFO] - Using requirement file: "./requirements.txt"
[INFO] - Tool 'session_context' imported successfully
[INFO] - Tool 'user_info' imported successfully

```

3. Confirm that the tools were installed by listing the existing tools
```
orchestrate tools list
```
<br>
If you see a knowledge base with the name ```session_context``` and ```user_info```, congratulations.   It is time to import the agent that will use these tools.


## Import the agent

The following steps guide you through importing the agent that is configured to use the tools that you imported in the previous section.  If the tools were not imported, this step will fail with an error message. 

1. Download the [agent spec file](https://github.com/jaymig/wxo-agents/blob/main/user_context/agents/welcome_agent.yaml){target="_blank"} into your 'demo' folder.

2. Import the agent configuration file with the following command
```
orchestrate agents import -f ./welcome_agent.yaml
```
<br>
If successful, you should see the following message:
```
[INFO] - Agent 'welcome_agent' imported successfully
```

Congratulations!  Your agent is imported.  You can verify that it works by logging into Watsonx Orchestrate and chatting with it.

## Chat with the Agent

Log into watsonx Orchestrate and navigate to the build pages.  You should see your newly imported agent at the top.
Click on the ```Welcome agent``` agent icon to access the agent builder.  You can interact with it right there in the builder experience using the customized starter prompts.  This agent is configured with two starter prompts, one for each tool.

![Starter Prompts](../images/user_context/welcome_agent.png#shadow#center){: style="height:400x;width:400px"}


The ```user_info``` tool is configured to receive the context variables from the agent, when the agent calls the tool.  You can see that in the tool definition:

```
...
@tool
def user_info(wxo_user_name: str, wxo_email_id: str):
...
```

The ```session_context``` tool is configured to read the context variables from the session.  You can see that this tool uses a specfic library and tool definition:

```
...
from ibm_watsonx_orchestrate.run.context import AgentRun
...

@tool
def session_context(context: AgentRun) -> str:
...
```


