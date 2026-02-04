# Hello World Agent - ADK

Now that you have used the low code agent builder to create your first Watsonx Orchestrate agent, it is time to learn the Agent Development Kit (ADK).

!!! note
     I use a Macbook, so these instructions are for the Mac.

!!! note
     This tutorial requires the use of the Agent Development Kit (ADK).  Installation of the ADK is outside of the scope of these tutorials.  Please see the [ADK installation](https://developer.watson-orchestrate.ibm.com/getting_started/installing) documentation for details.     

## Objective

This tutorial will guide you through importing the "Hello World" tool and agent using the ADK.

## Import the tool and agent step by step

Before proceeding, please download the ["Hello World" tool spec file](https://github.com/jaymig/wxo-agents/blob/main/hello-world/tools/hello-world-tool.json){target="_blank"} and the ["Hello World" agent spec file](https://github.com/jaymig/wxo-agents/blob/main/hello-world/agents/hello-agent.json){target="_blank"} to your local system.  For my example, I placed them in my desktop in a 'demo' folder.

1. Login to your terminal and navigate to the folder "demo" folder on your desktop.
```
# cd ~/Desktop/demo
```
<br>

2. From the demo folder, import the hello-world-tool.json that you downloaded previously.
```
# orchestrate tools import -k openapi -f ./hello-world-tool.json
```
<br>

3. (Optional) List the tools on your tenant. 
```
# orchestrate tools list
```
NOTE: If you have alot of tools or you want to look at the details of the tools, try the 'verbose' mode and pipe the output to 'less'.  Use your arrow keys to scroll up and down, and 'q' to quit.
```
# orchestrate tools list -v | less
```
<br>
4. Import the agent file that should be in your demo folder. 
```
# orchestrate agents import -f ./hello-agent.json
```
<br>

5. (Optional) List the agents in your tenant. 
```
# orchestrate agents list
```
NOTE: If you have alot of agents or you want to look at the details of the agents, try the 'verbose' mode and pipe the output to 'less'.  Use your arrow keys to scroll up and down, and 'q' to quit.
```
# orchestrate agents list -v | less
```


## Chat with the Agent

Now that you have imported the agent and tool, you can interact with it in the builder experience.  Try typing "hello" and see the response.


<br><br>
![Chat with Agent](../images/chat_with_agent.png#shadow#center){: style="height:600x;width:600px"}
<br><br>

