---
title: "exchange health monitoring mailbox messages non stop"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/333825/exchange-health-monitoring-mailbox-messages-non-st
question_id: 333825
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange health monitoring mailbox messages non stop

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/333825/exchange-health-monitoring-mailbox-messages-non-st (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

after upgrading exchange 2013  to latest CU we are getting a large number of Undeliverable inbound proxy probe emails coming from the postmaster@keyman  .com going to the healthmailbox and getting  "delivery has failed to these recipients or groups"    

What is this and How can i provide resolution.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-20*

[PS] C:\Users\admin\Desktop> Get-Mailbox -Monitoring | fl forward  

Creating a new session for implicit remoting of "Get-Mailbox" command...  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :  

DeliverToMailboxAndForward : False  

ForwardingAddress          :  

ForwardingSmtpAddress      :

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

it's annoying for 1 specific user who is getting them . they seem to be forwarding to a specific user 's mailbox? Is this possible?  

Where would i verify if/how  this forwarding is taking place..

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

. I followed the steps and they stopped for a short period but they have come back. How can i prevent these permanently??

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-26*

what about just creating the postmaster@keyman  .com mailbox . Would that work as well?    

Which solution is better?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-26*

You can delete them all with powershell:    

Get-Mailbox -Monitoring | Remove-Mailbox    

Make sure you also read this and give the necessary permissions so the AD objects are removed:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/remove-mailboxdatabase-cannot-remove-health-mailboxes    

Otherwise, remove the AD objects manually    

Then restart the Microsoft Exchange Health Manager, MSExchangeHM service on each Exch server to recreate them.    

There is NO danger in doing this. It can be done anytime.
