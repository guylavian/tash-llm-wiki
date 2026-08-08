---
title: "Primary Domain Controller as NTP server with no connection to external WAN"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2730191/primary-domain-controller-as-ntp-server-with-no-co
question_id: 2730191
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Primary Domain Controller as NTP server with no connection to external WAN

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2730191/primary-domain-controller-as-ntp-server-with-no-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A bit of a unique environment..

Here's the background: Windows Server (GUI) 2012 R2 virtual machine (VMware, not Hyper-V, don't think it matters tho?)

HIGHLY SECURE (No connection whatsoever outside the network) environment that is currently in the
testing phase*..* 

Small environment, so domain controller, DNS and DHCP all in one..

So the issue at hand is, this primary DC needs to also act as the NTP server for the entire environment..

Now, since there is no connection to the outside world, I cannot sync the time with a time server such as time.windows.com or pool.ntp.org so I need to manually configure the time on DC1 and then let all other member computers sync their time with mine so
 we have consistent time throughout the network even though it might be off in respect to real-time.

Sounds easy enough, but as my username suggests, I'm a total noob, so how do I do it??

Some Microsoft articles (like this one: https://support.microsoft.com/en-us/kb/816042 ) suggest that in order to configure the internal clock as the source for our NTP server on the domain controller requires changes to the registry.. I would honestly hope
 that a server as advanced as 2012 R2 should be able to do make something like this happen without needed to get into regedit. 

Also, in the article above, will it work if my DC is a VM or is it only regarding physical machines?

And once I accomplish this task, the question of domain member computers comes to mind... the following thoughts come to mind:

-  Will I need to go into every single member computer and manually point it to my DC to tell it that its also the NTP?

-  What about new servers that I join to the domain?

-  Is there perhaps a GPO I can create in order to do this for me? And if so, how? (GPO Noob too =P )

Thank you so much for helping out a young windows apprentice be able to perform him job and not get fired! =)

Regards,

knowNoob

## Answers

_No answers on this thread._
