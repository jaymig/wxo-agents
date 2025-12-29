#!/bin/bash
set -x

# remove agents
orchestrate agents remove -n hello_agent -k native

# remove tool
orchestrate tools remove --name hello_world_tool


