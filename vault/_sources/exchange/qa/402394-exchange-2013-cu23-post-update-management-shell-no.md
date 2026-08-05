---
title: "Exchange 2013 CU23 post update - Management Shell not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/402394/exchange-2013-cu23-post-update-management-shell-no
question_id: 402394
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 CU23 post update - Management Shell not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/402394/exchange-2013-cu23-post-update-management-shell-no (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,    

We recently upgraded our Exchange 2013 on-prem server to CU23 and everything seemed to work perfectly afterwards. I noticed that some shared mailboxes started giving issues of continuously prompting for passwords or just being entirely blank although there definitely is emails in the mailbox.    

For troubleshooting I opened up Exchange Management Shell and was presented with a whole lot of error messages which seems to just be repeating. I will be completely honest and say that I am not well versed in management of Exchange so I don't know what to do at the moment. Could anyone assist please? I hope this is something stupid that I am just missing.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-23*

Hi @Leunis van Rooyen       

Try the below,    

-  Open Windows powershell as administrator    

-  Navigate to Exchange scripts - cd $Exscripts    

-  Run .\UpdateCas.ps1 and .\UpdateConfigFiles.ps1 scripts one after another    

-  Run IISReset.     

If the above suggestions helps, please click on "Accept answer" and upvote it.
