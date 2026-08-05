---
title: "Exchange 2019 OWA and ECP session logout not effective"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1654705/exchange-2019-owa-and-ecp-session-logout-not-effec
question_id: 1654705
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 OWA and ECP session logout not effective

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1654705/exchange-2019-owa-and-ecp-session-logout-not-effec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI ，

Exchange 2019 OWA and ECP session logout not effective

Set OrganizationConfiguration - ActivityBasedAuthenticationTimeoutInterval 00:15:00
After configuring this attribute, I restarted the server, but after waiting for 15 minutes, I still did not log out of OWA or ECP

Looking forward to your reply!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-12*

Hi，

First of all, I offer a few ways that I hope can help you.

-  You can use the Get OrganizationConfiguration – ActivityBasedAuthenticationTimeoutEnabled cmdlet directive to confirm that ActivityBasedAuthenticationTimeoutEnabled is true.   If  is true，then use the Get OrganizationConfiguration- ActivityBasedAuthenticationTimeoutInterval cmdlet command to make sure your ActivityBasedAuthenticationTimeoutInterval is set correctly.

-  You clean up your browser cache or change to another browser to see if you have the same problem

Due to the heavy caching of IIS, Exchange and other services, there is a delay when logging out of your account.

The main component/feature of IIS involved is User Token Caching in IIS.  The default is 15 minutes, and so if a connection is made within 15 minutes of the last connection the cached token information is reused instead of checking with AD. 

If you want immediate effect, you may need to restart all services.
