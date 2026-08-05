---
title: "Send connector for distribution list (Exchange on premise)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/123862/send-connector-for-distribution-list-exchange-on-p
question_id: 123862
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Send connector for distribution list (Exchange on premise)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/123862/send-connector-for-distribution-list-exchange-on-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to create a send connector (Exchange 2016 on premise) for specific distribution lists? Need to bypass the Barracuda spam filter (outbound) for specific lists only - when smart hosting through them external recipients do not receive the emails to the list, only internal recipients do. Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-13*

@Jack - ITP      

The sender connector is selected by the recipients domain, it cannot only work for a part of users. Here is an article about Selecting the connector for an external recipient. It may be helpful to you.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-12*

Not possible without routing through Office 365 for example and using rule-based connectors or 3rd party software such as :  

https://jaapwesselius.com/2018/04/19/source-based-routing-in-exchange/#:~:text=In%20Exchange%20server%20Send%20Connectors,the%20namespace%20of%20the%20recipient.  

https://www.ivasoft.com/routebysender2013.shtml
