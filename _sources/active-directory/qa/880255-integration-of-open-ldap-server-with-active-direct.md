---
title: "Integration of Open-LDAP Server with Active Directory LDS."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/880255/integration-of-open-ldap-server-with-active-direct
question_id: 880255
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Integration of Open-LDAP Server with Active Directory LDS.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/880255/integration-of-open-ldap-server-with-active-direct (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Community,    

Thank you for your support.    

I am trying to achieve Integrate Open LDAP with Microsoft Active Directory LDS.    

1)After Integrating I am not able to See all the users and groups, to list down the users and groups I need to apply different Filters(OG= users,DC=nfvi,DC=LocalDomain, OG= groups ,DC=nfvi,DC=LocalDomain.)       

2)My expectation is to see the output like expected.jpg but I am able to see like actual.jpg image attached herewith.    

Please let me know how to resolve the issue.    

Best Regards,    

Janak Jagdish Kulkarni    

+91-8087478810    

janak.kulkarni@vinaykumar  .nec.com

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-16*

What are the connection settings you've used to connect?    

ADSI Edit is just another LDAP tool.  Apache Directory Studio is another.    

You need to ensure the Naming Context is set correctly.      

For AD this is usually the RootDSE but might be different for other LDAP databases.    

Can you share an example query as well please.
