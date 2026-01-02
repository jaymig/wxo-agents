# Chat with Hello World Agent

## Objective

At the end of this tutorial, you should have sent a message to the agent using the [/runs api](https://developer.watson-orchestrate.ibm.com/apis/orchestrate-agent/chat-with-orchestrate-assistant).


## Settting context via /runs API

This section walks you through setting context when usingthe /runs API.

1. Now we need to configure the body section.  Navigate to the body section and end the following text:
```
{
    "message": {
        "role": "user",
        "content": "what is my email_address?"
    },
    "context": {
        "wxo_user_name": "Jay Migliaccio"
    },
    "agent_id": "76f97aad-c458-47b4-85cd-05179f133ec4"
}
```

2. Now you can send your first message to the agent.  Click Send.  If everything is working, you can see the resulting object has a thread_id.
<br><br>
![runs API first testl](../images/runs_api/runs_api_first_test.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Save the thread_id as a new environment varible. We will use it to view the messages in the thread, using the /messages API.
<br><br>
![environment with thread_idl](../images/list_messages/environment_with_thread_id.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

## Next steps

In the next step, we will view the new messages using the [/messages api](https://developer.watson-orchestrate.ibm.com/apis/message-threads/get-message-by-id){target="_blank"}.  If you are ready to start click [next](./list-messages.md){target="_blank"}