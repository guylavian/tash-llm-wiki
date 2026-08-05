---
title: "ADFS - OWA - ECP automatically signs out when loging from custom IdP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688409/adfs-owa-ecp-automatically-signs-out-when-loging-f
question_id: 1688409
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADFS - OWA - ECP automatically signs out when loging from custom IdP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688409/adfs-owa-ecp-automatically-signs-out-when-loging-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have a problem. Im logging into adfs with Keycloak as an IdP, everything works well. Im redirected from Keycloak to ADFS and then im getting redirected to OWA the to the ECP with signout request. Token is sent to LS and /ls is redirecting to logoff /ecp/auth/TimeoutLogout.aspx

My relying party settings:   

SsoLifetime : 480   

TokenLifetime : 60

Both for test.com/ECP and test.com/OWA

Additionally when logging only using /adfs/ls/IdpInitiatedSignon.aspx im getting redirected to keycloak and then redirected to succesfully logged in page on adfs, where i can see that im logged in.

What can i provide to describe problem better? How should i configure Active Directory, maybe there is a problem?

## Answers

_No answers on this thread._
