---
title: "Installed new Exchange 2016 mailbox server into 2010 environment w/2010 Edge.  Test account from 2016 will not send/receive externally."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/137109/installed-new-exchange-2016-mailbox-server-into-20
question_id: 137109
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-excel-business-platform-windows", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Installed new Exchange 2016 mailbox server into 2010 environment w/2010 Edge.  Test account from 2016 will not send/receive externally.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/137109/installed-new-exchange-2016-mailbox-server-into-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently completed an installation of Exchange 2016 mailbox server into an Exchange 2010 environment, which includes one 2010 mailbox server and one 2010 Edge Transport server.      

I created a test account on the 2016 database and tested the send/receive connectivity.  I was able to send internally, but for external mail, it's hangs in the queue.  Error below.    

------------------------------------------------------------------------------    

Diagnostic information for administrators:    

Generating server: Exchange2016.domain.local    

Receiving server: edgesync - default-first-site-name to internet (2xx.xx.xx.xx)    

example@Stuff  .com    

Server at edgesync - default-first-site-name to internet (2xx.xx.xx.xx) returned '400 4.4.7 Message delayed'    

10/21/2020 10:43:36 AM - Server at edgesync - default-first-site-name to internet (2xx.xx.xx.xx) returned '451 4.4.397 Error communicating with target host. -> 421 4.2.1 Unable to connect -> SocketTimedout: Socket error code 10060'    

Original message headers:    

Received: from Exchange2016.domain.local (192.168.xx.xxx) by    

 Exchange2016.domain.local (192.168.xx.xxx) with Microsoft SMTP Server    

 (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id    

 15.1.2106.2; Wed, 21 Oct 2020 02:46:10 -0400    

Received: from Exchange2016.domain.local ([::1]) by    

 Exchange2016.domain.local ([::1]) with mapi id 15.01.2106.002; Wed, 21    

 Oct 2020 02:46:10 -0400

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-27*

Hi,   

just found your articel becuase I came to the same problem.  

I re subscribed and mail flow is working from the new mailboxserver 2016 aswell.  

however wenn I run test-edgesubscription on the old 2010 mailboxserver it states failed.  

when I run test-edgsubscription on the new 2016server it states successfully.   

Is this normal behavior in 2010/2016 mix?

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-10-26*

@Paul Siso       

Agree with AndyDavid. When we add a Mailbox server, the new Mailbox server doesn't automatically participate in EdgeSync synchronization. So we have to resubscribe the Edge Transport server to AD. For your reference: Add or Remove a Mailbox server.    

If you have any questions or need further help on this issue, please feel free to post back.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-10-23*

You have to re-subscribe an Edge Subscription whenever you add or remove Mailbox servers in the AD site.    

https://learn.microsoft.com/en-us/exchange/architecture/edge-transport-servers/edge-subscriptions?view=exchserver-2019    

Also, I would suggest following the docs and bring up an Exchange 2016 Edge and subscribe that    

https://practical365.com/exchange-server/exchange-server-2016-migration-mail-flow-cutover/
