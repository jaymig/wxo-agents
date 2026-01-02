# Hello World API

## Objective

This tutorial guide you through configuring your Insomnia client to fetch an authentication token from the Watsonx Orchestrate API.  These tokens are required to interact with all of the other APIs.  

## Authenticating with your tenant - step by step

If this is your first time using Insomnia, I reccomend you create a new Project where we sill create HTTP calls, and also an environment where we will store API keys, and other end point information.

1. Click on the "+" icon in the upper right hand corner of Insomnia to create a new project, and give the project a name.
<br><br>
![create project](../images/insomnia_new_project.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
<br><br>
![new project name](../images/hello_world_insomnia_project.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

2. Create a new Environment by clicking on the "+" icon to the rigth of the Environments label.  Give your new environment a name.
<br><br>
![create project](../images/create_new_environment.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
<br><br>
![new project name](../images/hello_world_demo_environment.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

3. Navigate into your enviornment by clicking on it, and then add your first environment variable "auth_url".  The url for generating auth tokens is [documented here](https://developer.ibm.com/apis/catalog/watsonorchestrate--custom-assistants/api/API--watsonorchestrate--generating-a-json-web-token#generatingjwt).
```
https://iam.platform.saas.ibm.com/siusermgr/api/1.0/apikeys/token
```
Your environment should look like this:
<br><br>
![auth url](../images/auth_url_environment.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

4. Next we need to add two more enviornment variables:  API key and tenant URL.  The API key and tenant url can be found in the settings menu of your watsonx Orchstrate tenant.
<br><br>
![settings menu](../images/settings_menu.png#shadow#left){: style="height:300x;width:300px"}
<br><br>
<br><br>
![url and api key](../images/url_and_API_key.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Here is a view of the configured environment
<br><br>
![configured environment](../images/environment_with_api_key_and_urls.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
You can now exit the enviornment by clicking on the X in the tab, and then open up your collection by clicking on Collection, as shown in the screenshots:
<br><br>
![exit environment](../images/exit_environment.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
<br><br>
![open collections](../images/click_on_collections.png#shadow#left){: style="height:500x;width:500px"}
<br><br>


4. Now we will configure an API call to generate a token.  This API is documented [here](https://developer.ibm.com/apis/catalog/watsonorchestrate--custom-assistants/api/API--watsonorchestrate--generating-a-json-web-token#generatingjwt).  Start by opening up your collection by clicking on it.
<br><br>
![open my collections](../images/open_my_first_collection.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

5. Select your environment, so the API call can use the variables you just created.  In the top left of Insomnia, click on Global Settings drop down menu and select the "Hello World Demo Environment".
<br><br>
![select environment](../images/select_hello_world_environment.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

6. You should be prompted to create your first HTTP API call.  Since this is a POST, you need to select POST from the drop down list.
<br><br>
![select POST](../images/configure_http_post.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

7. Now we will insert the variable for the URL.  By typeing a period "." in the URL box, a list of available variables will appear.  Select the _.auth_url from the list.  
<br><br>
![select POST](../images/insert_auth_url.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Here you can see what the correctly configured URL field should look like.  Note how the preview field below shows the actual URL using the value of the variables
<br><br>
![select POST](../images/configured_url.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

8. Now we will configure the body of the HTTP call to include the API Key. In the body section, type
```
{"apikey": ""}
``` 
Then insert a "." for the value of the API key, and a drop down list will appear with the available variables.  Select _.api_key from the list.
<br><br>
![configure key](../images/configure_api_key.png#shadow#left){: style="height:500x;width:500px"}
<br><br>
Here you can see what the correctly configured body looks like, with the variable as a placeholder for the value of the API key. 
<br><br>
![configured body](../images/configured_body.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

9. Now you are ready to test.  Click the SEND button. You should see a response payload that includes the token.
<br><br>
![send_success](../images/send_success.png#shadow#left){: style="height:500x;width:500px"}
<br><br>

10. To prevent confusion with other HTTP requests, let's rename this first HTTP call to "Token Auth", by clicking on the settings menu option and updating the name.
<br><br>
![rename token auth](../images/rename_to_token_Auth.png#shadow#left){: style="height:500x;width:500px"}
<br><br>


Congratulation!  You are now ready to find your agent ID using the /agents API

## Finding the Agent ID via /agents API

Ready for the next step?  Click [here to list your agents](./list-agents.md).

