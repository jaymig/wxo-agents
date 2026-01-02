# Chat with Hello World Agent

## Objective

At the end of this tutorial, you should have sent a message to the agent using the [/runs api](https://developer.watson-orchestrate.ibm.com/apis/orchestrate-agent/chat-with-orchestrate-assistant).


## Chat with the Agent via /runs API

This section walks you through setting up and using the /runs API.

1. First we need to create a new HTTP request for the /runs API.  By closing all the existing tabs, you should see an empty canvas with an icon to create a new HTTP request.
<br><br>
![new HTTP request](../images/create_new_HTTP_request.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

2. Next we can populate the URL using the same technique as we did above, select POST method from the drop down list, and then type a period "." and select _.wxo_url from the list.  Then append this to your host:
```
/v1/orchestrate/runs
```
Here is a view of the completed URL configuration
<br><br>
![new HTTP request](../images/orchestrate_runs_api_request.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

3. Navigate to the Auth tab, and select 'Bearer token' from the drop down list.
<br><br>
![select Bearer](../images/orchestrate_runs_auth.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

4. Next we will configure the token from the Token Auth API call as input to our Authorization token.  In the Token field, type a period "." and select "Request -> OAuth 2.0 Access Token" from the list.
<br><br>
![select OAuth token](../images/orchestrate_runs_auth_config.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

5. The result is an input variable that needs to be configured.  Click on the unconfigured variable token and a configuration dialogue will appear.
<br><br>
![unconfigured input](../images/unconfigured_token_input.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Variable configuration dialogue box:
<br><br>
![edit tag](../images/edit_tag.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

6. Click on the "function to perform" and select "Response - reference values from other request's responses"
<br><br>
![reference values](../images/edit_tags_reference_values_from_other_requests.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

7. Under Attribute, select "Body Attribute - value of response body" and under Request select "POST Token Auth"
<br><br>
![configure attribute](../images/edit_tag_select_token_auth.png#shadow#left){: style="height:500x;width:500px"}
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
![configure filter](../images/runs_api_auth_configured.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

9. Now we need to configure the body section.  Navigate to the body section and end the following text:
```
{
"message":{
	"role":"user",
	"content":"Hello, How are you?"
   },
"agent_id":""
}
```

10. Since the Agent ID is saved in a variable, all you need to do is type a period "." in between the two quotations marks and a list of environment variables appear.  Select agent_id from the list.
<br><br>
![runs API body configl](../images/runs_api/runs_api_body_config.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

11. Now you can send your first message to the agent.  Click Send.  If everything is working, you can see the resulting object has a thread_id.
<br><br>
![runs API first testl](../images/runs_api/runs_api_first_test.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Save the thread_id as a new environment varible. We will use it to view the messages in the thread, using the /messages API.
<br><br>
![environment with thread_idl](../images/list_messages/environment_with_thread_id.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

## Next steps

In the next step, we will view the new messages using the [/messages api](https://developer.watson-orchestrate.ibm.com/apis/message-threads/get-message-by-id).  If you are ready to start click [next](./list-messages.md)