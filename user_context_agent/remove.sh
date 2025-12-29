#!/bin/bash
set -x

# remove agents
orchestrate agents remove -n welcome_agent -k native

# remove tool
orchestrate tools remove --name echo_user_info
