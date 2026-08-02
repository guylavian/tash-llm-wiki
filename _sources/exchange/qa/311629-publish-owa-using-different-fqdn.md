---
title: "Publish Owa using different fqdn"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/311629/publish-owa-using-different-fqdn
question_id: 311629
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Publish Owa using different fqdn

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/311629/publish-owa-using-different-fqdn (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Could I use different internal and external urls for each iis virtual front end directory in exchange server   

For example:  

Owa.mail.contoso.com for owa  

Ecp.mail.contoso.com for ecp

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-15*

Hi @Mohammed Samir Ahmed  ,    

As said by Andy, it's definitely supported to use different URLs for each virtual directories with a valid certificate. That beings said, you can also consider using the same URL which is the simplest approach. Here's a blog for your reference:    

Exchange Server 2016 Client Access Namespace Configuration    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
