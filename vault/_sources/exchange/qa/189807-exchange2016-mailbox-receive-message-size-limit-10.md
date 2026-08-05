---
title: "exchange2016 mailbox receive message size limit 100MB and organization transport setting of max receive message size 30MB, how to allow user receiving 50MB Message"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/189807/exchange2016-mailbox-receive-message-size-limit-10
question_id: 189807
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
---
# exchange2016 mailbox receive message size limit 100MB and organization transport setting of max receive message size 30MB, how to allow user receiving 50MB Message

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/189807/exchange2016-mailbox-receive-message-size-limit-10 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi experts,   

organization transport setting of max receive message size limits has been 30MB since exchange 2016 installation,   

2 days ago, exchange 2016 mailbox receive message size limit of a user was increased from blank-setting to 100MB,   

but now the user still can't receive message with size of 33MB.   

is it true that user mailbox size limit takes precedence over all other  max receive message size limits?  

if so, why he user still can't receive message of 33MB that is smaller than user's mailbox limit 100MB?  

what other limits or restart exchange services need to do ?   

how to allow a special user receive messages larger than the org standard/default limits?  

Any suggestion would be greatly appreciated.  

Thanks for your time  

pingatwork

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-12-08*

Reason is the "organization transport setting of max receive message size limits has been 30MB"    

Increase this value more than 33MB.    

you can refer following for further details of message size limitation,    

https://learn.microsoft.com/en-us/exchange/mail-flow/message-size-limits?view=exchserver-2019
