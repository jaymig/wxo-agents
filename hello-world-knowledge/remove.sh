#!/bin/bash
set -x

# remove agents
orchestrate agents remove -n hello_agent_knowledge -k native

# remove tool
orchestrate tools remove --name hello_world_tool


# Remove Knowledge
orchestrate knowledge-bases remove --name knowledge_base_for_agent_Hello_world