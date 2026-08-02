---
title: "MS Exchange 2013 autodiscovery mode with MS Exchannge 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1294019/ms-exchange-2013-autodiscovery-mode-with-ms-exchan
question_id: 1294019
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# MS Exchange 2013 autodiscovery mode with MS Exchannge 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1294019/ms-exchange-2013-autodiscovery-mode-with-ms-exchan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

I have MS Exchange servers where users are only able to access mailbox via outlook on web. We want to enable auto-discovery between our Exchange 2013 with the newly set up Exchange 2016 to co-exist while we are working on the migration of the mailbox. 

Can we know what are the ports or protocol required to open if there is firewall between the Exchange 2013 and Exchange 2016?  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-31*

Hi @J L

exchange do not support restricting or altering network traffic between internal Exchange servers, between internal Exchange servers and internal Lync or Skype for Business servers, or between internal Exchange servers and internal Active Directory domain controllers in any and all types of topologies. If you have firewalls or network devices that could potentially restrict or alter this kind of internal network traffic, you need to configure rules that allow free and unrestricted communication between these servers: rules that allow incoming and outgoing network traffic on any port (including random RPC ports) and any protocol that never alter bits on the wire.

For more details please check the link below

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/network-ports?view=exchserver-2016,

https://learn.microsoft.com/en-us/exchange/architecture/client-access/autodiscover?view=exchserver-2016

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.
