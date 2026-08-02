---
title: "How to get RelaxMinimumPasswordLengthLimits GPO setting to show on DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1031302/how-to-get-relaxminimumpasswordlengthlimits-gpo-se
question_id: 1031302
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# How to get RelaxMinimumPasswordLengthLimits GPO setting to show on DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1031302/how-to-get-relaxminimumpasswordlengthlimits-gpo-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have all Windows 10 21H1 clients and I have 2 Domain Controllers, 2016 and 2019.  I have downloaded the latest GPO Templates for the 21H1 update and added those to my central store, but I cannot see the setting for "RelaxMinimumPasswordLengthLimits".  I have searched for this and found that it was introduced in Win10 2004 update in 2020, but how to I make that show up in my policies?  Why would that setting not be in the latest GPO templates from Microsoft?    

Thanks,

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-04*

Hi,    

To establish the required configuration via GP, set the following UI path to Enabled:    

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Relax minimum password length limits    

----------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
