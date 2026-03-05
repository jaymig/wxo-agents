#!/bin/bash

# Import script for Redact Demo Agent
# This script imports the agent and its tools into watsonx Orchestrate

echo "=========================================="
echo "Importing Redact Demo Agent"
echo "=========================================="
echo ""

# Import the tool
echo "📦 Importing tool..."
echo ""

echo "  → Importing pii_redaction_demo tool..."
orchestrate tools import --kind python --file tools/pii_redaction_demo.py
if [ $? -eq 0 ]; then
    echo "  ✅ pii_redaction_demo tool imported successfully"
else
    echo "  ❌ Failed to import pii_redaction_demo tool"
    exit 1
fi
echo ""

# Import the agent
echo "🤖 Importing Redact Demo agent..."
orchestrate agents import --file agents/redact_demo_agent.yaml
if [ $? -eq 0 ]; then
    echo "✅ Redact Demo agent imported successfully"
else
    echo "❌ Failed to import Redact Demo agent"
    exit 1
fi
echo ""

echo "=========================================="
echo "✅ Import Complete!"
echo "=========================================="
echo ""
echo "The Redact Demo agent is now available in watsonx Orchestrate."
echo ""
echo "To use the agent:"
echo "1. Open watsonx Orchestrate"
echo "2. Find the 'redact_demo' agent"
echo "3. Ask it to demonstrate PII redaction"
echo ""
echo "Example prompts:"
echo "  - 'Run the PII redaction demo'"
echo "  - 'Demonstrate PII redaction'"
echo "  - 'Show me how PII context variables work'"
echo ""

# Made with Bob
