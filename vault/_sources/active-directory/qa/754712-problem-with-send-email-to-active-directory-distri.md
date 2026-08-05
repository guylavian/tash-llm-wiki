---
title: "Problem with send email to Active Directory Distribution Group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/754712/problem-with-send-email-to-active-directory-distri
question_id: 754712
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Problem with send email to Active Directory Distribution Group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/754712/problem-with-send-email-to-active-directory-distri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

i have installed Exchange 2019 in my environment. I have problem with send email from my Exchange 2019 mailbox to my distribution group (with 1 member) on my Active Directory environment. On Exchange 2019 LogMessageTracking i see log as on bellow image.    

    

Maybe i have to set some attribute on my Active Directory DG ?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-15*

Hi,    

Mail-enabled distributed group, or mail-enabled security group are necessary to send mail to group.    

Try to use PowerShell cmdlet Enable-DistributionGroup to enable the mail function:    

https://learn.microsoft.com/en-us/powershell/module/exchange/enable-distributiongroup?view=exchange-ps    

Above is suggestion based on my experience. If you have more question about Exchange/Mailbox, we would recommend you to (post a new thread would be recommended) add tag such including key word Exchange, invite exchange professional to this thread/issue discussing.     

Best Regards,    

Eve Wang
