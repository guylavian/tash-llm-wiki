---
title: "Exchange 2019 on-prem ediscovery constantly prompts for credentials.  Never completes."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2259853/exchange-2019-on-prem-ediscovery-constantly-prompt
question_id: 2259853
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 on-prem ediscovery constantly prompts for credentials.  Never completes.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2259853/exchange-2019-on-prem-ediscovery-constantly-prompt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After creating several ediscovery files for a subpoena, I am unable to export any of them.  I have the latest CU for 2019 installed.  This process has worked fine in the past.  When trying to export I get a constant prompt for credentials.  The process won't complete.  I have verified the user in question has the organizational management authority and searched the web for hours looking for a solution.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-29*

The issue was caused by the latest CU.  Disabling the additional security in the EWS website allowed it to work.  It wasn't real consistent on the larger exports but the system will allow you to restart so I was able to complete the process.

Turned off extended protection for EWS virtual directory.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-22*

Hi David Webb,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, here are some suggestions for you:

-  Please try to login EAC via browser private mode, then try to export result to .pst again.

-  If it’s available, please try to export with other browsers.

-  Do you enable MFA for your account?

Please understand that we can't use the PST export tool with accounts that require multi-factor authentication (MFA).

You can try with other administration account that is a member of Discovery Management role group.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
