#!/bin/bash
set -x

## Un deploy channel
orchestrate channels delete --agent-name slack_agent --env live  --type byo_slack --name slack_demo_channel

## Un deploy agent
orchestrate agents undeploy --name slack_agent

## remove agents
orchestrate agents remove -n slack_agent -k native

## remove tool
orchestrate tools remove --name slack_context


