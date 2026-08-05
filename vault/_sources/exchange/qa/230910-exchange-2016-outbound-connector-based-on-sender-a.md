---
title: "Exchange 2016 Outbound Connector based on sender address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/230910/exchange-2016-outbound-connector-based-on-sender-a
question_id: 230910
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Outbound Connector based on sender address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/230910/exchange-2016-outbound-connector-based-on-sender-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We would like to be able to send outbound email to a specific outbound connector based on the internal sender address.  

Essentially, we have large quantities (for us) of email that we send to customers - order confirmations, shipping notifications, etc.  All email is currently routed out through a connector to a cloud based email filtering/scanning service.  The order confirmations and shipping notifications are causing a backlog.  We would like to route those emails directly to the internet but keep the remainder of out outbound email routing through the cloud service.  

We know we can setup a sub domain and route that way but we would also have to setup MX records, DKIM, etc as well as change the return email addresses, etc.  We would prefer to not have to restructure our email setup top to bottom for this.  

In Exchange 2016, is there a way to route outbound email from a specific sender address to a different, non-default outbound connector without affecting the remainder of our outbound email?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-15*

@John Coxen       

Hi,    

The send connectors on Exchange on-premises are based only on the Recipients' domains.    

    

So it is not possible to do it without some third-party agents.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-14*

Not natively.     

Options:    

Route outbound through Office 365 / EOP    

https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/conditional-mail-routing    

3rd party on-prem software:    

https://www.ivasoft.com/routebysender2013.shtml
