---
title: "Exchange Server 2019 with Edge - Insufficient Resources"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374297/exchange-server-2019-with-edge-insufficient-resour
question_id: 1374297
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange Server 2019 with Edge - Insufficient Resources

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374297/exchange-server-2019-with-edge-insufficient-resour (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all so I'm trying to find a root cause and better understand what happened.

Herse the environment: 

3 Exchange 2013 Server internal

2 Edge 2013 servers in DMZ

Internal applications sending emails to the Exchange 2013 servers then to the Edge servers

Added 2 new Exchange 2019 servers - mailbox/cas servers

What was experienced:

-  After installing the 2019 Servers we observed the mail queue piling up on the Edge servers, with error 452 4.3.1 Insufficient system resources.

-  We also observed the C drive space on one of the 2013 servers was close, upon which we shrunk the logs and cleared significant space

-  We also observed the drive where the Exchange 2019 was installed was actually near full.

-  Mail flow for this application still did not return to normal until we put the 2019 servers in maintenance then restarted the transport roles on all of the 2013 servers

Another observation:

The server installation path was C:*Programs* Files\Microsoft\Exchange Server\V15... , however after the install we noticed another folder C:*Program* Files\Microsoft\Exchange Server\V15\Tranport\EdgeSync....txt

this is only on the first 2019 server that was installed, and its literally file in there.

Contents of edgesync txt :

#Software: Microsoft Exchange Server  

#Version: 15.0.0.0  

#Log-type: EdgeSync Log  

#Date: 2023-09-21T19:46:16.122Z  

#Fields: date-time,session-id,sequence-number,local-serverfqdn,remote-serverfqdn,remote-port,event,level,data,context,sync-mode,sync-type,dc  

2023-09-21T19:46:16.122Z,f9b638a9492e4bd08de306c6f6560a6e,0,,,0,Service,None,,Service Started.,,,  

2023-09-21T19:53:49.568Z,735c4b2540754a748f92f657d4d87859,0,,,0,Service,None,,Service Started.,,,

So my questions are, 

Upon adding a new server into the environment does the Edge server automatically start using it.

Does the action of putting 2019 into maintenance mode and restarting the transport service on the other servers sound the reason it worked (not sure if i'm missing something)

If the Exchange 2019 servers were the cause, is there any reason why the other servers that didn't have resource issues weren't used to send email

-  Is it safe to say that i only need more resources on the Exchange 2019 servers before i bring them back from maintenance.

-  Is it safe to delete the Edge.txt file, there's nothing else in those folders, all other install files are in Programs Files\

Thanks for any help in advance.

## Answers

_No answers on this thread._
