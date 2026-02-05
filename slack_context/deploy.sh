#!/bin/bash
set -x

## import tools
orchestrate tools import -k python -f ./tools/slack_context.py

## Import slack agent
orchestrate agents import -f ./agents/slack_agent.yaml

## deploy agent
orchestrate agents deploy --name slack_agent

## deploy channel
orchestrate channels import --agent-name slack_agent --env live  --file channels/slack_channel.yaml

