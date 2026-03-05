# Redact Demo Agent

A watsonx Orchestrate agent that demonstrates PII (Personally Identifiable Information) redaction capabilities using context variables.

## Overview

This agent showcases how watsonx Orchestrate can handle sensitive data through context variables and demonstrates the PII redaction feature in agent analytics. The agent includes tools to populate and display various types of PII data that match the regular expression patterns used for redaction.

## Features

- **Context Variable Management**: Demonstrates how to use context variables to store sensitive information
- **PII Type Coverage**: Includes all major PII types from IBM's documentation:
  - Email addresses
  - Dates
  - Social Security Numbers (SSN)
  - Credit card numbers
  - Phone numbers
  - IP addresses (IPv4)
  - Postal addresses
  - Health insurance numbers
  - Salary information

- **Interactive Tool**: `pii_redaction_demo` - A comprehensive demonstration tool that:
  1. Displays example PII values that will be written
  2. Writes the PII values to context variables
  3. Reads back the context variables to confirm storage
  4. Shows the complete lifecycle of PII data handling

## Architecture

### Agent Configuration
- **Name**: `redact_demo`
- **Style**: React (conversational)
- **LLM**: groq/openai/gpt-oss-120b
- **Context Access**: Enabled with 9 PII-specific context variables

### Context Variables
The agent uses the following context variables to store PII data:
- `pii_email` - Email address
- `pii_date` - Date information
- `pii_ssn` - Social Security Number
- `pii_credit_card` - Credit card number
- `pii_phone` - Phone number
- `pii_ip_address` - IP address
- `pii_postal_address` - Postal address
- `pii_health_insurance` - Health insurance number
- `pii_salary` - Salary information

### Tool

#### pii_redaction_demo
A comprehensive demonstration tool that performs the complete PII lifecycle in a single execution:

**Step 1: Display Example Values**
Shows the PII values that will be written to context variables:
- Email: john.doe@example.com
- Date: 12/25/2023
- SSN: 123-45-6789
- Credit Card: 4532-1234-5678-9010
- Phone: +1 (555) 123-4567
- IP Address: 192.168.1.100
- Postal Address: 123 Main Street, Apt 4B, New York, NY 10001
- Health Insurance: ABC123456789
- Salary: $75,000 per year

**Step 2: Write to Context**
Writes all 9 PII values to their respective context variables.

**Step 3: Read and Verify**
Reads back all values from context variables to confirm they were stored correctly.

This single tool provides a complete demonstration of how PII data is handled in watsonx Orchestrate context variables.

## Installation

### Prerequisites
- watsonx Orchestrate ADK installed and configured
- Access to a watsonx Orchestrate instance

### Import Steps

1. Navigate to the redact-demo directory:
   ```bash
   cd redact-demo
   ```

2. Run the import script:
   ```bash
   ./import_all.sh
   ```

   This will:
   - Import the Python tool
   - Import the agent configuration
   - Verify successful deployment

## Usage

### Starting a Conversation

Once imported, you can interact with the agent using prompts like:

- "Run the PII redaction demonstration"
- "Demonstrate how PII redaction works"
- "Show me how PII data is handled"
- "Run the PII demo"

### Example Workflow

1. **Run the Complete Demo**:
   ```
   User: "Run the PII redaction demonstration"
   Agent: [Uses pii_redaction_demo tool to execute all three steps:
           - Display example PII values
           - Write values to context variables
           - Read back and verify storage]
   ```

2. **Explain Redaction**:
   ```
   User: "How does PII redaction work?"
   Agent: [Explains the redaction feature and how these patterns are masked in analytics]
   ```

## PII Redaction in Analytics

When agent analytics are enabled in watsonx Orchestrate, the PII patterns stored in context variables are automatically redacted based on regular expressions. This ensures that sensitive information is not exposed in:

- Analytics dashboards
- Log files
- Conversation history
- Audit trails

### Regular Expression Patterns

The PII types in this demo correspond to the patterns documented at:
https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=settings-managing-agent-analytics#pii-regular-expression-patterns

Each PII type has a specific regex pattern that identifies and masks the sensitive data:
- **Email**: `\b[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b`
- **Date**: `\b(?:1[666|000]|9\d{2})\d{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])\b`
- **SSN**: `\b(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}\b`
- **Credit Card**: `\b(?:\d{4}[-\s]?){3}\d{4}\b`
- **Phone**: `(?:\+?(\d{1,3}))?(?: ?\([-\s]?)?(?:\d{1,4})?\)?(?:[-\s]?\d{2,5}){2,}\b`
- **IP Address (IPv4)**: `\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b`
- **Postal Address**: `\b(\d{1,5})\s([a-zA-Z0-9\s]+)\s*,?\s*([a-zA-Z\s]+),\s*([A-Z]{2})\s*(\d{5}(-\d{4})?)\b`
- **Health Insurance**: `(?i)\b(?:\d{9}|[A-Za-z]\d{8})\d{3}-\d{2}-\d{4}[A-Za-z]{2,3}\d{6,9}\b`
- **Salary Pattern**: Complex pattern matching various salary formats

## Project Structure

```
redact-demo/
├── agents/
│   └── redact_demo_agent.yaml      # Agent configuration
├── tools/
│   └── pii_redaction_demo.py       # Complete PII demonstration tool
├── import_all.sh                    # Deployment script
└── README.md                        # This file
```

## Technical Details

### Context Variable Access

The agent uses the `AgentRun` object to access and modify context variables:

```python
from ibm_watsonx_orchestrate.run.context import AgentRun

@tool
def example_tool(context: AgentRun) -> str:
    req_context = context.request_context
    
    # Read a context variable
    value = req_context.get('pii_email')
    
    # Write to context variables
    req_context['pii_email'] = 'new@example.com'
    
    # Bulk update
    req_context.update({
        'pii_phone': '+1-555-0123',
        'pii_date': '01/01/2024'
    })
```

### Important Notes

- Context variables must be declared in the agent's `context_variables` list
- The agent must have `context_access_enabled: true`
- Variable names should use underscores, not hyphens (hyphens cause errors)
- Default context variables (`wxo_email_id`, `wxo_user_name`, `wxo_tenant_id`) cannot be modified

## Demonstration Scenarios

### Scenario 1: Basic PII Handling
1. User asks to run the PII demonstration
2. Agent calls `pii_redaction_demo` which:
   - Displays the example PII values
   - Writes them to context variables
   - Reads them back to verify storage
3. Agent explains how this data would be redacted in analytics

### Scenario 2: Educational Walkthrough
1. User asks about PII redaction
2. Agent explains the concept
3. Agent runs the demonstration tool to show the complete lifecycle
4. Agent explains which patterns would be masked in analytics
5. Agent provides link to IBM documentation

### Scenario 3: Testing Redaction
1. Run the PII demonstration tool
2. Have a conversation that references the PII values stored in context
3. Check analytics dashboard to verify redaction is working
4. Compare redacted vs. non-redacted data

## Troubleshooting

### Import Errors
If you encounter import errors:
- Verify ADK is properly installed: `adk --version`
- Check you're in the correct directory
- Ensure you have proper credentials configured

### Context Variable Issues
If context variables aren't working:
- Verify `context_access_enabled: true` in agent YAML
- Check that variable names match exactly (case-sensitive)
- Ensure variables are listed in `context_variables` array

### Tool Execution Errors
If the tool fails to execute:
- Check that the tool was imported successfully
- Verify the tool name matches in agent configuration
- Review tool logs in watsonx Orchestrate console

## References

- [IBM watsonx Orchestrate - Managing Agent Analytics](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=settings-managing-agent-analytics#pii-regular-expression-patterns)
- [watsonx Orchestrate ADK - Context Variables](https://developer.watson-orchestrate.ibm.com/agents/build_agent)
- [watsonx Orchestrate ADK - Python Tools](https://developer.watson-orchestrate.ibm.com/tools/create_tool)

## License

This is a demonstration project for watsonx Orchestrate capabilities.

## Support

For questions or issues:
1. Check the IBM watsonx Orchestrate documentation
2. Review the ADK reference materials
3. Contact your watsonx Orchestrate administrator