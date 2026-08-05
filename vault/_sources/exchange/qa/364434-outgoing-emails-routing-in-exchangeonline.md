---
title: "Outgoing emails routing in Exchangeonline"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/364434/outgoing-emails-routing-in-exchangeonline
question_id: 364434
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Outgoing emails routing in Exchangeonline

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/364434/outgoing-emails-routing-in-exchangeonline (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Exchange 2016 Hybrid with all users' mailboxes in Exchange online ( shared mailboxes in on-premises EX 2016 servers), currently configured all outgoing email from Exchange Online coming back to on-premises 3rd party host.   

Now, we would like to configure all outgoing emails from Exchange online using Microsoft EOP, not coming to on-prem 3rd party host.  

How can i configure Outbound connector in Exchange online to use all outgoing emails routed to EOP?  

We tested with couple of domains' outbound emails, configured outbound partner connector and transport rule to use the connector if the recipient domain is specific domain.  

But as we decided to use Exchange online outgoing emails thru Microsoft, I would like to know the best practice to   

Thanks in advance for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-21*

Hi @Tek-Nerd   ,    

Agree with what Andy said. If you create the specific connector, please try to disable it and send a test email.    

In addition, according to the Microsoft's official article we could know that in the Exchange hybrid environment, if there is no specific configuration, all emails sent from Officr 365 mailboxes to the Internet will go through EOP.    

For more information you could refer to: Outbound messages to the Internet    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-20*

OutBound mail to the internet from EOP doesnt need a connector.     

If you have one now that sends all outbound mail to the 3rd party host, disable it and test.    

https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow#when-do-i-need-a-connector
