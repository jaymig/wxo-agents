#!/bin/bash
set -x

# remove agents
orchestrate agents remove -n welcome_agent -k native

# remove tool
orchestrate tools remove --name session_context
orchestrate tools remove --name user_info
orchestrate tools remove --name update_user_context
orchestrate tools remove --name update_user_profile
orchestrate tools remove --name read_user_profile
