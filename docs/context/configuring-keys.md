# Configuring encryption keys

In this section, we will be configuring client and IBM encryption keys on your wxO tenant. Please note that wxO now has security enabled by default, but it is up to you to setup a key pair.

You can learn more about setting up security in the [ADK documentation](https://developer.watson-orchestrate.ibm.com/agents/integrate_agents#embedded-chat-security). 

At the end of this section, you will have created a key pair, and installed your public key on the wxO server.


## Configuring security on your server - step by step

Security can be configured either via API or via a script that is provided in the [ADK](https://developer.watson-orchestrate.ibm.com/agents/integrate_agents#enabling-security) (see step 2).

This tutorial uses the script with an IBM cloud tenant.

1. Create a new folder on your laptop for this exercise, for example:
```
# cd ~/Desktop/demo/
# mkdir embed-demo
# cd embed-demo
```
2. Open your browser to the [ADK](https://developer.watson-orchestrate.ibm.com/agents/integrate_agents#enabling-security) and copy the example script into that folder wxO-embed-chat-security-tool.sh
<br>

3. Log into your wxO tenant as an admin or builder and get the tenant URL.   As a reminder the tenant URL can be obtained by clicking on the icon in the upper right corner and selecting "settings" from the drop down menu.
<br>

4. When the settings page opens up, select "API details" tab.  There you will find the Service Instance URL and a link to Generate API keys.

5. Once you click on the "Generate API Key" button, you will come to a page for generating keys.  The screenshots below walk you through the process.

6. Save both the API key and the service instance URL, as we will need them in the next step.

7. Give the security configuration scrip execute permissions, then run the script.  
```
# chmod +x wxO-embed-chat-security-tool.sh
# ./wxO-embed-chat-security-tool.sh
```
8. The script will prompt you for your service instance URL and API key, and then present a navigation menu.   Select "1) Configure security with custom keys (Reccomended)" from the menu.   A few seconds later the script should indicate that security is configured and verified.

9. (Optional) review the security setup by navigating back to the main menu (option 1) and then choosing option 3: View the security configuration. that option from the menu.

10. Exit the script (option 2) and view the contents in your local folder.  You should see a new "wxo_security_config" directory with a few keys in it.

Here are the keys you should see:




You are ready to proceed with creating the web application.













