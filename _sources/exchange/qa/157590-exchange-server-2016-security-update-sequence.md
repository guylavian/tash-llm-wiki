---
title: "Exchange Server 2016 security update sequence"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/157590/exchange-server-2016-security-update-sequence
question_id: 157590
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Exchange Server 2016 security update sequence

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/157590/exchange-server-2016-security-update-sequence (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a mail server deployed based on Windows server 2016 Standard.   

Regular updates were installed only on the operating system itself.   

But there are security updates separately for Exchange Server. Will installing the latest update not result in a server crash?  

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-03*

Sorry for a long time didn`t update topic.   

Yes, In the expanded documents for each update, you can find the presence of older versions. So all i just need find the update that cover my previous and update for a latest actual file.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-11*

Hi @40726428,    

Security updates are released only for supported versions of the product. Running unsupported versions puts you at risk due to unpatched security vulnerabilities.    

The official KB here introduces about the security update for Microsoft Exchange Server 2019 and 2016    

To avoid the issue Exchange services or OWA, ECP not working after installing the security update, running the security update at an elevated command prompt    

-  Select Start, and type cmd.    

-  In the results, right-click Command Prompt, and then select Run as administrator.    

-  If the User Account Control dialog box appears, verify that the default action is the action that you want, and then select Continue.    

-  Type the full path of the .msp file, and then press Enter.    

This issue does not occur if you install the update through Microsoft Update which won't result in a server crash.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
