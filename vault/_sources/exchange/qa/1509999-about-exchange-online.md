---
title: "About Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1509999/about-exchange-online
question_id: 1509999
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# About Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1509999/about-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I Received NDR Email in spam folder instead inbox so I am having trouble noticing that I am unable to send emails  

when I try to send email following error occur  

i.e your message was't send because its too large and exceed exchange size limit that is 10 MB  

so can the following setting be possible??  

-  Execute the capacity limit judgment for Exchange mail in the compressed state instead of after decompressing it.   

-  Prevent NDRs from ending up in the Exchange junk folder.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-01-24*

Hi,

Thanks for writing here in Q&A.

Here is my answers to your questions as good as I could :)

-  That is an option on the mailbox etc. To see the config for a mailbox max send size and so, and you can run this commend when you are connected to Exchange Online to see the corrent configuration for a mailbox: `Get-Mailbox -Identity "******@domain.com" | fl maxsendsize,maxreceivesize`   To change it, you can set it up to etc. 150 MB via the command: `Set-Mailbox -Identity "******@domain.com" -MaxReceiveSize 150MB -MaxSendSize 150MB`

-  Hmm, normaly I had not seen this NDR´s in jumk - but it is possibel to write list the sender if it is.

Let me hear if this helps.

Have a nice day.
