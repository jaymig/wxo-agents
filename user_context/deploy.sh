#!/bin/bash
set -x

## import tools
orchestrate tools import -k python -f ./tools/user_info.py -r ./tools/requirements.txt
orchestrate tools import -k python -f ./tools/update_user_context.py -r ./tools/requirements.txt
orchestrate tools import -k python -f ./tools/session_context.py -r ./tools/requirements.txt
orchestrate tools import -k python -f ./tools/update_user_profile.py -r ./tools/requirements.txt
orchestrate tools import -k python -f ./tools/read_user_profile.py -r ./tools/requirements.txt

## Import Welcome agent
orchestrate agents import -f ./agents/welcome_agent.yaml

## Publish agent to live environment
orchestrate agents deploy --name welcome_agent

