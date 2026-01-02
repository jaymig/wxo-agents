#!/bin/bash
set -x

## import tools
orchestrate tools import -k openapi -f ./tools/hello-world-tool.json

## Import collaborator agent
orchestrate agents import -f ./agents/hello-agent.json

## Publish agent to live environment
orchestrate agents deploy --name hello_agent

