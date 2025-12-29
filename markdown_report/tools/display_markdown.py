from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def display_markdown():
    """
    This is a demonstration tool to show how to display images
    :returns: An image:
    """
    markdown = '''
        # Initiative Report

        ## Initiative Name
        **Allegorithmic (Substance) Zendesk - Archive and Decommission**

        - **Jira Key:** ACQ-1041  
        - **Status:** SLC  
        - **Status Release Quarter:** PPC Approved 2024 Q4  
        - **Headline:** Archive/decomm of Allego Zendesk  
        - **Program Manager:** Alejandra Cordova  
        - **Status Date:** Sep 26, 2024  

        ## Reporting Summary
        - Requirements document shared with business and received business sign-off on July 19th.
        - Extraction and loading of a sample data of the tickets created during June 2024 is completed and shared with CSMs for initial verification - **Completed**.
        - Contract end date: **Nov 21st, 2024**.

        ## Goals for Next Period
        - Pending work on Zendesk until a solution is found for the crash/report.

        ## Key Risks
        _(Not specified)_

        ## Past Due or Upcoming Milestones (Next 30 Days)

        | Milestone                         | Planned Date | Actual Date | Status |
        |----------------------------------|--------------|-------------|--------|
        | Allego: Complete archive of Zendesk | Oct 31, 2023 | 10/31/23    | New    |
        | Allego: Decommission Zendesk       | Nov 30, 2023 | 11/30/23    | New    |

     ''' 


    return markdown
