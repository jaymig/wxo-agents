# Hello World Agent

Once you have completed all of the [prerequisites](../index.md){target="_blank"} listed on the home page,  follow the steps below to create your first Watsonx Orchestrate agent.

!!! note
     If you are using a shared Watsonx Orchestrate tenant, this agent and tools may have already been installed by another user, and importing it will create a new tool with the same name.  See the instructions after step 1 on how to modify the tool specification to make it unique.

## Create and Configure the Agent

The following steps guild you through creating the  "Hello World" agent

1. Login to Watsonx Orchestrate and select 'Agent Builder' from the main navigation menu 
<br><br>
![Select Agent Builder](../images/select_agent_builder.png#shadow#center){: style="height:200x;width:200px"}
<br><br>

2. From the Manage Agents page, click on 'Create agent'.
<br><br>
![Create Agent](../images/create_agent.png#shadow#center){: style="height:400x;width:400px"}
<br><br>

3. From the Manage agent page, select "Create from scratch", and provide a name and description. 
<br><br>
![Create Agent from Scratch](../images/create_agent_from_scratch.png#shadow#center){: style="height:400x;width:300px"}
<br><br>

4. Scroll down to the "Knowledge" section and add this description, then upload Upload this document for knowlege 
<br>   
![Knowledge Description](../images/knowledge_description.png#shadow#center){: style="height:400x;width:400px"}
<br>
Example text: 
     Use the uploaded file to respond to questions about watsonx Orchestrate, tools or AI agents.
<br><br>

5. Scroll down a bit further and click 'upload files' to upload this [watsonx Orchestrate documentation file](https://github.com/jaymig/wxo-agents/blob/main/hello-world-knowledge/knowledge/IBM%20watsonx%20Orchestrate%20Doc.pdf){target="_blank"}. <br><br>
![Uploaded file](../images/upload_document.png#shadow#center){: style="height:400x;width:400px"}<br><br>

6. The next step is to add a tool.  Scroll down to the "Toolset" section and click on "Add tool", then select "Import" to Import an External Tool and upload this [Hello World Tool spec file](https://github.com/jaymig/wxo-agents/blob/main/hello-world/tools/hello-world-tool.json){target="_blank"}. 
<br><br>
![Add Tool](../images/add_tool.png#shadow#center){: style="height:400x;width:400px"}
<br><br>
![Import External Tool](../images/import_external_tool.png#shadow#center){: style="height:400x;width:400px"}
<br>

7. As part of the import process, you need to select the tool and click 'Done'.  
<br><br>
![Select Tool for import](../images/select_tool_for_import.png#shadow#center){: style="height:400x;width:400px"}
<br>
Once the tool is imported, you should see it in your agents list of tools: 
<br><br >
![Agent tool list](../images/agent_tool_list.png#shadow#center){: style="height:400x;width:400px"}
<br>

8. To complete this agent, provide instructions to guide it's behavior.
<br><br>
![Agent instructions](../images/hello_world_agent_behavior.png#shadow#center){: style="height:400x;width:400px"}
<br>
!!! example 
     Display the output of your "Hello World" tool, when the user sends you greetings such as "hello", "how are you", "bonjour", "Hi".  Do not use your general greeting response and go to the tool to respond.
<br><br>



## Chat with the Agent

Now that you have built the agent, you can interact with it right there in the builder experience.  Try typing "hello" and see the response.


<br><br>
![Chat with Agent](../images/chat_with_agent.png#shadow#center){: style="height:600x;width:600px"}
<br><br>

