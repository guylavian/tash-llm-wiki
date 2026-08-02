---
title: "MS Exchange 2019 - Out Of Office reply doesn't work for external email sender"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1274688/ms-exchange-2019-out-of-office-reply-doesnt-work-f
question_id: 1274688
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# MS Exchange 2019 - Out Of Office reply doesn't work for external email sender

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1274688/ms-exchange-2019-out-of-office-reply-doesnt-work-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I have three host running MS Exchange 2019 CU12.  

We are facing the following issue concerning Out-Of-Office auto reply message:  

MS Exchange doesn't generate OOF automatic replay for messages that come from outside organization.  

OOF seems to work with internal email.

In my case we have just one "Remote Domain". I checked online and I understood default configuration value is "False" for AutoReplyEnabled and AutoForwardEnable if you have MS Exchange on-premise.

```
[PS] C:\Windows\system32>Get-RemoteDomain | fl DomainName,AllowedOOFType,AutoReplyEnabled,AutoForwardEnabled
DomainName       : *
AllowedOOFType   : External
AutoReplyEnabled : False
AutoForwardEnabled: False
```

Moreover I tried to send many times email from external e-mail (for example @outlook.com) to this MS Exchange deployment. Only one time I got OOF, however I sent more or less ten mails to the same mailbox.  

Some suggestion for me?

Thanks in advance!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-29*

Hello  

I applied configuration suggested

```
Set-RemoteDomain Default -AutoReplyEnabled $true -AutoForwardEnabled $true
```

Unfortunately the issue persist.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-02*

Hello @Jarvis Sun-MSFT  

According to this official documentation

This KB is about Microsoft Exchange Online. In my case I am running Exchange 2019 CU12.  

Is still valid this knowledge base for my scenario?

It mentions that if automatic replies are enabled, only one reply is sent to each sender even if a recipient receives multiple messages from a sender.

I got OOF aut-reply only after that I sent different mail just for a mailbox.  

I recreated the same scenario with a new mailbox on the same exchange server.  

I did not get any auto-reply despite of I configured OOF.

Thanks a lot for your help!
