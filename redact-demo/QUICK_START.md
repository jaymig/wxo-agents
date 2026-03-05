# Redact Demo Agent - Quick Start Guide

## Installation (5 minutes)

```bash
cd redact-demo
./import_all.sh
```

## Usage Examples

### Run the Complete Demo
**User**: "Run the PII redaction demo"

**Agent Response**: Executes the complete 3-step demonstration:

**Step 1 - Display Values to Write:**
Shows all 9 PII example values that will be written to context variables

**Step 2 - Write to Context:**
Writes all values to their respective context variables

**Step 3 - Read and Verify:**
Reads back all values from context to confirm they were stored correctly

The tool displays:
- 📧 Email: john.doe@example.com
- 📅 Date: 12/25/2023
- 🔢 SSN: 123-45-6789
- 💳 Credit Card: 4532-1234-5678-9010
- 📱 Phone: +1 (555) 123-4567
- 🌐 IP Address: 192.168.1.100
- 🏠 Postal Address: 123 Main Street, Apt 4B, New York, NY 10001
- 🏥 Health Insurance: ABC123456789
- 💰 Salary: $75,000 per year

### Other Prompts
**User**: "Demonstrate PII redaction"
**User**: "Show me how PII context variables work"
**User**: "Explain how PII redaction protects sensitive data"

## Key Features

✅ **Single Comprehensive Tool**: One tool demonstrates the complete PII lifecycle

✅ **3-Step Process**: Display → Write → Read & Verify

✅ **9 PII Types Covered**: Email, Date, SSN, Credit Card, Phone, IP Address, Postal Address, Health Insurance, Salary

✅ **Context Variables**: Demonstrates both writing to and reading from context variables

✅ **Analytics Ready**: All patterns match IBM's documented regex patterns for redaction

✅ **Educational**: Clear step-by-step explanations of how PII redaction works

## Demo Flow

1. **Run Demo**: Ask agent to run the PII redaction demo
2. **Review Output**: See all 3 steps (Display → Write → Read)
3. **Understand**: Agent explains how redaction protects the data
4. **Verify**: Check analytics dashboard to see redaction in action

## PII Types Reference

| Type | Example Value | Context Variable |
|------|---------------|------------------|
| Email | john.doe@example.com | `pii_email` |
| Date | 12/25/2023 | `pii_date` |
| SSN | 123-45-6789 | `pii_ssn` |
| Credit Card | 4532-1234-5678-9010 | `pii_credit_card` |
| Phone | +1 (555) 123-4567 | `pii_phone` |
| IP Address | 192.168.1.100 | `pii_ip_address` |
| Postal Address | 123 Main Street, Apt 4B, New York, NY 10001 | `pii_postal_address` |
| Health Insurance | ABC123456789 | `pii_health_insurance` |
| Salary | $75,000 per year | `pii_salary` |

## Troubleshooting

**Q: Tool not found?**
A: Re-run `./import_all.sh` to ensure the tool is imported

**Q: Demo not running?**
A: Check that the agent is properly imported and available in your instance

**Q: Context variables not persisting?**
A: Context variables persist only during the conversation session

## Next Steps

- Review the full [README.md](README.md) for detailed documentation
- Check IBM's [PII Redaction Documentation](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=settings-managing-agent-analytics#pii-regular-expression-patterns)
- Explore context variable usage in your own agents