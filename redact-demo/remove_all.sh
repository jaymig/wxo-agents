#!/bin/bash

# Remove script for Redact Demo Agent
# This script removes the agent and its tools from watsonx Orchestrate

echo "=========================================="
echo "Removing Redact Demo Agent"
echo "=========================================="
echo ""

# Confirm before proceeding
read -p "Are you sure you want to remove the Redact Demo agent and its tools? (y/N) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "❌ Removal cancelled"
    exit 0
fi

echo ""

# Remove the agent
echo "🤖 Removing Redact Demo agent..."
orchestrate agents delete redact_demo
if [ $? -eq 0 ]; then
    echo "✅ Redact Demo agent removed successfully"
else
    echo "⚠️  Failed to remove Redact Demo agent (may not exist)"
fi
echo ""

# Remove the tool
echo "📦 Removing tool..."
echo ""

echo "  → Removing pii_redaction_demo tool..."
orchestrate tools delete pii_redaction_demo
if [ $? -eq 0 ]; then
    echo "  ✅ pii_redaction_demo tool removed successfully"
else
    echo "  ⚠️  Failed to remove pii_redaction_demo tool (may not exist)"
fi
echo ""

echo "=========================================="
echo "✅ Removal Complete!"
echo "=========================================="
echo ""
echo "The Redact Demo agent and its tools have been removed from watsonx Orchestrate."
echo ""
echo "To reinstall, run: ./import_all.sh"
echo ""

# Made with Bob
