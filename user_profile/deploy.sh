#!/bin/bash
set -x

## import tools
orchestrate tools import -k python -f ./tools/return_context.py

## Import collaborator agent
orchestrate agents import -f ./agents/profile_collaborator_agent.json

## Import supervisor agent
orchestrate agents import -f ./agents/profile_supervisor_agent.json

## deploy agents

orchestrate agents deploy --name profile_collaborator_agent
orchestrate agents deploy --name profile_supervisor_agent
