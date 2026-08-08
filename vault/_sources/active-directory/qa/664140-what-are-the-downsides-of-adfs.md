---
title: "what are the Downsides of ADFS?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/664140/what-are-the-downsides-of-adfs
question_id: 664140
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# what are the Downsides of ADFS?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/664140/what-are-the-downsides-of-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I read in one of the blogs that there are few downsides of ADFS and one among them is that "It does not authenticate “older” web applications and or / ADFS doesn’t support a heterogeneous IT landscape.  

May I know if its true? and if it is what are the older web applications? is it old Java applications?  

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-17*

HI Piaudonn, Thank you for the reply. Currently there is another SSO tool that we are using and we want to migrate from that to ADFS. I read that it doesnt support old applications, so I just wanted to confirm that.  

The scenario is that we will authenticate connecting to AD and not Database.  

Regards  

Sridhar

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-15*

Can you be more specific on what you need?  

ADFS is a Security Token Service that can issue tokens using different protocols: WS-Trust, WS-Federation, SAML2, OAuth2 and Open ID Connect. Some of those protocols are almost 15 years old... So one could say the product deals well with old stuff :)  

Used in combination with its reverse-proxy called Web Application Proxy, you can also publish on-premises Kerberos enabled applications using ADFS for pre-authentication.     

The language on which the application is written is (almost) irrelevant. What matters is the authentication scheme. If your application is using Username and Password in a local database, you can't use ADFS for this scenario without making some changes to the application or introducing some other integration.
