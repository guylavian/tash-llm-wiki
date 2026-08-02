---
title: "Is Azure Subscription required to manage Exchange 365? and is it included with Business Standard?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118212/is-azure-subscription-required-to-manage-exchange
question_id: 2118212
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-hybrid-management", "office-exchange-online"]
---
# Is Azure Subscription required to manage Exchange 365? and is it included with Business Standard?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118212/is-azure-subscription-required-to-manage-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is an Azure subscription required to run Powershell commands on Exchange 365?

I am attempting to setup a Hybrid Exchange between 2013 On Premise and 365 and not having much luck.  

When trying to follow Microsoft’s instructions for testing the OAuthConnectivity between cloud & On-premise, it tells me the following: To verify that your Exchange Online organization can successfully connect to your on-premises Exchange organization, connect to Exchange Online PowerShell and run the following command:

Test-OAuthConnectivity -Service EWS -TargetUri <external hostname authority of your Exchange On-Premises deployment>/metadata/json/1 -Mailbox <Exchange Online Mailbox> -Verbose | Format-List

 But if I attempt to open an online powershell I get this:

When attempting to run the command, I get an error showing “No Valid Subscription for Azure”  

So am I going to have to pay to create an Azure subscription, or is it included with 365?  Apparently I cannot run the commands to test without it.  I really don’t see how we can run an Exchange server without it.    

Some people tell me I do not need Azure, but How do I access the online Exchange server without Azure?     

I'm a complete newbe to cloud stuff.

## Answers

_No answers on this thread._
