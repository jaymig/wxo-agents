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
│  │  ┌──────────────────┐      ┌──────────────────────────┐   │ │
│  │  │ set_pii_examples │      │ display_pii_context      │   │ │
│  │  │                  │      │                          │   │ │
│  │  │ Writes to        │      │ Reads from               │   │ │
│  │  │ context vars     │      │ context vars             │   │ │
│  │  └──────────────────┘      └──────────────────────────┘   │ │
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

### Scenario 1: Setting PII Examples

```
User Request
    │
    ├─> "Set up example PII data"
    │
    v
Agent Processing
    │
    ├─> Understands intent
    │
    v
Tool Invocation: set_pii_examples
    │
    ├─> Receives AgentRun context
    │
    v
Context Variable Updates
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
Tool Response
    │
    ├─> Formatted confirmation message
    │
    v
Agent Response to User
    │
    └─> "✅ Successfully populated PII context variables..."
```

### Scenario 2: Displaying PII Values

```
User Request
    │
    ├─> "Show me the current PII values"
    │
    v
Agent Processing
    │
    ├─> Understands intent
    │
    v
Tool Invocation: display_pii_context
    │
    ├─> Receives AgentRun context
    │
    v
Context Variable Reads
    │
    ├─> Read pii_email
    ├─> Read pii_date
    ├─> Read pii_ssn
    ├─> Read pii_credit_card
    ├─> Read pii_phone
    ├─> Read pii_ip_address
    ├─> Read pii_postal_address
    ├─> Read pii_health_insurance
    └─> Read pii_salary
    │
    v
Tool Response
    │
    ├─> Formatted display of all values
    │
    v
Agent Response to User
    │
    └─> "📋 Current PII Context Variables:..."
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
│       ┌───────┴────────┐            │
│       │                │            │
│       v                v            │
│  ┌─────────┐    ┌──────────────┐  │
│  │  Tool 1 │    │    Tool 2    │  │
│  │  set_   │    │   display_   │  │
│  │  pii_   │    │   pii_       │  │
│  │ examples│    │  context     │  │
│  └────┬────┘    └──────┬───────┘  │
│       │                │            │
│       │ Write          │ Read       │
│       │                │            │
│       v                v            │
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

3. Population (set_pii_examples tool)
   ↓
   req_context.update({
     'pii_email': 'john.doe@example.com',
     'pii_date': '12/25/2023',
     ...
   })

4. Access (display_pii_context tool)
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

### set_pii_examples Tool

```python
@tool
def set_pii_examples(context: AgentRun) -> str:
    """
    Input: AgentRun context object
    
    Process:
    1. Access request_context
    2. Create dictionary of PII examples
    3. Update context with all values
    4. Format confirmation message
    
    Output: Formatted string with all PII values
    """
```

**Key Operations:**
- `req_context = context.request_context` - Get context accessor
- `req_context.update({...})` - Bulk update multiple variables
- Returns formatted confirmation message

### display_pii_context Tool

```python
@tool
def display_pii_context(context: AgentRun) -> str:
    """
    Input: AgentRun context object
    
    Process:
    1. Access request_context
    2. Read each PII variable
    3. Check if values are set
    4. Format display message
    
    Output: Formatted string showing all values
    """
```

**Key Operations:**
- `req_context = context.request_context` - Get context accessor
- `value = req_context.get('variable_name')` - Read individual variables
- Returns formatted display message

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
    ├─> Import tools via ADK
    ├─> Import agent via ADK
    │
    v
watsonx Orchestrate Platform
    │
    ├─> Tools registered
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
- **Tool Reusability**: Tools can be used by multiple agents
- **Variable Limit**: No practical limit on context variable count

## Extension Points

1. **Add More PII Types**
   - Declare new context variable
   - Update set_pii_examples tool
   - Update display_pii_context tool

2. **Custom Redaction Patterns**
   - Configure in analytics settings
   - Match variable naming convention

3. **Additional Tools**
   - Create new tools that read/write context
   - Add to agent's tools list

4. **Integration with External Systems**
   - Tools can call external APIs
   - Store results in context variables
   - Display via existing tools

---

**Architecture Version**: 1.0
**Last Updated**: 2026-03-05
**Platform**: IBM watsonx Orchestrate