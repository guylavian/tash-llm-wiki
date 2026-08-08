---
title: "Monitor Domain Controller for Authentication Requests"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/146591/monitor-domain-controller-for-authentication-reque
question_id: 146591
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Monitor Domain Controller for Authentication Requests

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/146591/monitor-domain-controller-for-authentication-reque (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I ned to migrate some 2008 R2 DCs. I'm going to stand up some 2016 DCs and migrate FSMO, DHCP etc., but what's the best way to force clients to never use the 2008 DCs and/or monitor them to see what ongoing clients/applications are using them?  

I know of LDAP Server Weight and Priority reg keys but never had a reason to use them. This is a specific scenario where it could seem appropriate?  

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-31*

I'm concerned some legacy apps will be hard-coded   

Still should work, just setup the logging.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-30*

Should just happen automatically unless you have somehow hard coded clients. Just check your DHCP server is handing out the addresses for the new domain controllers Also something here may also help.  

https://support.microsoft.com/en-us/help/556015  

--please don't forget to Accept as answer if the reply is helpful--
