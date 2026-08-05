---
title: "ADFS expecting wrong anchor claim type in on-behalf-of request"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/288589/adfs-expecting-wrong-anchor-claim-type-in-on-behal
question_id: 288589
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS expecting wrong anchor claim type in on-behalf-of request

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/288589/adfs-expecting-wrong-anchor-claim-type-in-on-behal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Consider the following setup:  

On-premise ADFS 2019.  

Two Claims Provider Trusts:  

-  "Active Directory" with anchor claim type "windowsaccountname"  

-  "Identity Provider X" with anchor claim type "providerxaccountname"  

Application Group with:  

-  Server Application with client id "ABC"  

-  Web API with resource server id "ABC", with a single ClaimsProviderName set to "Identity Provider X"  

-  Web API with resource server id "XYZ"  

Authentication from Server Application "ABC" to Web API "ABC" works as expected with scopes "openid profile user_impersonation".  

Trying to obtain access token (scope openid) with on-behalf-of flow for Web API "XYZ" results in following error message on ADFS:  

MSIS9364: Cannot complete the OAuth request. An id token is required by the request but one cannot be constructed because nop Anchor claim is present. Verify the AnchorClaimType property on the associated Claims Provider Trust is set correctly.  

I verified and anchor claim "providerxaccountname" is present in the access token of Web API "ABC".  

Some further testing showed that ADFS expects the anchor claim "windowsaccountname". Why?  

P.S.: Setting a single ClaimsProviderName to "Identity Provider X" on Web API "XYZ" made no difference (nor did I expect it to).

## Answers

_No answers on this thread._
