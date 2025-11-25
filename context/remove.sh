#!/bin/bash
set -x

# remove agents
orchestrate agents remove -n context_supervisor_agent -k native
orchestrate agents remove -n context_collaborator_agent -k native

# remove tool
orchestrate tools remove --name return_context


