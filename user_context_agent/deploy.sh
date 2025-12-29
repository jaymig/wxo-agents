#!/bin/bash
set -x

## import tools
orchestrate tools import -k python -f ./tools/user_and_email.py -r ./tools/requirements.txt

## Import Welcome agent
orchestrate agents import -f ./agents/welcome_agent.yaml

## Publish agent to live environment
orchestrate agents deploy --name welcome_agent

