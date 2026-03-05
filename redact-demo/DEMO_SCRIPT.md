# Redact Demo Agent - Demo Script

## Introduction Script

"Today I'll demonstrate the PII redaction capabilities in watsonx Orchestrate using our Redact Demo agent. This agent showcases how context variables can store sensitive information and how that information is automatically redacted in analytics."

## Demo Flow

### Part 1: Agent Introduction (1 minute)

**Say**: "Let me show you the Redact Demo agent. This agent has been configured with 9 different types of PII context variables, matching IBM's documented redaction patterns."

**Show**: Navigate to the agent in watsonx Orchestrate

**Highlight**:
- Agent name: "redact_demo"
- Purpose: PII redaction demonstration
- Two tools available

---

### Part 2: Setting Up PII Data (2 minutes)

**Say**: "First, let's populate the context variables with example PII data."

**User Input**:
```
Set up example PII data
```

**Expected Response**:
```
✅ Successfully populated PII context variables with example values:

📧 Email: john.doe@example.com
📅 Date: 12/25/2023
🔢 SSN: 123-45-6789
💳 Credit Card: 4532-1234-5678-9010
📱 Phone: +1 (555) 123-4567
🌐 IP Address: 192.168.1.100
🏠 Postal Address: 123 Main Street, Apt 4B, New York, NY 10001
🏥 Health Insurance: ABC123456789
💰 Salary: $75,000 per year

These values are now stored in context variables...
```

**Explain**:
- "The agent just called the `set_pii_examples` tool"
- "This tool populated 9 context variables with example PII data"
- "Each type corresponds to a regex pattern used for redaction"

---

### Part 3: Displaying PII Values (2 minutes)

**Say**: "Now let's verify what's stored in the context variables."

**User Input**:
```
Show me the current PII values
```

**Expected Response**:
```
📋 Current PII Context Variables:

📧 Email: john.doe@example.com
📅 Date: 12/25/2023
🔢 SSN: 123-45-6789
💳 Credit Card: 4532-1234-5678-9010
📱 Phone: +1 (555) 123-4567
🌐 IP Address: 192.168.1.100
🏠 Postal Address: 123 Main Street, Apt 4B, New York, NY 10001
🏥 Health Insurance: ABC123456789
💰 Salary: $75,000 per year

✅ These values are stored in context variables...
```

**Explain**:
- "The agent called the `display_pii_context` tool"
- "This tool reads from the context variables we just set"
- "Notice all 9 PII types are displayed"

---

### Part 4: Understanding Redaction (3 minutes)

**Say**: "Let me explain how PII redaction works with these values."

**User Input**:
```
How does PII redaction work with these values?
```

**Expected Response** (agent will explain):
- Context variables store the sensitive data
- When analytics are enabled, regex patterns match these formats
- Matched patterns are automatically redacted in logs and analytics
- The original data remains in the conversation context

**Show**: Navigate to analytics settings (if available)

**Highlight**:
- PII redaction toggle
- List of supported PII types
- Regex patterns for each type

---

### Part 5: Demonstrating Each PII Type (5 minutes)

**Say**: "Let's look at each PII type individually."

#### Email
**User Input**: "Tell me about the email PII type"

**Explain**:
- Pattern: `\b[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b`
- Example: john.doe@example.com
- Redacted as: [REDACTED] or [EMAIL]

#### SSN
**User Input**: "What about Social Security Numbers?"

**Explain**:
- Pattern: `\b(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}\b`
- Example: 123-45-6789
- Redacted as: [REDACTED] or [SSN]

#### Credit Card
**User Input**: "Show me credit card redaction"

**Explain**:
- Pattern: `\b(?:\d{4}[-\s]?){3}\d{4}\b`
- Example: 4532-1234-5678-9010
- Redacted as: [REDACTED] or [CREDIT_CARD]

#### Phone Number
**User Input**: "How are phone numbers handled?"

**Explain**:
- Pattern: `(?:\+?(\d{1,3}))?(?: ?\([-\s]?)?(?:\d{1,4})?\)?(?:[-\s]?\d{2,5}){2,}\b`
- Example: +1 (555) 123-4567
- Redacted as: [REDACTED] or [PHONE]

---

### Part 6: Real-World Scenario (3 minutes)

**Say**: "Let me show you a real-world scenario where this matters."

**User Input**:
```
I need to update my contact information. My email is john.doe@example.com, 
my phone is +1 (555) 123-4567, and my SSN is 123-45-6789.
```

**Expected Response**:
Agent acknowledges the information (stored in context)

**Then Show**: Analytics dashboard

**Explain**:
- "In the conversation, we see the actual values"
- "But in analytics, these would appear as [REDACTED]"
- "This protects sensitive information while maintaining functionality"

---

### Part 7: Benefits Overview (2 minutes)

**Say**: "Let me summarize the key benefits of PII redaction."

**Highlight**:

1. **Privacy Protection**
   - Sensitive data masked in logs
   - Compliance with data protection regulations
   - Reduced risk of data exposure

2. **Operational Transparency**
   - Analytics still show conversation patterns
   - Can track agent performance
   - Identify common user requests

3. **Flexibility**
   - Configure which PII types to redact
   - Custom regex patterns supported
   - Per-agent configuration available

4. **Ease of Use**
   - Automatic redaction (no code changes)
   - Works with context variables
   - Transparent to end users

---

### Part 8: Q&A Scenarios

#### Q: "Can I add custom PII types?"
**A**: "Yes! You can define custom regex patterns in the analytics settings and add corresponding context variables to your agent."

#### Q: "Does redaction affect agent functionality?"
**A**: "No, redaction only affects what's stored in analytics and logs. The agent still has access to the actual values during the conversation."

#### Q: "What happens if I don't use context variables?"
**A**: "Redaction still works based on regex pattern matching in the conversation text, but context variables provide more control and clarity."

#### Q: "Can I see the redacted data?"
**A**: "Administrators with proper permissions can access the original data if needed for debugging or compliance purposes."

---

## Demo Variations

### Quick Demo (5 minutes)
1. Set up PII data
2. Display values
3. Explain redaction concept
4. Show one example (email or SSN)

### Technical Deep Dive (15 minutes)
1. Show agent YAML configuration
2. Explain context variable setup
3. Walk through tool code
4. Demonstrate each PII type
5. Show analytics dashboard
6. Discuss regex patterns

### Business-Focused Demo (10 minutes)
1. Explain compliance requirements
2. Show PII redaction in action
3. Highlight business benefits
4. Discuss use cases
5. ROI and risk reduction

---

## Talking Points

### For Technical Audiences
- "Context variables provide type-safe PII storage"
- "Regex patterns are configurable and extensible"
- "Tools use the AgentRun object for context access"
- "Redaction happens at the analytics layer"

### For Business Audiences
- "Protects customer privacy automatically"
- "Helps meet GDPR, CCPA, and other regulations"
- "Reduces risk of data breaches"
- "Maintains operational visibility"

### For Compliance Audiences
- "Automatic PII masking in all logs"
- "Configurable redaction policies"
- "Audit trail of all interactions"
- "Supports data minimization principles"

---

## Common Questions & Answers

**Q**: How many PII types are supported?
**A**: This demo covers 9 types, but you can add custom patterns for additional types.

**Q**: Does this work with external agents?
**A**: Yes, context variables work with both native and external agents.

**Q**: Can I turn off redaction for specific conversations?
**A**: Redaction is configured at the agent or instance level, not per-conversation.

**Q**: What if a PII pattern matches non-sensitive data?
**A**: You can refine the regex patterns to be more specific and reduce false positives.

**Q**: Is there a performance impact?
**A**: Minimal - regex matching is very fast and happens asynchronously.

---

## Follow-Up Actions

After the demo, suggest:

1. **Try It Yourself**
   - Import the agent in your environment
   - Test with different PII values
   - Review analytics dashboard

2. **Customize**
   - Add your organization's PII types
   - Adjust regex patterns
   - Configure redaction policies

3. **Integrate**
   - Use context variables in your agents
   - Enable PII redaction in production
   - Train team on best practices

4. **Monitor**
   - Review analytics regularly
   - Verify redaction is working
   - Adjust patterns as needed

---

## Demo Checklist

Before the demo:
- [ ] Agent imported and tested
- [ ] Tools working correctly
- [ ] Analytics dashboard accessible
- [ ] Example prompts prepared
- [ ] Backup plan if live demo fails

During the demo:
- [ ] Clear, confident delivery
- [ ] Show, don't just tell
- [ ] Engage audience with questions
- [ ] Handle questions smoothly
- [ ] Stay on time

After the demo:
- [ ] Share documentation links
- [ ] Provide import script
- [ ] Offer follow-up support
- [ ] Collect feedback
- [ ] Schedule next steps

---

**Demo Duration**: 15-20 minutes (full version)
**Audience Level**: All levels (adjust technical depth as needed)
**Prerequisites**: watsonx Orchestrate access, Redact Demo agent imported