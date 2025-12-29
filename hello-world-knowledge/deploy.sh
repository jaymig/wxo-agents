#!/bin/bash
set -x

## import knowledege base
orchestrate knowledge-bases import -f ./knowledge/knowledge_base.json

## import tools
orchestrate tools import -k openapi -f ./tools/hello-world-tool.json

## Import collaborator agent
orchestrate agents import -f ./agents/hello-agent-with-knowledge.json

## Publish agent to live environment
orchestrate agents deploy --name hello_agent_knowledge

