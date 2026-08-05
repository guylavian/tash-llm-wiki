---
title: "Parent Domain Controller ratio server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/275333/parent-domain-controller-ratio-server-2019
question_id: 275333
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Parent Domain Controller ratio server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/275333/parent-domain-controller-ratio-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to find out the best practices approach to the number of domain controllers a parent domain should have per number of child domains. As an example, if a parent domain has 30 child domains, 2 is sufficient, but then when you get into the hundreds, what should the ratio be? I am configuring a new domain and want to plan accordingly for a large global domain structure with multiple levels of domain hierarchy.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-17*

Hello,    

Thank you so much for posting here.    

One best practice is to try and limit the number of domains. Avoid having a multi-domain forest unless and until there is strong business requirement.    

Hope something here could be helpful.    

https://social.technet.microsoft.com/Forums/ie/en-US/7da3051b-76c7-48db-8bdd-527f7213bbe1/parent-child-domain-best-practice?forum=winserverDS    

https://mcpmag.com/articles/2010/09/29/ad-design-know-your-domains.aspx    

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
