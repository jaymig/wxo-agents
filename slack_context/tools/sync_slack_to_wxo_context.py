import logging
from typing import Any

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.agent_builder.tools.types import (
    PythonToolKind,
    PluginContext,
    AgentPreInvokePayload,
    AgentPreInvokeResult
)

# Configure logging
logger = logging.getLogger(__name__)

@tool(
    kind=PythonToolKind.AGENTPREINVOKE,
    description="Syncs Slack user context to WXO context variables"
)
def sync_slack_to_wxo_context(
    plugin_context: PluginContext,
    agent_pre_invoke_payload: AgentPreInvokePayload
) -> AgentPreInvokeResult:
    """
    Syncs Slack user context to WXO context variables.
    
    This pre-invoke plugin checks if user_real_name and user_email are set in the Slack context,
    and if so, updates wxo_user_name and wxo_email_id with those values in the context state.
    
    Args:
        plugin_context: The plugin context containing user information and state
        agent_pre_invoke_payload: The agent invocation payload
    
    Returns:
        AgentPreInvokeResult: Result indicating whether to continue processing
    """
    logger.info("=== sync_slack_to_wxo_context: Starting ===")
    
    # Access the context from plugin_context.state
    user_context: dict[str, Any] | None = plugin_context.state.get("context")
    logger.info(f"user_context retrieved: {user_context is not None}")
    
    if user_context is None:
        logger.warning("No user_context available, continuing without changes")
        # No context available, continue without changes
        result = AgentPreInvokeResult(
            modified_payload=agent_pre_invoke_payload,
            continue_processing=True
        )
        return result
    
    # Log current WXO context values before sync
    current_wxo_user_name = user_context.get('wxo_user_name', 'Not set')
    current_wxo_email_id = user_context.get('wxo_email_id', 'Not set')
    logger.info(f"Current WXO context - wxo_user_name: {current_wxo_user_name}, wxo_email_id: {current_wxo_email_id}")
    
    # Read Slack context variables with safe null checks
    channel_data = user_context.get('channel')
    logger.info(f"channel_data retrieved: {channel_data is not None}")
    
    user_real_name = ''
    user_email = ''
    
    if channel_data and isinstance(channel_data, dict):
        slack_data = channel_data.get('slack')
        logger.info(f"slack_data retrieved: {slack_data is not None}")
        
        if slack_data and isinstance(slack_data, dict):
            user_real_name = slack_data.get('user_real_name', '')
            user_email = slack_data.get('user_email', '')
            logger.info(f"Slack context - user_real_name: '{user_real_name}', user_email: '{user_email}'")
    else:
        logger.warning("No channel_data or invalid format")
    
    # Update WXO context if Slack values are available
    if user_real_name or user_email:
        logger.info("Updating WXO context with Slack values")
        
        if user_real_name:
            user_context['wxo_user_name'] = user_real_name
            logger.info(f"Set wxo_user_name to: '{user_real_name}'")
        
        if user_email:
            user_context['wxo_email_id'] = user_email
            logger.info(f"Set wxo_email_id to: '{user_email}'")
        
        # Update the state with modified context
        plugin_context.state["context"] = user_context
        logger.info("Updated plugin_context.state with modified context")
    else:
        logger.info("No Slack values to sync (both user_real_name and user_email are empty)")
    
    # Return the payload unchanged and continue processing
    result = AgentPreInvokeResult(
        modified_payload=agent_pre_invoke_payload,
        continue_processing=True
    )
    logger.info("=== sync_slack_to_wxo_context: Completed ===")
    return result

# Made with Bob
