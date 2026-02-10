#!/bin/bash
set -x

## import tools
orchestrate tools import -k python -f ./tools/slack_context.py
orchestrate tools import -k python -f ./tools/update_user_context.py
orchestrate tools import -k python -f ./tools/sync_slack_to_wxo_context.py

## Import slack agent
orchestrate agents import -f ./agents/slack_agent.yaml

## deploy agent
orchestrate agents deploy --name slack_agent

## deploy channel
## note that slack_channel.yaml is a placeholder, and actual values are in .slack_channel.yaml
 orchestrate channels import --agent-name slack_agent --env live  --file channels/.slack_channel.yaml

