# List agents API

## Objective

This tutorial will step you through configuring Insomnia HTTP call to the [/orchestrate/agents API](https://developer.watson-orchestrate.ibm.com/apis/agents/list-registered-agents) to list the existing agents in your tenant, so we can find the Agent ID.  We need the Agent ID in order to call the /runs API.  

## List agents - step by step guide.

1. Create a new HTTP request, using the "+" icon at the top of your list of existing HTTP requests.  Select "New HTTP request" from the menu
<br><br>
![new http request](../images/list_agents/new_http_request.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

2. Configure the request with the _.wxo_url variable and the following path:
```
/v1/orchestrate/agents
```
<br><br>
![get agent url](../images/list_agents/get_agents_url.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

3. Next we will configure the token from the Token Auth API call as input to our Authorization token.  In the Token field, type a period "." and select "Request -> OAuth 2.0 Access Token" from the list.
<br><br>
![select OAuth token](../images/list_agents/list_agents_auth_config.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

4. The result is an input variable that needs to be configured.  Click on the unconfigured variable token and a configuration dialogue will appear.
<br><br>
![unconfigured input](../images/list_agents/list_agents_unconfigured_auth.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Variable configuration dialogue box:
<br><br>
![edit tag](../images/list_agents/edit_tag.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

5. Click on the "function to perform" and select "Response - reference values from other request's responses"
<br><br>
![reference values](../images/list_agents/edit_tags_reference_values_from_other_requests.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

6. Under Attribute, select "Body Attribute - value of response body" and under Request select "POST Token Auth"
<br><br>
![configure attribute](../images/list_agents/edit_tag_select_token_auth.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

7. Under Trigger Behavior secrtion, select "Always - Always resend request" from the drop down menu.
<br><br>
![Always resend request](../images/list_agents/edit_tag_always_resend_request.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

8. Lastly, configure the filter to fetch the "token" field from the Token Auth output.  This can be done using the syntax 
```
 $.token
```
(which represent the token parameter from the output of the Token Auth API call, payload).  You can see the token value in the 'live Preview" box at the bottom of the screen.
<br><br>
![configure filter](../images/edit_tag_configure_filter.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Click Done to complete this configuration.  The correctly configured Auth section should look like this:
<br><br>
![get agent authl](../images/list_agents/get_agents_auth.png#shadow#left){: style="height:500x;width:500px"}
<br><br>


9. Click the Send button and view the results, which should be your agent details.  If your tenant has multiple agents, use the CMD+F key to search for 'hello_world' and you should be able to find the Hello World agent and see it's id.
<br><br>
![get agent outputl](../images/list_agents/get_agents_api_call.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Copy the Agent ID and save it to your environment.
<br><br>
![environment with agent_idl](../images/list_agents/environment_with_agent_id.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

## Chatting with the Agent ID via /runs API

Ready for the next step?  Click [here to chat with your agent](./chat-with-agent.md).

