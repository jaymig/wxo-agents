#!/bin/bash
set -x

# remove agents
orchestrate agents remove -n report_manager -k native

# remove tool
orchestrate tools remove --name status_report
