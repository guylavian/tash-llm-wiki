---
title: "Exchange 2016 Lab Setup. want to deploy DAG member in azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2752997/exchange-2016-lab-setup-want-to-deploy-dag-member
question_id: 2752997
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Exchange 2016 Lab Setup. want to deploy DAG member in azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2752997/exchange-2016-lab-setup-want-to-deploy-dag-member (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 4 Virtual servers in my lab (note i have not been working with Exchange very long so play easy with me)

-  DC

-  FS

-  EX01

-  EX02

the situation is DNS and AD Server.

the File Server  in the member server that has the CNO

EX01 is the main 2016 "Mailbox server" 

EX02 is also a 2016 "Mailbox server"

-  DAG deployed called = DAG1, DAG1 has two members - EX01-EX02. both are working as expected and i have no issues to report about either of them.

I want to deploy a DC, EX03 and Alternate Witness server in the event of my "LAB" losing internet connectivity the passive node in azure, EX03 will become the active node and stay in place until i manually revert when the disaster has been resolved.

Azure Setup has 3 VMs

-  DC setup as a RODC joined to my LAN domain called "domain1" (working)

-  Filewitness (working)

-  EX03 (working)

I am unsure as to how i can achieve this setup. can I am also unsure of the context of the question I am asking.......

looking for site resilient DR for exchange 2016 using Azure RM

Thanks

Shane

## Answer (community) — community member

*upvotes: 0 · updated: 2017-12-26*

Hi,

Your question is outside the scope of this Community.

MSDN Azure Forums:

https://social.msdn.microsoft.com/forums/azure/en-US/home?category=windowsazureplatform

TechNet Azure Forums:

https://social.technet.microsoft.com/forums/azure/en-US/home?category=windowsazureplatform

TechNet Exchange Forums.

https://social.technet.microsoft.com/Forums/exchange/en-us/home?category=exchangeserver

And/or here:

https://social.technet.microsoft.com/Forums/exchange/en-US/home?forum=exchangesvrgeneral

TechNet Server Forums. 

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

Or MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
