---
title: "Not Deployed Printer GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198807/not-deployed-printer-gpo
question_id: 2198807
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Not Deployed Printer GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198807/not-deployed-printer-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear,

I need to make our company printer access only authorized department peoples so what i did in the printer properties security i removed everyone then i added the department group this group have permission to print, so when i did like this the printer did not deploy the user automatically via GPO, when i enable everyone its automatic deployed, see some screenshots so need solution for this, and all the user added in the group, the issue not one printer we have total 18 printer, i think the configuration isssue , also i can add manually the printer , but not work automatically if not have permission everyone, i don't want everyone

check the screenshot = New folder

## Answer (community) — community member

*upvotes: 1 · updated: 2024-04-29*

Hello,

Based on the information you've provided and the screenshot, it seems you have correctly assigned the department group to the printer with the appropriate permissions. Also, it is necessary to check the Group Policy configuration itself.

Here are some more focused steps to troubleshoot the issue:

-  Check the group policy you're using to deploy the printers is correctly set up. Open the Group Policy Management Console (GPMC) and navigate to Computer Configuration > Policies > Administrative Templates > Printers. Check the "Deployed Printers" settings.

-  Ensure that the GPO is linked to the correct Organizational Unit (OU) that contains the users or computers needing the printer access. If you're targeting computers, it should be linked to the OU containing the computer accounts. You can create a new GPO with printer deployment settings for one department and then link it to an OU with a test user or computer account that is a member of the corresponding department group. This will help you determine if the issue is with the specific GPO or the overall setup.

-  Ensure that the Active Directory replication is working correctly if you have a multi-domain controller environment so that group memberships and GPO changes are consistently updated across the network.

-  Beside, click the "Advanced" button on the printer's security tab to ensure the departmental group has the necessary permissions there as well.

Remember to force a Group Policy update using `gpupdate /force` after making changes, and check the Application Event Log on the client machines for any related warnings or errors.

I hope this helps.

Best regards
