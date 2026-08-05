---
title: "How to make more secure Exchange 2019 OWA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/413701/how-to-make-more-secure-exchange-2019-owa
question_id: 413701
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to make more secure Exchange 2019 OWA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/413701/how-to-make-more-secure-exchange-2019-owa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are currently using basic authentication / FBA for OWA, but it looks unsecure in the modern world.  

What are best practices to secure OWA?  

We tested 2 options:  

-  ADFS authentication;  

-  Windows authentication (we were trying to use Kerberos as it's described in the article https://techcommunity.microsoft.com/t5/iis-support-blog/setting-up-kerberos-authentication-for-a-website-in-iis/ba-p/347882#:~:text=%20Setting%20up%20Kerberos%20Authentication%20for%20a%20Website,be%20used.%20It%20might%20also%20use...%20More%20. But the last requires to change site's settings and we are not sure how it affects all means of clients' access).  

Best regards,  

Dmitry Horushin.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-05-28*

I would integrate with ADFS ( and use a MFA solution as well)

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-06-07*

Sounds like you need to setup Azure Modern Auth instead:    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/hybrid-modern-auth-overview?view=o365-worldwide    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/configure-exchange-server-for-hybrid-modern-authentication?view=o365-worldwide

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-06*

Hi  

Thank you.  

My superior wants to test a configuration with Kerberos authentication when requests of external OWA users are accepted by Azure based proxy servers. He believes that this configuration is easy to configure and maintain that a configuration with ADFS and MFA. But we miss a documentation how to set up OWA with Kerberos.  

Our further steps:  

-  set up an Azure proxy for external users;  

-  set up a second Exchange 2019 server to see how it works with load balancer;  

-  install the next Exchange 2019 CU and test how it affects the configuration.  

If you can help to find Microsoft recommendations/best practices how to secure Exchange OWA on-premises, it will be wonderful.  

Best regards,  

Dmitry Horushin.
