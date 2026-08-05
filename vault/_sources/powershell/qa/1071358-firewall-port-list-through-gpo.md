---
title: "Firewall Port list through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1071358/firewall-port-list-through-gpo
question_id: 1071358
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Firewall Port list through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1071358/firewall-port-list-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

I have a query which returns all enable inbound ports. I would like to make a filter to the current script to check for open ports for certain ports- Some are in ranged port (49152-65535) and some of them are not...     

Some questions I have:    

-  How do I make it possible to run on a remote Win10 client inside the Lan (I would like to choose an IP and then it will scan it)    

-  Does this command runs on the GPO FW rules or not?     

-  I want to be able to question a Linux machine with the same script. Can it be accomplished?    

-  How do I show the output on AsBuiltReport framework?    

This is the query:    

Get-NetFirewallRule -Action Allow -Enabled True -Direction Inbound |    

Format-Table -Property Name,    

DisplayName,    

DisplayGroup,    

@{Name='Protocol';Expression={($PSItem | Get-NetFirewallPortFilter).Protocol}},    

@{Name='LocalPort';Expression={($PSItem | Get-NetFirewallPortFilter).LocalPort}},    

@{Name='RemotePort';Expression={($PSItem | Get-NetFirewallPortFilter).RemotePort}},    

@{Name='RemoteAddress';Expression={($PSItem | Get-NetFirewallAddressFilter).RemoteAddress}},    

Profile    

Thank you in advance.

## Answers

_No answers on this thread._
