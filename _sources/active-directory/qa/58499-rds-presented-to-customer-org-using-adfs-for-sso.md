---
title: "RDS presented to customer org, using ADFS for sso"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/58499/rds-presented-to-customer-org-using-adfs-for-sso
question_id: 58499
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# RDS presented to customer org, using ADFS for sso

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/58499/rds-presented-to-customer-org-using-adfs-for-sso (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We have an RDS 2012R2 environment that we need to present a customer org. for ~ 1000 x users.  

Will be RDS web or the RDAC used by customer.  

We also have an ADFS farm, externally accessible.  

We can add in the customer's ADFS as a claims provider trust, so that when they enter their creds at our ADFS it redirects to theirs for auth > send token back to our ADFS and hopefully logs them into our RDS web environment? Is this supported?!  

Are we able to use WAP in conjunction with RDS to present ADFS authentication to our customers?  

As obviously we don't wish to enter 1000 x users into our AD.  

End goal being that ******@customerorg.uk can  authenticate as himself to our RDS Web or RDAC.  

However, in this scenario not sure how we would assign resources to the customer given they are not known by our AD/RDS for group assignment?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-09*

In addition to piaudonn's comment, I can recommend the following links:  

https://web.archive.org/web/20180619155432/http://blog.tmurphy.org/2015/06/securing-rd-gateway-with-web.html  

https://www.petenetlive.com/KB/Article/0001143

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-04*

You can publish an RDP gateway with the Web Application Proxy. There is example here.  

That's for the access to the gateway. This does not provide SSO when you connect from this gateway to the actual target hosts.
