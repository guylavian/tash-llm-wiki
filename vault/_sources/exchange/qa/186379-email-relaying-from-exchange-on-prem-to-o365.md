---
title: "Email Relaying from Exchange On-Prem. to O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/186379/email-relaying-from-exchange-on-prem-to-o365
question_id: 186379
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Email Relaying from Exchange On-Prem. to O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/186379/email-relaying-from-exchange-on-prem-to-o365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have a question regarding email relaying in Hybrid Configuration Setup as mentioned below,  

Current Setup:  

Exchange 2016   

Exchange Online   

External Email Gateway (Forcepoint Cloud Security - MX Record holder)  

HCW is setup with Centralized Transport Enable.  

External Email lands on FP and forwarded to Exchange on-Prem. and redirected to Exchange Online if mailbox is not available on-Prem.   

New Requirement:  

We want Forcepoint to Send Email to Exchange Online and from EOL to On-Prem.  

Forcepoint <>EOL <> Exchange2016  

As per my understanding following is the plan I have scoped.  

Forcpoint: Fairly Simple  

Connector to Send Emails to EOL  

Connctor to Receive Emails from EOL  

Exchange 2016:  

Disable Send Connector (External Emails to Forcepoint)  

Modify Send Connector (Emails to EOL)  

change Address space from @mydomain.onmicrosoft.com to *  

Exchange Online: (O365)  

New: Email Receive connector from Forcepoint IPs to Exchange Online  

New: Email Send Connector Send * from Exchange Online to Forcepoint via FP Smart Host  

Modify Email Send Connector From EOL to On-Prem. Exchangechange address space from * to @mydomain.com & change -RouteAllMessagesViaOnPremises from True to False  

This is high level plan. My only concern is if email from Internet to EOL, Mailbox not available on EOL, should it automatically check for send connector created from EOL to On-Prem or would I need to change Authoritative Status of my accepted domain setting?  

Any other advise would also be appreciated.  

Thank you & regards,

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-07*

@Rana Junaid Abrar AHMAD       

In general, HCW will help to configure the connector for the mail flow between on-premises and Exchange Online. You can re-run HCW and don't enable centralized mail transport. Then check connectors settings between on-premises and Exchange Online. Here are more information for Manage mail flow using a third-party cloud service with Exchange Online and on-premises mailboxes.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
