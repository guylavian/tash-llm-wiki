---
title: "MS Exchange Service Host not starting Exchange 2013 CU13"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/122626/ms-exchange-service-host-not-starting-exchange-201
question_id: 122626
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# MS Exchange Service Host not starting Exchange 2013 CU13

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/122626/ms-exchange-service-host-not-starting-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

MS Exchange Service Host not starting Exchange 2013 CU13  

Urgency: Our Public SSL Certificate will be expired soon.  

We are unable to assign services to the newly installed certificate for not starting the MS Exchange Service Host.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-12*

Did you make change to the default Exchange security groups?    

Check if it exists in the root domain.    

Thread with similar error info:     

https://dirteam.com/dave/2012/02/07/do-not-move-rbac-role-group-out-of-the-exchange-security-group-ou/    

https://social.technet.microsoft.com/Forums/office/en-US/68ccb34e-0bf8-4893-b169-60bd8971b0b4/exchange-cu9-organization-preparation-failes?forum=exchangesvrdeploy    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-11*

Please try installing CU14 and see the issue is able to be resolved. CU14 has more bug fixes compared to the old versions of CUs
