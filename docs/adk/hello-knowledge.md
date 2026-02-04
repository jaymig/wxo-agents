# Hello Knowledge

This tutoral expands upon the Hello World example and adds a working example for importing  knowledge using the ADK.  This tutorial assumes that you have completed the ADK [Hello World ADK tutorial](./hello-world-adk.md). 

In this tutoral you will:

1. Import knowlege using the ADK (using the embeded Milvus vector store)

2. Re-import the agent, using an updated agent file, specifying the knowledge source imported in step 1.

## Import the knowledge

1. Download the example knowledge configuration file is located [here](https://github.com/jaymig/wxo-agents/blob/main/hello-world-knowledge/knowledge/knowledge_base.json){target="_blank"} and the PDF file located [here](https://github.com/jaymig/wxo-agents/blob/main/hello-world-knowledge/knowledge/IBM%20watsonx%20Orchestrate%20Doc.pdf){target="_blank"} into your 'demo' folder.
<br>

2. Import this knowledge file using the below command line
```
orchestrate knowledge-bases import -f ./knowledge-base.json
```
NOTE: It is important that the "IBM watsonx Orchestrate Doc.pdf" PDF file is in the same directory as the knowledge base configuration.
<br>
You should see an output as follows:
```
[INFO] - Successfully imported knowledge base 'knowledge_base_for_agent_Hello_world'
```
<br>
3. Confirm that the knowledge base was installed by listing the existing knowledge bases
```
orchestrate knowledge-bases list
```
<br>
If you see a knowledge base with the name 'knowledge_base_for_agent_Hello_world', congratulations.   It is time to update your agent to point to this new knowledgebase.


## Re-import the agent

The following steps guild you through updating the "Hello World" agent with the new configuration.   We will simply import the agent with the new configuration file.

1. Download the new agent configuration file from [here](https://github.com/jaymig/wxo-agents/blob/main/hello-world-knowledge/agents/hello-agent-with-knowledge.json){target="_blank"}

2. Import the agent configuration file with the following command
```
orchestrate agents import -f ./hello-agent-with-knowledge.json
```
<br>
If you are updating an existing agent (e.g. the one you just imported in the previous tutorial), you should see the following message:
```
[INFO] - Existing Agent 'hello_agent' found. Updating...
[INFO] - Agent 'hello_agent' updated successfully
```

Congratulations!  Your agent is updated with knowledge.  You can verify that it works by logging into Watsonx Orchestrate and chatting with it.

## Chat with the Agent

Now that you have built the agent, you can interact with it right there in the builder experience.  Try typing "How do I work with Agents" and see that the response comes from the knowledge file you just uploaded.



