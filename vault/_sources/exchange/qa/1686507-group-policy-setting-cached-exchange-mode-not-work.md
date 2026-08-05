---
title: "Group Policy setting Cached Exchange Mode not working."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1686507/group-policy-setting-cached-exchange-mode-not-work
question_id: 1686507
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
---
# Group Policy setting Cached Exchange Mode not working.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1686507/group-policy-setting-cached-exchange-mode-not-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am struggling to set outlook Exchange Cached Mode to 6 Month Group policy.We have Citrix Environment users will connect to Windows 2019 server with RDS license's multiple connections, we have FSlogix configured. User will use Outlook and most of the users Mailbox size is more than 35 GB. so we want to implement Exchange Chace mode for 6 months to reduce the OST file size. we are using 'Microssoft Office LTSC Professional Plus 2021 -en-us'

we applied the policy 

We applied Exchange Cached mode from Group Policy.

We applied the below configuration to 6 months 

from Group Policy Management 'Select Cached Exchange Mode sync settings for profiles' to ALL it is not getting applied on outlook too.

Any help is much appreciated  thank you.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2024-05-28*

Hello

Did you see the settings for the GPO in this article: 

https://learn.microsoft.com/en-us/outlook/troubleshoot/installation/cached-exchange-mode

https://www.stellarinfo.com/blog/plan-and-configure-cached-exchange-mode-in-outlook/

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-05-28*

Hi @Srinivas  ,

I understand that you’re having trouble applying the ‘ALL’ setting for Cached Exchange Mode sync in Outlook via Group Policy Management. Here are a few things you could check:

-  Group Policy Update: After changing the Group Policy, you need to ensure that the policy is updated on the client machines. You can do this by running the `gpupdate /force` command in the command prompt on the client machines.

-  Registry Settings: You can also check the registry settings on the client machines. The Cached Exchange Mode settings are stored in the registry in the `HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\Cached Mode` key.

-  GPMC Display Issue: There is a known issue where the Group Policy Management Console (GPMC) does not differentiate between the ‘One week’, ‘Two weeks’, or ‘All’ options for the Cached Exchange Mode Sync Setting policy, and it always shows ‘Three days’ when you reopen the management console. However, this only affects the way that the setting is displayed in GPMC, and the Cached Exchange Mode Sync Setting policy should work correctly as it’s configured.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
