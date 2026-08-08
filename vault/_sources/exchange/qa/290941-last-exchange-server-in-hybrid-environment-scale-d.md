---
title: "Last Exchange Server in Hybrid Environment - Scale Down Resources"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/290941/last-exchange-server-in-hybrid-environment-scale-d
question_id: 290941
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Last Exchange Server in Hybrid Environment - Scale Down Resources

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/290941/last-exchange-server-in-hybrid-environment-scale-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need advice to reduce CPU load and disk utilization on minimal last Exchange 2016 server in Hybrid Environment.  

Our migration is complete. No onprem mailboxes and no mailflow from onprem so no local SMTP or Store required.  

No more migrations required.  

We have Azure AD Connect so our onprem AD is the master.  

Went through all the steps to decommission our last Exchange 2010 server last year.  

Now have a minimal Exchange 2016 server running on Server 2016 as a VM 8Gb ram 2 vCpu  

The sole purpose of this server is for recipient management. eg. adding new Office365 mailboxes.    

Problem: The Exchange Server 2016 runs continuously at 20-25% CPU when it has nothing to do.  

No mailboxes. No SMTP connectors. No mailbox store.  

We connect to it a couple of times per week to add an O365 mailbox.  

What Exchange services can be safely shutdown so it simply operates as a recipient management tool?  

What system settings are available to tell .Net to use less memory?  

To save resources, currently considering turning it off and only power it up to do an AD recipient update and then shutdown.  

It would be nice if Microsoft would follow through with their promise at Ignite 2017 to create a recipient management tool...............

## Answers

_No answers on this thread._
