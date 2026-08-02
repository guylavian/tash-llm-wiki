---
title: "Remove Messageclass from exchange server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/349592/remove-messageclass-from-exchange-server-2016
question_id: 349592
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Remove Messageclass from exchange server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/349592/remove-messageclass-from-exchange-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys  

    I think through this link: https://eightwone.com/2013/05/16/removing-messages-by-message-class-from-mailbox/, to remove exchange 2016 inside for the IPM. Note. EnterpriseVault. Shortcut ", but the script in my exchange 2016 cannot run, how should I modify the script, thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-09*

Because its a script from an untrusted source (which is basically anything that you didn't create yourself) you will need to probably unblock it (right click the script see https://social.technet.microsoft.com/wiki/contents/articles/38496.unblock-downloaded-powershell-scripts.aspx ) and potential change your execution policy https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy.    

Its important when you post something to always include the actual error (drop in a screen shot if that is easier) that assists anybody trying to help
