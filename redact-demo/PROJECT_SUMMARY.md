# Redact Demo Agent - Project Summary

## Overview
A complete watsonx Orchestrate agent demonstrating PII (Personally Identifiable Information) redaction capabilities using context variables. This agent showcases all 9 PII types documented in IBM's analytics redaction patterns.

## Project Structure

```
redact-demo/
├── agents/
│   └── redact_demo_agent.yaml          # Main agent configuration
├── tools/
│   └── pii_redaction_demo.py           # Complete PII demonstration tool
├── import_all.sh                        # Automated deployment script
├── README.md                            # Comprehensive documentation
├── QUICK_START.md                       # Quick reference guide
└── PROJECT_SUMMARY.md                   # This file
```

## Components

### 1. Agent: redact_demo
- **Purpose**: Demonstrate PII redaction with context variables
- **Style**: React (conversational)
- **LLM**: groq/openai/gpt-oss-120b
- **Context Access**: Enabled
- **Context Variables**: 9 PII-specific variables
- **Tool**: 1 (pii_redaction_demo)

### 2. Tool: pii_redaction_demo
- **Type**: Python tool
- **Function**: Complete PII lifecycle demonstration in 3 steps
  - Step 1: Display example PII values
  - Step 2: Write all 9 PII values to context variables
  - Step 3: Read back and verify storage
- **Context Access**: Uses AgentRun to both write and read context
- **Output**: Comprehensive 3-step demonstration report

## PII Types Covered

Based on IBM's documentation at:
https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=settings-managing-agent-analytics#pii-regular-expression-patterns

1. **Email** - `pii_email`
   - Example: john.doe@example.com
   - Pattern: Email address format

2. **Date** - `pii_date`
   - Example: 12/25/2023
   - Pattern: Date formats (MM/DD/YYYY, etc.)

3. **SSN** - `pii_ssn`
   - Example: 123-45-6789
   - Pattern: Social Security Number format

4. **Credit Card** - `pii_credit_card`
   - Example: 4532-1234-5678-9010
   - Pattern: Credit card number format

5. **Phone** - `pii_phone`
   - Example: +1 (555) 123-4567
   - Pattern: Various phone number formats

6. **IP Address** - `pii_ip_address`
   - Example: 192.168.1.100
   - Pattern: IPv4 address format

7. **Postal Address** - `pii_postal_address`
   - Example: 123 Main Street, Apt 4B, New York, NY 10001
   - Pattern: US postal address format

8. **Health Insurance** - `pii_health_insurance`
   - Example: ABC123456789
   - Pattern: Health insurance number format

9. **Salary** - `pii_salary`
   - Example: $75,000 per year
   - Pattern: Salary/monetary amount formats

## Key Features

### Context Variable Management
- Demonstrates proper use of `context_access_enabled`
- Shows how to declare context variables in agent YAML
- Implements read and write operations using AgentRun

### PII Redaction Integration
- All example values match IBM's documented regex patterns
- Ready for analytics redaction when enabled
- Educational explanations of how redaction works

### User-Friendly Tools
- Clear, formatted output with emojis for readability
- Helpful error messages when values aren't set
- Links to IBM documentation for reference

## Technical Implementation

### Agent Configuration (YAML)
```yaml
context_access_enabled: true
context_variables:
  - pii_email
  - pii_date
  - pii_ssn
  - pii_credit_card
  - pii_phone
  - pii_ip_address
  - pii_postal_address
  - pii_health_insurance
  - pii_salary
```

### Tool Implementation (Python)
```python
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run.context import AgentRun

@tool
def tool_name(context: AgentRun) -> str:
    req_context = context.request_context
    
    # Read from context
    value = req_context.get('variable_name')
    
    # Write to context
    req_context['variable_name'] = 'new_value'
    
    # Bulk update
    req_context.update({'var1': 'val1', 'var2': 'val2'})
```

## Deployment

### Prerequisites
- watsonx Orchestrate ADK installed
- Access to watsonx Orchestrate instance
- Proper credentials configured

### Installation Steps
```bash
cd redact-demo
./import_all.sh
```

### Verification
1. Check that the tool is imported
2. Verify agent is available in watsonx Orchestrate
3. Test by asking agent to run the PII demonstration
4. Confirm all 3 steps execute successfully

## Usage Scenarios

### Demo Scenario 1: Complete Demonstration
1. User: "Run the PII redaction demonstration"
2. Agent uses `pii_redaction_demo` tool
3. Tool executes all 3 steps (Display → Write → Verify)
4. Agent explains how redaction works

### Demo Scenario 2: Educational
1. User: "Explain PII redaction"
2. Agent explains the concept
3. Agent runs the demonstration tool
4. Agent shows how patterns are redacted in analytics

### Demo Scenario 3: Analytics Verification
1. Run the PII demonstration
2. Have conversation referencing PII values
3. Check analytics dashboard
4. Verify redaction is working

## Benefits

### For Demonstrations
- ✅ Shows all 9 PII types in one execution
- ✅ Clear 3-step process (Display → Write → Verify)
- ✅ Visual output with emojis
- ✅ Educational explanations included
- ✅ Easy to deploy and use

### For Learning
- ✅ Complete example of context variable usage
- ✅ Shows both read and write operations in one tool
- ✅ Demonstrates proper tool structure
- ✅ Includes comprehensive documentation

### For Development
- ✅ Template for context variable agents
- ✅ Reusable tool pattern
- ✅ Best practices implementation
- ✅ Ready for customization

## Customization Options

### Add More PII Types
1. Add new context variable to agent YAML
2. Update `pii_examples` dictionary in `pii_redaction_demo.py`
3. Update the display sections in the tool
4. Re-import tool and agent

### Modify Example Values
1. Edit the `pii_examples` dictionary in `pii_redaction_demo.py`
2. Update display formatting if needed
3. Re-import tool

### Change Agent Behavior
1. Modify instructions in agent YAML
2. Adjust LLM model if needed
3. Re-import agent

## Testing Checklist

- [ ] Import script runs without errors
- [ ] Tool appears in watsonx Orchestrate
- [ ] Agent is available and accessible
- [ ] `pii_redaction_demo` tool executes all 3 steps successfully
- [ ] Step 1 displays all 9 example values
- [ ] Step 2 writes all values to context variables
- [ ] Step 3 reads back and verifies all values
- [ ] Agent responds appropriately to user prompts
- [ ] Context variables persist during conversation
- [ ] Analytics redaction works (if enabled)

## Documentation Files

1. **README.md** - Complete technical documentation
2. **QUICK_START.md** - Fast reference guide
3. **PROJECT_SUMMARY.md** - This overview document

## References

- [IBM PII Redaction Patterns](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=settings-managing-agent-analytics#pii-regular-expression-patterns)
- [watsonx Orchestrate Context Variables](https://developer.watson-orchestrate.ibm.com/agents/build_agent)
- [watsonx Orchestrate Python Tools](https://developer.watson-orchestrate.ibm.com/tools/create_tool)

## Version History

- **v1.0** - Initial release with 9 PII types and 1 comprehensive tool

## Support

For issues or questions:
1. Review the README.md documentation
2. Check the QUICK_START.md guide
3. Consult IBM watsonx Orchestrate documentation
4. Contact your watsonx Orchestrate administrator

---

**Created**: 2026-03-05
**Purpose**: PII Redaction Demonstration
**Platform**: IBM watsonx Orchestrate