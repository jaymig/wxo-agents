# Department Contact Agent

This agent is able to retrieve the correct email address for a given department contact.  It accomplishes this by using sequencing multiple tools dynamically.  This is one of the key, powerful features of Agents.   They understand the intent of users and can identify which tools, and which sequence is needed to complete the task.

## Create and Configure the Agent

The following steps guild you through creating the  "Department Contact" agent

1. Login to Watsonx Orchestrate and select 'Agent Builder' from the main navigation menu 
<br><br>
![Select Agent Builder](../images/select_agent_builder.png#shadow#center){: style="height:200x;width:200px"}
<br><br>

2. From the Manage Agents page, click on 'Create agent'.
<br><br>
![Create Agent](../images/create_agent.png#shadow#center){: style="height:400x;width:400px"}
<br><br>

3. From the Manage agent page, select "Create from scratch", and provide a name (e.g. Department Contact Agent) and description (An agent that demonstrates creating an email to a specific contact in the list using a dynamic sequence of tools)
<br><br>
![Create Agent from Scratch](../images/create_department_contact_agent.png#shadow#center){: style="height:400x;width:300px"}
<br><br>

4. The next step is to add the tools.  Scroll down to the "Toolset" section and click on "Add tool", then select "Import" to Import an External Tool and upload this [Email Department Contact spec file](../examples/department-contacts/tools/email-department-contact.json){target="_blank"}. 
<br><br>
![Add Tool](../images/add_tool.png#shadow#center){: style="height:400x;width:400px"}
<br><br>
![Import External Tool](../images/import_external_tool.png#shadow#center){: style="height:400x;width:400px"}
<br>

5. The spec file contains three tools: Send an email, Department Contacts, Contact Details.  You need to select all three tools and click 'Done'.  
<br><br>
![Select all Tools for import](../images/select_and_import_tools.png#shadow#center){: style="height:400x;width:400px"}
<br>
Once the tools are imported, you should see then in your agents list of tools: 
<br><br >
![Agent tool list](../images/department_contact_tools_list.png#shadow#center){: style="height:400x;width:400px"}
<br>

6. This is a simple instruction to get you started.  Try this example, and then iterate on this example to get the Agent to complete the task to your satisfacion.  You can use the chat prompt below to test your instructions.
<br><br>
!!! example 
     Be verbose and polite and use the name "John Doe" in the signature of all emails.
     Always show a well formatted draft email with line breaks and I ask me to confirm before sending.
<br><br>

You can see here a working example.

!!! example
     If you are asked to draft an email to a department (dpt), always use the 'Department Contacts' tool to look up the department contact and  'contact details' tool to get their email address to be the recipient of the email. 

     Be verbose and polite and use the name "John Doe" in the signature.  Always show the draft and format it nicely in paragraphs.

     When asked to send the email use 'Mock Sending an email' tool. Always confirm I want to send the email first, unless I say it is good to go. Also add the current day & time in confirmation message and display it out in a table.

Also add a subject line summarizing the email.  Put it right above message and under To and cc fields.

Don't tell me why you do, just do it.

## Chat with the Agent

Now that you have built the agent, you can interact with it right there in the builder experience.  For example, try this message

```
Email the dev team about an issue with the product as Git Number 123 to be fixed as soon as possible.
```

```
Send an email to the development department contact about a bug in the Configuration section of the application
```

