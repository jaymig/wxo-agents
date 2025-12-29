#!/bin/bash
set -x

## import tools
orchestrate tools import -k python -f ./tools/status_report.py -r ./tools/requirements.txt

## Import Welcome agent
orchestrate agents import -f ./agents/report_manager.yaml

## Publish agent to live environment
orchestrate agents deploy --name report_manager

