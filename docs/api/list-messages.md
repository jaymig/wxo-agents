# Viewing Message details with the Messages API

## Objective

In this tutorial, we will configure Insomnia HTTP client to query the /message API to get message details.


## Get the messages - Step by Step

1.  Create a new HTTP request, with the following URL as shown in the diagram.
```
GET {{ _.wxo_url }}/v1/orchestrate/threads/{{ _.thread_id }}/messages
```
<br><br>
![get message URL configl](../images/list_messages/get_messages_url_config.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

2. Next you will configure the authentication method for this API call.  Fortunately, all API calls use the same bearer token for authentication, and we have already created an API call to fetch a valid bearer token from the [authentication service for AWS tenants](https://developer.ibm.com/apis/catalog/watsonorchestrate--custom-assistants/Generating+the+JWT+Token+for+the+AWS+offering){target="_blank"}.  You used it in the previous steps.  Follow step 3 - 8 above in the [list agents](./list-agents.md){target="_blank"} section to configure the Auth section to use the Token API call to fetch a Bearer token.
<br><br>
![get message Auth configl](../images/list_messages/get_messages_auth_config.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

3. Run the command and view the messages in the thread.  You should be able to see the message you sent and the response from the Agent.
<br><br>
![get message outputl](../images/list_messages/get_messages_output.png#shadow#left){: style="height:500x;width:500px"}
<br><br>


## Resources

You can find the Insomnia export of [my environment](../examples/insomnia/Hello-world-demo-environment_2025-08-29.yaml){target="_blank"} (sanitized) and [My first Collection](../examples/insomnia/my_first_collection.yaml){target="_blank"}.   

Please provide feedback to jmig@us.ibm.com
