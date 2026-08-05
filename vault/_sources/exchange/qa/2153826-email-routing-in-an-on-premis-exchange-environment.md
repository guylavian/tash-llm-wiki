---
title: "Email routing in an on-premis Exchange environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2153826/email-routing-in-an-on-premis-exchange-environment
question_id: 2153826
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Email routing in an on-premis Exchange environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2153826/email-routing-in-an-on-premis-exchange-environment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey Experts,

I'm really confused because of an issue that I newly realised in my Exchange environment. It is wierd and I can not find any reason for it.

I have upgraded the Exchange environment from 2013 to 2019 and all mechanism works fine. We have a load balancer and are using it in transparency mode. But, what is the isse?

I realised since some month ago, that one of servers plays no role in mail transport, it seems. When I check transport logs, I see that all emails are sending and receiving by MBX2 and MBX1 just works with MBX2 and deliverd all sending emails there to send, and receivs all emails from it.

I see in Transort logs, that by MBX1 the emails stay always in Submit event and STOREDRIVER as source. I don't see any Source as SMTP and when I send an email from a mailbox on MBX1 to another on the same server(MBX1), I see that this email finally sent by MBX2 and on the MBX1 still Submit as event and STOREDRIVER as source.

I can not find any error or failed process on MBX1. Just confused, if it is really an issue? Or this is an automatic decission from transport service?

I appreciate any tipp or help to figure out, what the issue is.

Best,

Hassan

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-20*

Hi @Anonymous  ,

I found finally the issue and solved it. For me this is very complicated to understand but finally solved.

The problem was Permissions for the Network Services on the parent folder of log path for messagetrackinglog. As I changed this path to a log partition, I have set all permissions for child items in the parent folder and also for parent. We have done some changes on the log partition about ReFS and NTFS topic and somehow the thing is happened. The permission for Network Services is just for Parent folder missed and just on MBX1. 

2nd wierd thing is, all permissions on all services are correctly set on both servers and in this path the logs about STOREDRIVER can be written. Just SMTP loge which I don't know they caome from which component could not be written. It was the reason that I didn't check the permissions never. If it has permission, it should write, if not how a component can write some logs?!?!?

But at the end the problem solved and I want thank you for your help. I apprciate it.

Best,

Hassan

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-04*

Hi @HassanShakeri-1231,

Welcome to the Microsoft Q&A platform!

Based on your description, you are experiencing a complex issue in your Exchange 2019 environment. Here are some steps and considerations that may help you diagnose and resolve the issue:

-  Make sure that the transport service on MBX1 is configured correctly and is running. You can use the Exchange Management Shell to verify the service status and configuration.

-  Since you mentioned that emails on MBX1 are stuck in submission events with STOREDRIVER as the source, this indicates that the Mailbox Transport Submission Service may not be handing the mail to the Transport Service. Check the transport logs for any errors or warnings that may provide more insight.

-  Verify that your load balancer is configured correctly to distribute traffic between MBX1 and MBX2. Sometimes, misconfiguration may cause one server to handle all traffic.

-  Make sure that there are no mail flow rules or transport rules that may affect the routing of emails. These rules sometimes cause unexpected behavior in mail flow.

-  Run the Exchange Health Checker script to identify any potential issues in your Exchange environment. This script can help you pinpoint configuration issues or service issues.

-  Check the Windows Event Log on MBX1 for any errors related to the Transport service. Look for events that might indicate why the service is not processing email as expected.

-  Sometimes, transient issues can be resolved simply by restarting the Transport service on MBX1. You can do this through the Services console or by using PowerShell.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
