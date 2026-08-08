---
title: "Outbound email for perticular domain in Exchange server 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138071/outbound-email-for-perticular-domain-in-exchange-s
question_id: 138071
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Outbound email for perticular domain in Exchange server 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138071/outbound-email-for-perticular-domain-in-exchange-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are facing issue with outbound emails to a particular domain only.

This is because our internal domain name is same as the receivers email domain.

for example : our internal domain is xyz.com  

our mail server domain is abc.com  

``  

receivers email domain is also xyz.com

our mail flow is as below -

mail server --> email security gateway --> global domains

the outbound emails are getting deferred and expired on the email security gateway as its resolving the same domain name and the connection is refused by internal domain.

if anyone of you have come across a similar scenario, your help will be highly appreciated.

regards

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-26*

@Mohammed Nadeem       

Hi,    

Agree with Manu, you can add the particular domain to the external relay in the accpted domains settings.    

Create a specific send connector to route the emails to your gateway and also configure the DNS settings on your gateway to route the emails to the correct external domain.    

Here is a similar case for your reference: Do not want Exchange 2010 route email internally    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-25*

Add an external relay address with the external organization's domain name and try this
