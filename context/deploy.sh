#!/bin/bash
set -x

## import tools
orchestrate tools import -k python -f ./tools/return_context.py

## Import collaborator agent
orchestrate agents import -f ./agents/context_collaborator_agent.json

## Import supervisor agent
orchestrate agents import -f ./agents/context_supervisor_agent.json

