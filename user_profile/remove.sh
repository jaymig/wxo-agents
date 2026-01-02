#!/bin/bash
set -x


## Un deploy agents
orchestrate agents undeploy --name profile_collaborator_agent
orchestrate agents undeploy --name profile_supervisor_agent

## remove agents
orchestrate agents remove -n profile_supervisor_agent -k native
orchestrate agents remove -n profile_collaborator_agent -k native

## remove tool
orchestrate tools remove --name context_from_session


