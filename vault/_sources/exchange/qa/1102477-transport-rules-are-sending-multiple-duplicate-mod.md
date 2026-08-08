---
title: "Transport Rules are sending multiple/duplicate moderation emails for approval"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1102477/transport-rules-are-sending-multiple-duplicate-mod
question_id: 1102477
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Transport Rules are sending multiple/duplicate moderation emails for approval

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1102477/transport-rules-are-sending-multiple-duplicate-mod (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a hybrid on premise and 365 cloud configuration consisting of Exchange 2013 CU23 and Exchange 2016 for some shared and system mailboxes that cannot be migrated to 365 and the rest of our user mailboxes (several thousand) are migrated to the cloud. Since 2019, we have been having recurring and intermittent problems on the 2013 DAG where users in one of the teams at our company send external emails out which require moderation approval and once approved, a duplicate or multiple approval requests are sent again by Exchange, even after being approved.     

We have worked on it extensively with Microsoft Support and they have never been able to solve this, and eventually the problem ceases but eventually recurs months later. Since we migrated all of our user mailboxes to the cloud last year, this problem has returned and gotten extensively worse. Multiple email moderation requests for approval are being sent, sometimes 3-5 times for each outbound email. The affected team of moderators has grown increasingly impatient and Microsoft support has shown little interest in getting this fixed and is not devoting much attention here.    

I'm willing to provide as much detail as possible here, but below is a common scenario:    

-  End user sends email to external recipient with one of several qualifying attachments (doc, docx, xlsx, pdf, txt, etc)    

-  If the email contains an attachment such as any of the above extensions and is being sent externally, the rule is invoked and a moderation request is     

 sent to a specified moderator in the rule for approval.    

-  Moderator approves the request and email is sent    

-  Several more moderation requests for approval to send the same email are sent to the moderator; the email has already been sent externally so this does not serve any purpose    

-  Often times, these outbound emails are being sent on behalf of a shared mailbox that resides on premise by a user mailbox which resides in the cloud.    

-  The shared mailboxes reside in a Exchange 2013 DAG with CU23    

-  The user mailboxes are linked mailboxes and were migrated from the Exchange 2013 DAG to M365    

-  The Exchange 2016 DAG is part of a separate domain that has a trust relationship with the domain that the 2013 Exchange DAG belongs to; all email sent from on premise is routed from Exchange 2013 through Exchange 2016 to the internet.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-29*

I've done extensive investigation and research tonight and may have found the issue. When a user sends an email to an external recipient with a qualifying attachment (pdf, docx, etc), the message is submitted to moderators automatically by the transport rules for approval    

-  The system attendant/arbitration mailbox sends the approval request to a moderator for approval, and the message is approved and released for delivery    

-  I noticed when this happens, the message is dropped or blocked and no information is provided in the Explorer portal at security.microsoft.com why     

-  The moderator receives a duplicate approval request immediately after, approves it and the message is released for delivery and the final status is delivered, or the Latest delivery location shows: On-prem/external    

I'm unable to find any reason anywhere why these messages are being dropped/blocked, and its only happening when the duplicate moderation requests arrive. I kept asking myself, "Why isnt anyone noticing that the recipients are receiving their emails, and I noticed right after the dropped or blocked status, the same message shows again as delivered.     

I cant find anything online about this, does this mean anything to you? We had a heated meeting with our support engineer covering the case today; they simply are not able to come up with anything here and the only reason we are this far is because I'm doing all of the work.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-24*

Here are a few steps to troubleshoot the issue:    

Ensure arbitration mailboxes are moved to Exchange 2016.    

Delete and recreate rules.    

Move the moderator's mailbox to Exchange 2016.    

Restart transport services.    

Multiple Moderation Approval Requests: http://byronwright.blogspot.in/2017/06/multiple-moderation-approval-requests.html    

Get the complete details about Client Connectivity in an Exchange: https://blogs.technet.microsoft.com/exchange/2015/10/26/client-connectivity-in-an-exchange-2016-coexistence-environment-with-exchange-2010/
