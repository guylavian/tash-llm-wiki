---
title: "Not Deployed Printer GPO when i remove everyone"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198698/not-deployed-printer-gpo-when-i-remove-everyone
question_id: 2198698
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-print-fax-scan"]
---
# Not Deployed Printer GPO when i remove everyone

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198698/not-deployed-printer-gpo-when-i-remove-everyone (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am reaching out to address an issue we have encountered regarding the deployment of printers via Group Policy Objects (GPOs) based on departmental groups.

As per our company's setup, we have a total of 18 printers, each designated for specific departments. To streamline printer access, I have created multiple groups corresponding to each printer, ensuring that users only have access to the printers relevant to their department.

However, during the deployment process using GPOs, we have encountered an issue. When I add the respective departmental group to the printer's security settings, the printer is not deployed to the users within that group. Interestingly, when I enable access for "Everyone," the printer is automatically deployed. However, this is not an ideal solution as it compromises security by granting unnecessary access.

I have attached screenshots illustrating the configuration settings for your reference.

Could you please assist me in resolving this issue? I am keen to ensure that our printer deployment aligns with our departmental access permissions without compromising security.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-13*

Any updates about this?   

I am having the exact same problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-30*

Hello,

Based on the information you've provided and the screenshot, it seems you have correctly assigned the department group to the printer with the appropriate permissions. Also, it is necessary to check the Group Policy configuration itself.

Here are some more focused steps to troubleshoot the issue:

-  Check the GPO you're using to deploy the printers is correctly set up. For printer deployment via GPO, you should use the "Deployed Printers" settings found under Computer Configuration > Policies > Windows Settings > Printer Connections.

-  Ensure that the GPO is linked to the correct Organizational Unit (OU) that contains the users or computers needing the printer access. If you're targeting computers, it should be linked to the OU containing the computer accounts. You can create a new GPO with printer deployment settings for one department and then link it to an OU with a test user or computer account that is a member of the corresponding department group. This will help you determine if the issue is with the specific GPO or the overall setup.

-  Ensure that the Active Directory replication is working correctly if you have a multi-domain controller environment so that group memberships and GPO changes are consistently updated across the network.

-  Beside, click the "Advanced" button on the printer's security tab to ensure the departmental group has the necessary permissions there as well.

Remember to force a Group Policy update using `gpupdate /force` after making changes, and check the Application Event Log on the client machines for any related warnings or errors.

I hope this helps.

Best regards

Please find the attached screenshot , its already correct OU and GPO, so i don't know the issue, if you can check remotely its better

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-29*

Hello,

Based on the information you've provided and the screenshot, it seems you have correctly assigned the department group to the printer with the appropriate permissions. Also, it is necessary to check the Group Policy configuration itself. 

Here are some more focused steps to troubleshoot the issue: 

-  Check the GPO you're using to deploy the printers is correctly set up. For printer deployment via GPO, you should use the "Deployed Printers" settings found under  Computer Configuration > Policies > Windows Settings > Printer Connections.

-  Ensure that the GPO is linked to the correct Organizational Unit (OU) that contains the users or computers needing the printer access. If you're targeting computers, it should be linked to the OU containing the computer accounts. You can create a new GPO with printer deployment settings for one department and then link it to an OU with a test user or computer account that is a member of the corresponding department group. This will help you determine if the issue is with the specific GPO or the overall setup. 

-  Ensure that the Active Directory replication is working correctly if you have a multi-domain controller environment so that group memberships and GPO changes are consistently updated across the network. 

-  Beside, click the "Advanced" button on the printer's security tab to ensure the departmental group has the necessary permissions there as well. 

Remember to force a Group Policy update using `gpupdate /force` after making changes, and check the Application Event Log on the client machines for any related warnings or errors.  

I hope this helps. 

Best regards
