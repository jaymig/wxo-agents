#!/bin/bash
set -x


## Un deploy agents
orchestrate agents undeploy --name context_collaborator_agent
orchestrate agents undeploy --name context_supervisor_agent

## remove agents
orchestrate agents remove -n context_supervisor_agent -k native
orchestrate agents remove -n context_collaborator_agent -k native

## remove tool
orchestrate tools remove --name return_context


