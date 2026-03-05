# Redact Demo Agent - Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     watsonx Orchestrate                          │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    Redact Demo Agent                        │ │
│  │                                                              │ │
│  │  Name: redact_demo                                          │ │
│  │  Style: react                                               │ │
│  │  LLM: groq/openai/gpt-oss-120b                             │ │
│  │  Context Access: Enabled                                    │ │
│  │                                                              │ │
│  │  ┌──────────────────────────────────────────────────────┐  │ │
│  │  │         Context Variables (9 PII Types)              │  │ │
│  │  │                                                        │  │ │
│  │  │  • pii_email          • pii_phone                    │  │ │
│  │  │  • pii_date           • pii_ip_address               │  │ │
│  │  │  • pii_ssn            • pii_postal_address           │  │ │
│  │  │  • pii_credit_card    • pii_health_insurance         │  │ │
│  │  │  • pii_salary                                         │  │ │
│  │  └──────────────────────────────────────────────────────┘  │ │
│  │                                                              │ │
│  │  ┌──────────────────────────────────────────────────┐   │ │
│  │  │         pii_redaction_demo Tool                  │   │ │
│  │  │                                                   │   │ │
│  │  │  Step 1: Display example PII values              │   │ │
│  │  │  Step 2: Write to context variables              │   │ │
│  │  │  Step 3: Read back and verify storage            │   │ │
│  │  └──────────────────────────────────────────────────┘   │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │              Analytics & PII Redaction Layer                │ │
│  │                                                              │ │
│  │  Regex Patterns:                                            │ │
│  │  • Email Pattern      → Redacts email addresses            │ │
│  │  • SSN Pattern        → Redacts social security numbers    │ │
│  │  • Credit Card Pattern → Redacts credit card numbers       │ │
│  │  • Phone Pattern      → Redacts phone numbers              │ │
│  │  • IP Pattern         → Redacts IP addresses               │ │
│  │  • Address Pattern    → Redacts postal addresses           │ │
│  │  • Health Ins Pattern → Redacts health insurance numbers   │ │
│  │  • Salary Pattern     → Redacts salary information         │ │
│  │  • Date Pattern       → Redacts date information           │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

### Complete PII Demonstration Flow

```
User Request
    │
    ├─> "Run the PII redaction demonstration"
    │
    v
Agent Processing
    │
    ├─> Understands intent
    │
    v
Tool Invocation: pii_redaction_demo
    │
    ├─> Receives AgentRun context
    │
    v
STEP 1: Display Example Values
    │
    ├─> Shows all 9 PII values that will be written
    │
    v
STEP 2: Write to Context Variables
    │
    ├─> pii_email = "john.doe@example.com"
    ├─> pii_date = "12/25/2023"
    ├─> pii_ssn = "123-45-6789"
    ├─> pii_credit_card = "4532-1234-5678-9010"
    ├─> pii_phone = "+1 (555) 123-4567"
    ├─> pii_ip_address = "192.168.1.100"
    ├─> pii_postal_address = "123 Main Street..."
    ├─> pii_health_insurance = "ABC123456789"
    └─> pii_salary = "$75,000 per year"
    │
    v
STEP 3: Read Back and Verify
    │
    ├─> Read all 9 context variables
    ├─> Confirm values were stored correctly
    │
    v
Tool Response
    │
    ├─> Comprehensive report showing all 3 steps
    │
    v
Agent Response to User
    │
    └─> Complete demonstration output with explanations
```

## Component Interactions

```
┌──────────────┐
│     User     │
└──────┬───────┘
       │
       │ Natural Language Request
       │
       v
┌──────────────────────────────────────┐
│      Redact Demo Agent               │
│                                      │
│  ┌────────────────────────────────┐ │
│  │   LLM Processing               │ │
│  │   (groq/openai/gpt-oss-120b)  │ │
│  └────────────┬───────────────────┘ │
│               │                      │
│               │ Tool Selection       │
│               │                      │
│       │                             │
│       v                             │
│  ┌──────────────────────────────┐ │
│  │  pii_redaction_demo Tool     │ │
│  │                               │ │
│  │  1. Display example values   │ │
│  │  2. Write to context         │ │
│  │  3. Read back and verify     │ │
│  └────┬─────────────────────────┘ │
│       │                             │
│       │ Write & Read                │
│       │                             │
│       v                             │
│  ┌────────────────────────────┐   │
│  │   Context Variables        │   │
│  │   (9 PII Types)            │   │
│  └────────────────────────────┘   │
└──────────────────────────────────────┘
       │
       │ Response
       │
       v
┌──────────────┐
│     User     │
└──────────────┘
```

## Context Variable Lifecycle

```
1. Declaration (Agent YAML)
   ↓
   context_variables:
     - pii_email
     - pii_date
     - ...

2. Initialization (Optional)
   ↓
   Variables start as undefined/null

3. Population (pii_redaction_demo tool - Step 2)
   ↓
   req_context.update({
     'pii_email': 'john.doe@example.com',
     'pii_date': '12/25/2023',
     ...
   })

4. Verification (pii_redaction_demo tool - Step 3)
   ↓
   value = req_context.get('pii_email')

5. Persistence
   ↓
   Variables persist throughout conversation session

6. Redaction (Analytics Layer)
   ↓
   Regex patterns match and mask PII in logs/analytics
```

## PII Redaction Process

```
┌─────────────────────────────────────────────────────────┐
│                  Conversation Flow                       │
└─────────────────┬───────────────────────────────────────┘
                  │
                  │ Contains PII data
                  │
                  v
┌─────────────────────────────────────────────────────────┐
│              Analytics Processing                        │
│                                                          │
│  Input: "My email is john.doe@example.com"             │
│         "My SSN is 123-45-6789"                        │
│         "Call me at +1 (555) 123-4567"                 │
│                                                          │
│  ┌────────────────────────────────────────────────┐   │
│  │         Regex Pattern Matching                  │   │
│  │                                                  │   │
│  │  Email Pattern:    \b[a-zA-Z0-9._+-]+@...      │   │
│  │  SSN Pattern:      \b(?!666|000|9\d{2})\d{3}... │   │
│  │  Phone Pattern:    (?:\+?(\d{1,3}))?...        │   │
│  └────────────────────────────────────────────────┘   │
│                                                          │
│  Output: "My email is [REDACTED]"                      │
│          "My SSN is [REDACTED]"                        │
│          "Call me at [REDACTED]"                       │
└─────────────────────────────────────────────────────────┘
                  │
                  │ Redacted data
                  │
                  v
┌─────────────────────────────────────────────────────────┐
│            Analytics Dashboard / Logs                    │
│                                                          │
│  Safe to view - No PII exposed                          │
└─────────────────────────────────────────────────────────┘
```

## Tool Architecture

### pii_redaction_demo Tool

```python
@tool
def pii_redaction_demo(context: AgentRun) -> str:
    """
    Complete PII redaction demonstration tool
    
    Input: AgentRun context object
    
    Process:
    1. Display example PII values that will be written
    2. Write all 9 PII values to context variables
    3. Read back all values to confirm storage
    4. Format comprehensive demonstration report
    
    Output: Multi-step formatted report showing:
    - Step 1: Example values to write
    - Step 2: Write operation confirmation
    - Step 3: Read-back verification
    - Summary and redaction explanation
    """
```

**Key Operations:**
- `req_context = context.request_context` - Get context accessor
- `req_context.update({...})` - Bulk update all 9 variables
- `value = req_context.get('variable_name')` - Read back for verification
- Returns comprehensive 3-step demonstration report

## Security Considerations

```
┌─────────────────────────────────────────────────────────┐
│                  Security Layers                         │
│                                                          │
│  1. Context Variable Isolation                          │
│     └─> Variables only accessible within agent session  │
│                                                          │
│  2. PII Redaction in Analytics                          │
│     └─> Automatic masking based on regex patterns       │
│                                                          │
│  3. Access Control                                       │
│     └─> Only authorized users can access agent          │
│                                                          │
│  4. Audit Trails                                         │
│     └─> All interactions logged (with redaction)        │
└─────────────────────────────────────────────────────────┘
```

## Deployment Architecture

```
Development Environment
    │
    ├─> Create agent YAML
    ├─> Create Python tools
    ├─> Create documentation
    │
    v
Local Testing
    │
    ├─> Validate YAML syntax
    ├─> Check tool structure
    │
    v
Import Script (import_all.sh)
    │
    ├─> Import tool via ADK
    ├─> Import agent via ADK
    │
    v
watsonx Orchestrate Platform
    │
    ├─> Tool registered
    ├─> Agent deployed
    ├─> Context variables configured
    │
    v
Production Use
    │
    └─> Users interact with agent
```

## Performance Characteristics

- **Tool Execution**: < 1 second per tool call
- **Context Variable Access**: Immediate (in-memory)
- **Agent Response Time**: 2-5 seconds (depends on LLM)
- **Redaction Processing**: Real-time (regex matching)

## Scalability

- **Concurrent Users**: Supports multiple simultaneous conversations
- **Context Isolation**: Each session has independent context
- **Tool Reusability**: Tool can be used by multiple agents
- **Variable Limit**: No practical limit on context variable count

## Extension Points

1. **Add More PII Types**
   - Declare new context variable in agent YAML
   - Update pii_redaction_demo tool to include new type
   - Add to pii_examples dictionary

2. **Custom Redaction Patterns**
   - Configure in analytics settings
   - Match variable naming convention

3. **Additional Tools**
   - Create new tools that read/write context
   - Add to agent's tools list
   - Can work alongside pii_redaction_demo

4. **Integration with External Systems**
   - Tool can call external APIs
   - Store results in context variables
   - Display in demonstration output

---

**Architecture Version**: 1.0
**Last Updated**: 2026-03-05
**Platform**: IBM watsonx Orchestrate